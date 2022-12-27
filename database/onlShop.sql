CREATE DATABASE onlShop;
USE onlShop;


-- TABLES CREATION ------------------------------------
DROP TABLE product;
CREATE TABLE Product(
	product_id INT,
    date_added DATE,
    price DOUBLE,
    image TEXT,
    brand VARCHAR(20),
    model VARCHAR(20),
    quantity INT,
    name VARCHAR(100),
    discount_amount INT,
    date_updated DATE,
    
    PRIMARY KEY (product_id)
);

DROP TABLE customer;
CREATE TABLE Customer(
	user_id INT AUTO_INCREMENT,
    email VARCHAR(50),
    password VARCHAR(10),
    balance DOUBLE,
    username VARCHAR(20),
    Bdate DATE,
    Fname VARCHAR(20),
    Lname VARCHAR(20),
    floor INT,
    street VARCHAR(30),
    area VARCHAR(30),
    city VARCHAR(30),
    country VARCHAR(30),
    
    PRIMARY KEY (user_id)
);


DROP TABLE VIEWS;
CREATE TABLE Views(
	user_id INT,
    product_id INT,
    times_viewed INT,
    
    FOREIGN KEY (user_id) REFERENCES Customer(user_id)
		ON DELETE RESTRICT 
		ON UPDATE CASCADE,
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
		ON DELETE RESTRICT
		ON UPDATE CASCADE,
    PRIMARY KEY (user_id, product_id)
);

DROP TABLE Order_;
CREATE TABLE Order_(
	order_id INT,
    total_price DOUBLE,
    payment_method ENUM('Visa', 'Cash'),
    floor INT,
    street VARCHAR(30),
    area VARCHAR(30),
    city VARCHAR(30),
    country VARCHAR(30),
    dateTime_placed DATETIME,
    customer_id INT,
    
    FOREIGN KEY (customer_id) REFERENCES Customer(user_id)
		ON DELETE CASCADE
		ON UPDATE CASCADE,
    PRIMARY KEY (order_id)
);


DROP TABLE category_;
CREATE TABLE Category_(
	product_id INT,
    category VARCHAR(20),
    
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (product_id)
);

DROP TABLE containment;
CREATE TABLE Containment(
	product_id INT,
    order_id INT,
    amount INT,
    
    FOREIGN KEY (product_id) REFERENCES Product(product_id)
		ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (order_id) REFERENCES Order_(order_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (product_id, order_id)
);


DROP TABLE seller;
CREATE TABLE Seller(
	user_id INT,
    email VARCHAR(50),
    password VARCHAR(10),
    username VARCHAR(20),
    name VARCHAR(50),
    floor INT,
    street VARCHAR(30),
    area VARCHAR(30),
    city VARCHAR(30),
    country VARCHAR(30),
    
    PRIMARY KEY (user_id)
);


DROP TABLE sells;
CREATE TABLE Sells(
	Product_id INT,
    user_id INT,
    
    FOREIGN KEY (Product_id) REFERENCES Product(product_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    FOREIGN KEY (user_id) REFERENCES Seller(user_id)
		ON DELETE CASCADE
        ON UPDATE CASCADE,
    PRIMARY KEY (product_id, user_id)
);

INSERT INTO Customer (user_id, email, password, balance, username, Bdate, Fname, Lname, floor, street, city, country)
VALUES (1, 'test@gmail.com', 'pass', 0.0, 'Mido', '2002-09-28', 'Mohamed', 'Tarek', 6, 'Seasame street', 'ToonCity', 'Egypt');

INSERT INTO Product(product_id, date_added, price, image, brand, model, quantity, name, discount_amount, date_updated)
VALUES (1, '2019-12-17', 100.23, 'https://images-na.ssl-images-amazon.com/images/I/71oVh2UO8xL._SL1500_.jpg,http://pisces.bbystatic.com/image2/BestBuy_US/images/products/5689/5689019_sa.jpg,https://images-na.ssl-images-amazon.com/images/I/81EzIaCamJL._SL1500_.jpg,https://images-na.ssl-images-amazon.com/images/I/71X2tAW39aL._SL1500_.jpg,https://images-na.ssl-images-amazon.com/images/I/71c8xybNthL._SL1500_.jpg,http://static.bhphoto.com/images/smallimages/1368452917000_911749.jpg,http://static.bhphoto.com/images/images500x500/sanus_vlf410_b1_vlf410_super_slim_full_motion_1368452917000_911749.jpg,http://static.bhphoto.com/images/multiple_images/thumbnails/1368452838000_IMG_316474.jpg',
		'Samsung', 'S5', 120, 'Samsung Galaxy S5 pro-max', 0, NULL);

INSERT INTO Order_ VALUES (1, 100.23, 'Cash', 1, 'gang st', 'paradise', 'Cairo', 'Egypt', 1, '2020-01-01 12:00:00');

INSERT INTO Containment VALUES(1, 1, 1);

INSERT INTO View_ (product_id, user_id, times_viewed)
VALUES (1, 1, 2);

SELECT name, brand, model, price 
FROM Product NATURAL JOIN View_ 
ORDER BY times_viewed;

INSERT INTO customer(user_id, email, password, balance, username, Bdate, Fname, Lname, floor, street, area, city, country)
VALUES (2, 'c@g.com', 1, 0.0, 'a b', '2022-12-22', 'a', 'b', NULL, NULL, NULL, NULL, NULL);

SELECT * FROM customer;
TRUNCATE TABLE customer;