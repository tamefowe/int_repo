
create_city_area_table = """
create table city_area(
city_area_id int not null auto_increment,
area varchar(32) not null,
city varchar(32) not null,
primary key(city_area_id)
);
 """

create_users_table = """
create table users(
user_id int not null auto_increment,    
last_name varchar(24) not null,
first_name varchar(24) not null,
password binary(64) not null,
authority smallint,
creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
primary key (user_id)
);
 """

create_users_email_table = """
create table users_email(
user_id  int not null,
email varchar(32) not null,
primary key (user_id),
foreign key (user_id) references users(user_id) on delete cascade
);
"""

create_users_mobile_phone_table = """
create table users_mobile_phone(
user_id  int not null,
mobile_phone varchar(16) not null,
primary key (user_id),
foreign key (user_id) references users(user_id) on delete cascade
);
"""

create_properties_table = """
create table properties(
property_id int not null auto_increment,
rent_or_sell_or_both tinyint not null,
plot_area float,
cov_area float,
bedrooms tinyint not null,
bathrooms tinyint not null,
description varchar(255),
user_id int,
city_area_id int not null,
creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
primary key (property_id),
foreign key (user_id) references users(user_id),
foreign key (city_area_id) references city_area(city_area_id)
);
"""

create_properties_reference_table = """
create table properties_reference(
property_id int not null,
reference varchar(16) not null,
primary key (property_id),
foreign key (property_id) references properties(property_id) on delete cascade
);
"""

create_property_rented_by_table = """
create table property_rented_by(
property_id int not null,
user_id int not null,
creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
primary key (property_id, user_id),
foreign key (property_id) references properties(property_id) on delete cascade,
foreign key (user_id) references users(user_id) on delete cascade
);
"""

create_checked_by_ip_table = """
create table checked_by_ip(
property_id int not null,
ip varchar(32) not null,
creation_date DATETIME DEFAULT CURRENT_TIMESTAMP,
primary key (ip, property_id),
foreign key (property_id) references properties(property_id) on delete cascade
);
"""
