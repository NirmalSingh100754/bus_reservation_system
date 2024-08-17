import sqlite3
con = sqlite3.Connection("bus")
cur = con.cursor()
cur.execute("create table if not exists operators(operator_id int,name varchar(30),address varchar(50),phone bigint,email varchar(50),CONSTRAINT operators_pk PRIMARY KEY(operator_id))")
cur.execute(
    "insert into operators values(1,'KAMLA TRAVELS','GUNA M.P.',1231231234,'kamlatravels@gmail.com')")
cur.execute(
    "insert into operators values(2,'RAHUL TRAVELS','VARANASI U.P.',1111111111,'rahultravels@gmail.com')")
cur.execute(
    "insert into operators values(3,'AKASH TRAVELS','INDORE M.P.',2222222222,'akashtravels@gmail.com')")
cur.execute(
    "insert into operators values(4,'KUMMAN TRAVELS','GUNA M.P.',3333333333,'kummantravels@gmail.com')")
cur.execute("insert into operators values(5,'NIRMAL TRAVELS','MIRZAPUR U.P.',1111122222,'nirmaltravels@gmail.com')")

cur.execute("create table if not exists route_details(route_id int,station_Name varchar(30),station_id int,mark int,CONSTRAINT route_det_pk PRIMARY KEY(route_id,station_id))")
cur.execute("insert into route_details values (10, 'GUNA' ,100,0)")
cur.execute("insert into route_details values (11, 'GUNA' ,100,1)")
cur.execute("insert into route_details values (10, 'SADA' ,101,0)")
cur.execute("insert into route_details values (11, 'SADA' ,101,1)")
cur.execute("insert into route_details values (10, 'BINAGANJ' ,102,0)")
cur.execute("insert into route_details values (11, 'BINAGANJ' ,102,1)")
cur.execute("insert into route_details values (12, 'ALLAHABAD' ,106,0)")
cur.execute("insert into route_details values (13, 'ALLAHABAD' ,106,1)")
cur.execute("insert into route_details values (12, 'VARANASI' ,108,0)")
cur.execute("insert into route_details values (13, 'VARANASI' ,108,1)")

cur.execute("create table if not exists bus_details(busid int,bustype varchar(30),capacity int,fare int,operator_id int,route_id int,CONSTRAINT bus_det_pk PRIMARY KEY(busid),CONSTRAINT bus_det_fk1 foreign key (operator_id) REFERENCES operators (operator_id) ON DELETE CASCADE,CONSTRAINT bus_det_fk2 foreign key (route_id) REFERENCES route_details (route_id) ON DELETE CASCADE)")
cur.execute("insert into bus_details values (1000,'AC 2X2',35,1500,1,10)")
cur.execute("insert into bus_details values (1001,'AC 3X2',35,1200,2,11)")
cur.execute("insert into bus_details values (1002,'AC 3X3',35,1250,3,10)")
cur.execute("insert into bus_details values (1003,'SLEEPER 2X2',40,800,4,10)")
cur.execute("insert into bus_details values (1004,'SLEEPER 3X3',42,850,5,11)")
cur.execute("insert into bus_details values (1005,'SLEEPER 3X3',50,900,5,12)")
cur.execute("insert into bus_details values (1006,'SLEEPER 3X3',50,900,5,13)")

cur.execute("create table if not exists run_details(bus_id int,running_date date,seat_avl int,CONSTRAINT run_det_pk PRIMARY KEY(bus_id,running_date),CONSTRAINT run_det_fk FOREIGN KEY(bus_id) references bus_details(busid) ON DELETE CASCADE)")
cur.execute("insert into run_details values(1000,'2023-12-16',35)")
cur.execute("insert into run_details values(1001,'2023-12-16',35)")
cur.execute("insert into run_details values(1002,'2023-12-18',35)")
cur.execute("insert into run_details values(1003,'2023-12-19',40)")
cur.execute("insert into run_details values(1004,'2023-12-20',42)")
cur.execute("insert into run_details values(1005,'2023-12-15',50)")
cur.execute("insert into run_details values(1006,'2023-12-15',50)")
con.commit()