create database db_skincare;
drop database db_skincare;

create table skincaredata(
id int unique identity(100,1),
uname varchar(30) not null,
email varchar(30) not null unique,
age varchar(50) not null,
skintype varchar(50) not null,
);
select * from skincaredata;

insert into skincaredata values ('hassaan','has@gmail.com','18','oil');


drop table skincare;
truncate table skincare;


alter table skincare;


insert into dry values(1,'creave',4000);
insert into dry values(2,'cetaphil',3950);
insert into dry values(3,'vnicream',4850);
insert into dry values(4,'aveeno',3800);
insert into dry values(5,'eucrein',4150);

select*from oily;
drop table dry;

insert into oily values(2,'eucrein',2000);
insert into oily values(3,'nuetrogena',3450);
insert into oily values(1,'cerave',3400);
insert into oily values(4,'la-roche-posay',7000);
insert into oily values(5,'avene',1600);

insert into acne values(1,'tozarc',300);
insert into acne values(2,'diffren gel',2000);
insert into acne values(3,' Spironolactone',300);
insert into acne values(4,'neutrgena',2000);
insert into acne values(5,'pca',1900);
