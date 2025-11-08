create table shirts(
	dress_type varchar(50),
    quantity int
    );
    
insert into shirts values("formal_shirt",14);
insert into shirts values("causual_shirt",50);
insert into shirts values("t_shirt",30);

select * from shirts;
select quantity from shirts;
select dress_type from shirts;
select * from shirts where quantity >= 50;
select * from shirts where quantity <= 50 order by quantity;
select * from shirts where quantity <= 50 order by quantity desc;
select * from shirts where quantity > 20 order by quantity desc;
select * from shirts where quantity >=14 and quantity <=50;
select * from shirts where quantity < 14 or quantity > 50;
select * from shirts where quantity between 10 and 50;
select * from shirts where not quantity = 50;
select * from shirts where not dress_type = "t_shirt";

show tables;

show databases;

insert into shirts (dress_type) values("party wear");
insert into shirts (quantity) values(99);
select * from shirts;
/* primary key -- not null -- default --*/

create table customers(
id int not null auto_increment,
cname varchar(50) not null,
email varchar(50) not null default "no email",
amount int,
primary key(id)
);

describe customers;
show tables;
insert into customers (cname,email,amount) values ("maha","maha@gmail.com",1000);
insert into customers (cname,amount) values ("rocky",1000);
insert into customers (cname,email,amount) values ("roja","roja@gmail.com",100);
insert into customers (cname,email,amount) values ("kamala","kamala@gmail.com",500);
insert into customers (cname,amount) values ("lovely",700);
insert into customers (cname,email,amount) values ("mala","mala@gmail.com",200);
select * from customers;

select cname from customers order by cname;
select email from customers;
select email from customers where not email ="no email" ;
select cname from customers where not amount = 0;   
select cname from customers where amount between 500 and 1000; 

-- as TEMP
select amount as purchase from customers;

-- update TABLE NAME SET NEW VALUES WHERE CONDITION
update customers set email = "rockey@gmail.com" where id=2;
update customers set amount = 300 where id = 3;

-- delete FROM TABLE NAME WHERE
delete from customers where id = 5;  

-- aggregate funcation
-- microdegree database
create database microdegree;
use microdegree;

-- creation of table
create table students (
st_id int not null auto_increment,
email varchar(50),
st_fname varchar(50),
st_lname varchar(50),
login_count int,
course_count int,
signup_month int,
primary key(st_id)
);

describe students;

insert into students(email, st_fname, st_lname, login_count, course_count, signup_month) values ("maha@gmail.com", "maha", "laxmi", 100, 10, 150), ("rocky@gmail.com", "rocky", "bhai", 110, 10, 160), ("janu@gmail.com", "jaanu", "jain", 100, 10, 150), ("niraj@gmail.com", "niraj", "sharma", 102, 9, 170), ("mohil@gmail.com", "mohil", "vaidya", 111, 11, 150);
select * from students;
insert into students(email, st_fname, st_lname, login_count, course_count, signup_month) values ("fara@gmail.com", "fara", "khan", 200, 15, 159), ("sk@gmail.com", "salman", "khan", 150, 8, 178), ("kareena@gmail.com", "kareena", "khan", 210, 10, 139),  ("mala@gmail.com", "malaikha", "khan", 140, 9, 169), ("kapil@gmail.com", "kaphil", "sharma", 200, 15, 159), ("deepika@gmail.com", "deepika", "padukone", 100, 10, 150);        
insert into students(email, st_fname, st_lname, login_count, course_count, signup_month) values ("jaya@gmail.com", "jaya", "bhachhan", 200, 15, 159), ("abhi@gmail.com", "abhi", "shake", 100, 10, 150), ("kiccha@gmail.com", "kiccha", "sudeep", 110, 10, 158), ("deepa@gmail.com", "deepa", "laxmi", 100, 10, 150);


-- concatination ()
select concat(st_fname,' ', st_lname) as full_name from students;
select concat(st_fname,' ', st_lname) as full_name, login_count from students;

-- REPLACE CASE SEN ( CLNAME OR CHAR , CHANGE, VALUE)
select replace(st_fname,"a","@") as fullname from students; 
select replace(st_fname,"@","a") as fullname from students; 

-- truncate after 7C WITH ...SUBSTRINT(COL OR VAL, START CHAR Or start, HOW MANY CHAR Or end)
select email from students;
select substring(email,1,7) from students;

-- truncate ... using concat
select concat(substring(email,1,7),"...") as TRUNCAT from students;

-- length of emails
select  count(email) as count from students;

-- char_length
select char_length(email) from students;
select email, char_length(email) as length from students;

-- REVERSE CHAR
select reverse(email) from students;

-- uppercase
select upper(st_fname) from students;
select lower(st_fname) from students;