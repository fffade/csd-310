/*
    Group 2
    Module 10.1 Assignment
    11/28/23
    Description: Create the database for Outland Adventures.
*/

-- Last updated 12/03/23

/* RESET */
/*DROP TABLE booking;
DROP TABLE trip;
DROP TABLE guide;
DROP TABLE location;
DROP TABLE equipment;
DROP TABLE equipment_order;
DROP TABLE equipment_purchase;
DROP TABLE equipment_rental;
DROP TABLE customer;*/

-- CUSTOMER TABLE
CREATE TABLE customer (
    customer_id     INT             NOT NULL AUTO_INCREMENT,
    customer_Lname   VARCHAR(75)     NOT NULL,
    customer_Fname   VARCHAR(75)     NOT NULL,
    customer_email   VARCHAR(75)     NOT NULL,
     
    PRIMARY KEY(customer_id)
); 


-- GUIDES TABLE
CREATE TABLE guide (
    guide_id	INT	NOT NULL	AUTO_INCREMENT,
    guide_Fname VARCHAR(75)     NOT NULL,
    guide_Lname VARCHAR(75)     NOT NULL,
	
    PRIMARY KEY(guide_id)
);


-- LOCATIONS TABLE
CREATE TABLE location (
    location_id	INT	NOT NULL	AUTO_INCREMENT,
    location_name VARCHAR(75)     NOT NULL,
    	
    PRIMARY KEY(location_id)
);


-- TRIPS TABLE
CREATE TABLE trip(
    trip_id	INT	NOT NULL	AUTO_INCREMENT,
    trip_name	VARCHAR(75) NOT NULL,
    trip_price	INT NOT NULL,
    trip_length	INT NOT NULL,
	trip_startDate DATE NOT NULL,
    location_id INT NOT NULL,
    guide_id	INT NOT NULL,

    PRIMARY KEY(trip_id),

    CONSTRAINT fk_trip_location
    FOREIGN KEY(location_id)
        REFERENCES location(location_id),
		
    CONSTRAINT fk_trip_guide
    FOREIGN KEY(guide_id)
        REFERENCES guide(guide_id)	
);

-- BOOKINGS TABLE
CREATE TABLE booking (
    booking_id	INT	NOT NULL	AUTO_INCREMENT,
    booking_date DATE     NOT NULL,
    customer_id INT NOT NULL,
    trip_id INT NOT NULL,
	
    PRIMARY KEY(booking_id),

	CONSTRAINT fk_booking_customer
    FOREIGN KEY(customer_id)
        REFERENCES customer(customer_id),
		
    CONSTRAINT fk_booking_trip
    FOREIGN KEY(trip_id)
        REFERENCES trip(trip_id)	
);


-- EQIPMENT ORDERS TABLE
CREATE TABLE equipment_order (
    order_id	INT	NOT NULL	AUTO_INCREMENT,
    order_date DATE     NOT NULL,
    order_quantity INT     NOT NULL,
	
    PRIMARY KEY(order_id)
);


-- EQIPMENT ITEMS TABLE
CREATE TABLE equipment (
    equipment_id	INT	NOT NULL AUTO_INCREMENT,
    equipment_name VARCHAR(75)     NOT NULL,
    order_id INT NOT NULL,
	
    PRIMARY KEY(equipment_id),

    CONSTRAINT fk_equipment_order
    FOREIGN KEY(order_id)
        REFERENCES equipment_order(order_id)
);

-- EQIPMENT RENTAL TABLE
CREATE TABLE equipment_rental (
    rental_id	INT	NOT NULL	AUTO_INCREMENT,
    rental_dateStart DATE     NOT NULL,
    rental_dateEnd DATE     NOT NULL,
	rental_total INT NOT NULL,
    equipment_id INT NOT NULL,
    customer_id INT NOT NULL,
	
    PRIMARY KEY(rental_id),

    CONSTRAINT fk_rental_equipment
    FOREIGN KEY(equipment_id)
        REFERENCES equipment(equipment_id),
	
	CONSTRAINT fk_rental_customer
    FOREIGN KEY(customer_id)
        REFERENCES customer(customer_id)
);

-- EQIPMENT PURCHASES TABLE
CREATE TABLE equipment_purchase(
    purchase_id	INT	NOT NULL	AUTO_INCREMENT,
    purchase_date DATE     NOT NULL,
    purchase_quantity INT     NOT NULL,
	purchase_total INT NOT NULL,
	customer_id INT NOT NULL,
    equipment_id INT NOT NULL,
	
    PRIMARY KEY(purchase_id),

    CONSTRAINT fk_purchase_equipment
    FOREIGN KEY(equipment_id)
        REFERENCES equipment(equipment_id),
	
	CONSTRAINT fk_purchase_customer
    FOREIGN KEY(customer_id)
        REFERENCES customer(customer_id)
);

-- CUSTOMER RECORDS
INSERT INTO customer(customer_Lname, customer_Fname, customer_email)
VALUES('Venture', 'Teddy', 'tedventure@yahoo.com');
INSERT INTO customer(customer_Lname, customer_Fname, customer_email)
VALUES('McName', 'Guy', 'epictreks127@gmail.com');
INSERT INTO customer(customer_Lname, customer_Fname, customer_email)
VALUES('Businessman', 'Edward', 'ebusinessman@outlook.com');
INSERT INTO customer(customer_Lname, customer_Fname, customer_email)
VALUES('Laustneme', 'Reece', 'reecelaustneme@gmail.com');
INSERT INTO customer(customer_Lname, customer_Fname, customer_email)
VALUES('Branch', 'Todd', 'treehugger1997@yahoo.com');
INSERT INTO customer(customer_Lname, customer_Fname, customer_email)
VALUES('Robinson', 'Colin', 'travelbug54@aol.com');

-- GUIDE RECORDS
INSERT INTO guide(guide_Lname, guide_Fname)
VALUES('MacNell', 'John');
INSERT INTO guide(guide_Lname, guide_Fname)
VALUES('Marland', 'D.B.');

-- LOCATION RECORDS
INSERT INTO location(location_name)
VALUES('Africa');
INSERT INTO location(location_name)
VALUES('Asia');
INSERT INTO location(location_name)
VALUES('Southern Europe');

-- TRIPS RECORDS
INSERT INTO trip(trip_name, trip_price, trip_length, trip_startDate, location_id, guide_id)
VALUES('Everest Base Camp', 3670, 14, '2025-01-05', (SELECT location_id FROM location WHERE location_name = 'Asia'), (SELECT guide_id FROM guide WHERE guide_Lname = 'MacNell'));
INSERT INTO trip(trip_name, trip_price, trip_length, trip_startDate, location_id, guide_id)
VALUES('Best of Singapore', 2290, 7, '2024-09-11', (SELECT location_id FROM location WHERE location_name = 'Asia'), (SELECT guide_id FROM guide WHERE guide_Lname = 'MacNell'));
INSERT INTO trip(trip_name, trip_price, trip_length, trip_startDate, location_id, guide_id)
VALUES('South Africa Odyssey', 2900, 14, '2024-04-23', (SELECT location_id FROM location WHERE location_name = 'Africa'), (SELECT guide_id FROM guide WHERE guide_Lname = 'Marland'));
INSERT INTO trip(trip_name, trip_price, trip_length, trip_startDate, location_id, guide_id)
VALUES('Africa Adventure', 1980, 7, '2024-06-19', (SELECT location_id FROM location WHERE location_name = 'Africa'), (SELECT guide_id FROM guide WHERE guide_Lname = 'Marland'));
INSERT INTO trip(trip_name, trip_price, trip_length, trip_startDate, location_id, guide_id)
VALUES('Dolomites Hiking Tour', 3290, 14, '2024-02-16', (SELECT location_id FROM location WHERE location_name = 'Asia'), (SELECT guide_id FROM guide WHERE guide_Lname = 'MacNell'));
INSERT INTO trip(trip_name, trip_price, trip_length, trip_startDate, location_id, guide_id)
VALUES('Montserrat Hiking Off the Beaten Path', 1750, 7, '2024-09-24', (SELECT location_id FROM location WHERE location_name = 'Asia'), (SELECT guide_id FROM guide WHERE guide_Lname = 'Marland'));


-- BOOKING TABLE
INSERT INTO booking (booking_date, customer_id, trip_id)
VALUES('2023-04-26', (SELECT customer_id FROM customer WHERE customer_Lname = 'Robinson'), (SELECT trip_id FROM trip WHERE trip_name = 'Everest Base Camp'));
INSERT INTO booking (booking_date, customer_id, trip_id)
VALUES('2023-05-10', (SELECT customer_id FROM customer WHERE customer_Lname = 'Branch'), (SELECT trip_id FROM trip WHERE trip_name = 'Best of Singapore'));
INSERT INTO booking (booking_date, customer_id, trip_id)
VALUES('2023-03-12', (SELECT customer_id FROM customer WHERE customer_Lname = 'McName'), (SELECT trip_id FROM trip WHERE trip_name = 'South Africa Odyssey'));
INSERT INTO booking (booking_date, customer_id, trip_id)
VALUES('2023-05-11', (SELECT customer_id FROM customer WHERE customer_Lname = 'Laustneme'), (SELECT trip_id FROM trip WHERE trip_name = 'Africa Adventure'));
INSERT INTO booking (booking_date, customer_id, trip_id)
VALUES('2023-11-03', (SELECT customer_id FROM customer WHERE customer_Lname = 'Venture'), (SELECT trip_id FROM trip WHERE trip_name = 'Dolomites Hiking Tour'));
INSERT INTO booking (booking_date, customer_id, trip_id)
VALUES('2023-11-26', (SELECT customer_id FROM customer WHERE customer_Lname = 'Businessman'), (SELECT trip_id FROM trip WHERE trip_name = 'Montserrat Hiking Off the Beaten Path'));

-- EQUIPMENT ORDERS TABLE
INSERT INTO equipment_order(order_date, order_quantity)
VALUES ('2021-11-14', '2');
INSERT INTO equipment_order(order_date, order_quantity)
VALUES ('2022-09-14', '1');
INSERT INTO equipment_order(order_date, order_quantity)
VALUES ('2023-05-27', '3');
INSERT INTO equipment_order(order_date, order_quantity)
VALUES ('2023-11-02', '2');

-- EQUIPMENT ITEMS TABLE
INSERT INTO equipment(equipment_name, order_id)
VALUES ('Eight Person Canvas Tent', (SELECT order_id FROM equipment_order WHERE order_date = '2021-11-14'));
INSERT INTO equipment(equipment_name, order_id)
VALUES ('Three person Canvas Tent', (SELECT order_id FROM equipment_order WHERE order_date = '2021-11-14'));
INSERT INTO equipment(equipment_name, order_id)
VALUES ('Visionner Binoculars', (SELECT order_id FROM equipment_order WHERE order_date = '2023-05-27'));
INSERT INTO equipment(equipment_name, order_id)
VALUES ('Canon EOS RP', (SELECT order_id FROM equipment_order WHERE order_date = '2023-11-02'));
INSERT INTO equipment(equipment_name, order_id)
VALUES ('Canon RF200-800mm Lens', (SELECT order_id FROM equipment_order WHERE order_date = '2023-11-02'));
INSERT INTO equipment(equipment_name, order_id)
VALUES ('Full Suspension Mountain Bike', (SELECT order_id FROM equipment_order WHERE order_date = '2022-09-14'));

-- RENTAL TABLE
INSERT INTO equipment_rental(rental_dateStart, rental_dateEnd, rental_total, equipment_id, customer_id)
VALUES ('2025-01-05', '2025-01-19', 200, (SELECT equipment_id FROM equipment WHERE equipment_name = 'Eight Person Canvas Tent'), (SELECT customer_id FROM customer WHERE customer_Lname = 'Robinson'));
INSERT INTO equipment_rental(rental_dateStart, rental_dateEnd, rental_total, equipment_id, customer_id)
VALUES ('2022-05-01', '2023-05-07', 30, (SELECT equipment_id FROM equipment WHERE equipment_name = 'Visionner Binoculars'), (SELECT customer_id FROM customer WHERE customer_Lname = 'McName'));

-- PURCHASE TABLE
INSERT INTO equipment_purchase(purchase_date, purchase_quantity, purchase_total, customer_id, equipment_id)
VALUES ('2023-09-07', 1, 1700, (SELECT equipment_id FROM equipment WHERE equipment_name = 'Full Suspension Mountain Bike'), (SELECT customer_id FROM customer WHERE customer_Lname = 'Venture'));

