# # create database report;
#
# create table person_tbl
# (
#     id         int primary key auto_increment,
#     name       nvarchar(30) not null,
#     family     nvarchar(30) not null
#
# );
#
# create table user_tbl
# (
#     id        int primary key auto_increment,
#     username  nvarchar(30) not null unique,
#     password  nvarchar(30) not null,
#     access    tinyint,
#     department nvarchar(30) not null,
#     person_id int,
#     FOREIGN KEY (person_id) REFERENCES person_tbl (id)
# );
#
# create table inventory_tbl
# (
#     id        int primary key auto_increment,
#     title     nvarchar(20) not null,
#     unit      nvarchar(30) not null,
#     department nvarchar(30) not null,
#     person_id int,
#     FOREIGN KEY (person_id) REFERENCES person_tbl (id)
# );
#
#
# create table daily_report_tbl
# (
#     id        int primary key auto_increment,
#     name      nvarchar(20) not null,
#     family    nvarchar(30) not null,
#     presence  tinyint,
#     date      date,
#     hour      int,
#     department    nvarchar(30) not null,
#     person_id int,
#     FOREIGN KEY (person_id) REFERENCES person_tbl (id)
# );
#
#
#
# create table monthly_report_tbl
# (
#     id        int primary key auto_increment,
#     name      nvarchar(20) not null,
#     family    nvarchar(30) not null,
#     job       nvarchar(30) not null unique,
#     number_of_days   int,
#     number_of_hours  int,
#     department    nvarchar(30) not null,
#     person_id int,
#     FOREIGN KEY (person_id) REFERENCES person_tbl (id)
# );
#
#
# create table warehouse_tbl
# (
#     id        int primary key auto_increment,
#     title     nvarchar(20) not null,
#     code      int,
#     unit      nvarchar(30) not null unique,
#     quantity  int not null,
#     department nvarchar(30) not null,
#     person_id int,
#     FOREIGN KEY (person_id) REFERENCES person_tbl (id)
#
# );
#
# create table workers_tbl
# (
#     id        int primary key auto_increment,
#     name      nvarchar(20) not null,
#     family    nvarchar(30) not null,
#     job       nvarchar(30) not null unique,
#     daily_wages   int,
#     hourly_wages  int,
#     department    nvarchar(30) not null,
#     person_id int,
#     FOREIGN KEY (person_id) REFERENCES person_tbl (id)
# );
