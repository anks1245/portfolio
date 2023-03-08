
import http
from http.client import HTTPResponse
from imp import reload
from itertools import count
from ntpath import join
import os
from django.shortcuts import render,redirect
from django.http import HttpResponse

from calc.models import About, Education, Experience, GetIP, Hero, Register
from django.core.mail import send_mail



# Create your views here.

toast_msg = ''

#essentials
def checkDevice(request,ip,page):
    
    # Let's assume that the visitor uses an iPhone...
    is_mobile = request.user_agent.is_mobile # returns True
    is_tablet = request.user_agent.is_tablet # returns False
    # request.user_agent.is_touch_capable # returns True
    is_pc = request.user_agent.is_pc # returns False
    device = ''
    if is_mobile:
        device = 'mobile'
    elif is_tablet:
        device = 'tablet'
    elif is_pc:
        device = 'pc'
    else:
        device = ''

    # Accessing user agent's browser attributes
    # request.user_agent.browser  # returns Browser(family=u'Mobile Safari', version=(5, 1), version_string='5.1')
    browser = request.user_agent.browser.family  # returns 'Mobile Safari'

    # Operating System properties
    # request.user_agent.os  # returns OperatingSystem(family=u'iOS', version=(5, 1), version_string='5.1')

    # Device properties
    # request.user_agent.device  # returns Device(family='iPhone')
    device_fam = request.user_agent.device.family  # returns 'iPhone'

    saveip = GetIP(ip_address = ip,location='',browser=browser,device= device,device_type=device_fam,visited_at=page)
    if saveip.save():
        return True
    else:
        return False




def get_ip_address(request, page):
    user_ip_address = request.META.get('HTTP_X_FORWARDED_FOR')
    if user_ip_address:
        ip = user_ip_address.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    checkDevice(request,ip,page)
    saveip = GetIP.objects.all()

    return saveip.count()
    # return ip

def show_ip_address(request):
    user_ip = get_ip_address(request)
    return render(request, "output.html", {"user_ip":user_ip})

#essential ends here

#pages

def index(request):
    ip = get_ip_address(request,'index')

    user = Register.objects.get(id = 1)
    about = About.objects.all()
    education = Education.objects.all().order_by('id').reverse()
    experience = Experience.objects.all().order_by('id').reverse()
    hero = Hero.objects.all()
    heroResp = {
            'hero':hero[0],
            'spe':hero[0].specialization
        }
    response = { 'user_ip':ip ,'heroResp':heroResp, 'user':user , 'about':about[0], 'education':education,'experience':experience }

    return render(request,'index.html',{"data":response})

def login(request):
    ip = get_ip_address(request,'login')
    if(not is_authenticated(request)):
        return render(request,'login.html',{'name':'Login'})
    else:
        return redirect('dashboard')

def logout(request):
    request.session.clear()
    request.session.flush()
    return redirect('login')


def dashboard(request):
    ip = get_ip_address(request,'dashboard')
    if(request.session.get('is_authenticated')):
        user=Register.objects.get(id = request.session.get('id'))

        pc_count = GetIP.objects.filter(device='pc').count()

        mobile_count = GetIP.objects.filter(device='mobile').count()

        others = GetIP.objects.exclude(device="mobile").exclude(device="pc").count()

        response = { 'user':user , 'count':ip, 'pc':pc_count,'mobile':mobile_count,'others':others }
        return render(request,'admin.html',{'data':response})
    else:
        return redirect('login')

def profile(request):
    if is_authenticated(request):
        
        user=Register.objects.get(id = request.session.get('id'))
        saveip = GetIP.objects.all()

        response = { 'user':user ,'visitors':saveip.count() }
        return render(request,'profile.html',{'data':response})
        
    else:
        return redirect('login')

def landingpage(request):
    if(request.session.get('is_authenticated')):
        user = Register.objects.get(id = request.session.get('id'))
        about = About.objects.all()
        education = Education.objects.all().order_by('id').reverse()
        experience = Experience.objects.all()
        hero = Hero.objects.all()

        # print(hero.count())
        heroResp = {
                'hero':'',
                'spe':''
            }
        # print(about)
        aboutHero = []
        if(hero.count() > 0):
            heroResp = {
                'hero':hero[0],
                'spe':(hero[0].specialization).split(',')
            }
        if(about.count() > 0):
                aboutHero = about[0]
        print(heroResp)
        response = { 'heroResp':heroResp, 'user':user , 'about':aboutHero, 'education':education,'experience':experience }
        return render(request,'landingpage.html',{'data':response})
        # return render(request,'landingpage.html')
    else:
        return redirect('login')
    # return HttpResponse("hi")


#pages ends here

#functionality

def auth(request):
    if request.method == 'POST':
        email_input = request.POST['email']
        password_input = request.POST['pass']

        register = Register.objects.filter(email=email_input).filter(password=password_input)

        request.session['name'] = register[0].name
        request.session['id'] = register[0].id
        request.session['is_authenticated'] = True

        # return HttpResponse(register[0].name)
        # return render(request,'admin.html',{'id':request.session.get('id'),'name':request.session.get('name')})
        return redirect('dashboard')


    else:
        return redirect('login')

def is_authenticated(request):
    if(request.session.get('is_authenticated')):
        return True
    else:
        return False

def delete_profilepic(request):
    user = Register.objects.get(id=request.session.get('id'))
    if len(user.img) > 0:
        os.remove(user.img.path)
        return True
    else:
        return False
    

def updateProfile(request):
    if request.method == 'POST':
        _email = request.POST['email']
        new_dob = request.POST['dob']
        new_name = request.POST['name']
        user = Register(id=request.session.get('id'),dob=new_dob,name=new_name,email=_email)
        user.save(update_fields=['name','dob'])
        # return redirect('profile')
    return redirect('profile') 

def update_profile_pic(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            if delete_profilepic(request):

                user = Register(id=request.session.get('id'),img=request.FILES['profile_pic'])
                user.save(update_fields=['img']) 
    
        # return HttpResponse(request.FILES['profile_pic'].size > 0)
    return redirect('profile')

def update_address(request):
    if request.method == 'POST':
        _address = request.POST['address']
        _city = request.POST['city']
        _country = request.POST['country']

        user = Register(id=request.session.get('id'),address=_address,city=_city, country= _country)
        user.save(update_fields=['address','city','country'])

    return redirect('profile')

    #editHomepage

def updateHeroImage(request):
    if request.method == 'POST':
        _img = request.POST['hero_img']

        heroImg = Hero(id = 1,hero_img=_img)

        heroImg.save(update_fields=['hero_img'])
    
    return redirect('landingpage')

def updateHeroData(request):
    if request.method == 'POST': 
        
        print(request.session.get('id'))
        ch = ''
        for res in request.POST.getlist('spe[]'):
            ch += res + ','
        
        _title = request.POST['title']
        _file = request.FILES['resume']
        _link = request.POST['video-link']

        
        heroData = Hero(id=request.session.get('id'),title= _title, specialization = ch, cv_file = _file, embedded_link = _link)

        if Hero.objects.count() > 0:
            heroData.save(update_fields=['title','cv_file','specialization','embedded_link'])
        else :
            heroData.save()
        
        
        # return HttpResponse(file)
    return redirect('landingpage')

def updateAbout(request):
    if request.method == 'POST':
    #     check = request.POST['check']

        _title = request.POST['title-about']
        _desp = request.POST['desp-about']

    #     # _degree = request.POST['degree-about']
    #     # _experience = request.POST['experience-about']
    #     # _phone = request.POST['phone-about']
    #     # _github = request.POST['github-about']
    #     # _linkedIn = request.POST['linkdin-about']

        user = Register.objects.get(id=request.session.get('id'))

        _dob = user.dob

        about = About(id = request.session.get('id'),specialization = _title,about=_desp,birthday = _dob)

        print(About.objects.count())

        if About.objects.count()>0:
    #         if check == 1:
                about.save(update_fields=['specialization','about','birthday'])
    #         else:
    #             about.save(update_fields=['degree','experience','phone','github','linkedin'])
        else:
            about.save()

    return redirect('landingpage')
    # return HttpResponse(user.dob)

def updateBio(request):
        if request.method == 'POST':
            _degree = request.POST['degree-about']
            _experience = request.POST['experience-about']
            _phone = request.POST['phone-about']
            _github = request.POST['github-about']
            _linkedIn = request.POST['linkdin-about']

            about = About(id = request.session.get('id'),degree = _degree, experience= _experience, phone = _phone,github=_github,linkedin = _linkedIn)

            if About.objects.count()>0:
    #         if check == 1:
                # about.save(update_fields=['specialization','about','birthday'])
    #         else:
                about.save(update_fields=['degree','experience','phone','github','linkedin'])
            else:
                about.save()

        return redirect('landingpage')

def addEducation(request):
    if request.method == 'POST':
        _degree = request.POST.getlist('degree[]')
        _university = request.POST.getlist('university[]')
        _start = request.POST.getlist('start[]')
        _end = request.POST.getlist('end[]')
        _description = request.POST.getlist('description[]')


        for i in range(len(_degree)):

        #     l.append(i)

            education = Education(degree = _degree[i],university = _university[i],start_year = _start[i],end_year= _end[i],desp=_description[i])

            education.save()
        
    return redirect('landingpage')

    # return HttpResponse(len(_description))

def addExperience(request):
    if request.method == 'POST':
        _role = request.POST.getlist('pos[]')
        _company = request.POST.getlist('company[]')
        _start = request.POST.getlist('start_com[]')
        _end = request.POST.getlist('end_com[]')
        _description = request.POST.getlist('description_com[]')

        for i in range(len(_role)):
            exp = Experience(role=_role[i],company=_company[i],start_year=_start[i],end_year=_end[i],desp=_description[i])
            exp.save()

    return redirect('landingpage')

            



    #end editHomepage

def sendMail(request):
    if request.method == 'POST':
        _name = request.POST['name']
        _msg = "You have a mail from "+_name+"<br>"+request.POST['message']
        _subject = request.POST['subject']
        _email = request.POST['email']

        send_mail("Message Sent Successfully",_msg,'anks1245@gmail.com',[_email],fail_silently=False)
        send_mail(_subject,_msg,'anks1245@gmail.com',['anks1245@gmail.com'],fail_silently=False)

    return HttpResponse("Email sent successfully") 

#functionality ends here
