show databases;
use ai_sangari;
show tables;
create table Student_details(Sno int auto_increment not null primary key ,
 Name varchar(50) not null , 
 Tamil int not null ,
 English  int not null , 
 Maths int not null , 
 Science int not null , 
 Social int not null , 
 Total int not null);
 
 select * from Student_details;
 alter table Student_details drop column Total;
