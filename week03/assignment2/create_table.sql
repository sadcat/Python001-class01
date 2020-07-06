create table positions
(
	id int auto_increment
		primary key,
	city varchar(100) charset utf8mb4 null,
	company varchar(100) charset utf8mb4 null,
	position varchar(100) charset utf8mb4 null,
	salary varchar(100) charset utf8mb4 null
);
