-- SQLite
-- INSERT INTO calc_hero(title,specialization,hero_img,cv_file,embedded_link,updated_at) 
-- VALUES ("Ankit Ram Nag","Android Developer, Web Developer","uploads/image-front.jpeg","","",CURRENT_TIMESTAMP);

-- DELETE FROM calc_hero WHERE id=4;

-- SELECT * from calc_about;

-- INSERT INTO calc_about(specialization,about,birthday,degree,experience,phone,github,linkedin,updated_at) 
-- VALUES ("","","","","","","","",CURRENT_TIMESTAMP);

UPDATE calc_register SET dob='2002-04-18' WHERE id=1;