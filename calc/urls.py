from django.urls import path

from . import views

urlpatterns = [
    path('',views.index,name='home'),
    path('login',views.login,name='login'),
    path('dashboard',views.dashboard,name='dashboard'),
    path('profile',views.profile,name='profile'),
    path('landingpage',views.landingpage,name='landingpage'),
    path('logout',views.logout,name='logout'),

    # forms
    path('auth',views.auth,name='Auth'),
    path('update-profile',views.updateProfile,name='update_profile'),
    path('profilepic-update',views.update_profile_pic,name='update_profile_pic'),
    path('update-address',views.update_address,name='update_address'),

    path('update-heroData',views.updateHeroData,name='heroData'),
    path('update-heroImg',views.updateHeroImage,name='heroImg'),

    path('update-about',views.updateAbout,name="update-about"),
    path('update-bio',views.updateBio,name='updateBio'),

    path('add-education',views.addEducation,name="addEducation"),
    path('add-experience',views.addExperience,name="addExperience"),
]