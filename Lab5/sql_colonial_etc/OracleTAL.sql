CREATE TABLE REP
(REP_NUM CHAR(2) PRIMARY KEY,
LAST_NAME CHAR(15),
FIRST_NAME CHAR(15),
STREET CHAR(15),
CITY CHAR(15),
STATE CHAR(2),
POSTAL_CODE CHAR(5),
COMMISSION DECIMAL(7,2),
RATE DECIMAL(3,2) );
CREATE TABLE CUSTOMER
(CUSTOMER_NUM CHAR(3) PRIMARY KEY,
CUSTOMER_NAME CHAR(35) NOT NULL,
STREET CHAR(20),
CITY CHAR(15),
STATE CHAR(2),
POSTAL_CODE CHAR(5),
BALANCE DECIMAL(8,2),
CREDIT_LIMIT DECIMAL(8,2),
REP_NUM CHAR(2) );
CREATE TABLE ORDERS
(ORDER_NUM CHAR(5) PRIMARY KEY,
ORDER_DATE CHAR(10),
CUSTOMER_NUM CHAR(3) );
CREATE TABLE ITEM
(ITEM_NUM CHAR(4) PRIMARY KEY,
DESCRIPTION CHAR(30),
ON_HAND DECIMAL(4,0),
CATEGORY CHAR(3),
STOREHOUSE CHAR(1),
PRICE DECIMAL(6,2) );
CREATE TABLE ORDER_LINE
(ORDER_NUM CHAR(5),
ITEM_NUM CHAR(4),
NUM_ORDERED DECIMAL(3,0),
QUOTED_PRICE DECIMAL(6,2),
PRIMARY KEY (ORDER_NUM, ITEM_NUM) );
INSERT INTO REP
VALUES
('15','Campos','Rafael','724 Vinca Dr.','Grove','CA','90092',23457.50,0.06);
INSERT INTO REP
VALUES
('30','Gradey','Megan','632 Liatris St.','Fullton','CA','90085',41317.00,0.08);
INSERT INTO REP
VALUES
('45','Tian','Hui','1785 Tyler Ave.','Northfield','CA','90098',27789.25,0.06);
INSERT INTO REP
VALUES
('60','Sefton','Janet','267 Oakley St.','Congaree','CA','90097',0.00,0.06);
INSERT INTO CUSTOMER
VALUES
('126','Toys Galore','28 Laketon St.','Fullton','CA','90085',1210.25,7500.00,'15');
INSERT INTO CUSTOMER
VALUES
('260','Brookings Direct','452 Columbus Dr.','Grove','CA','90092',575.00,10000.00,'30');
INSERT INTO CUSTOMER
VALUES
('334','The Everything Shop','342 Magee St.','Congaree','CA','90097',2345.75,7500.00,'45');
INSERT INTO CUSTOMER
VALUES
('386','Johnson''s Department Store','124 Main St.','Northfield','CA','90098',879.25,7500.00,'30');
INSERT INTO CUSTOMER
VALUES
('440','Grove Historical Museum Store','3456 Central Ave.','Fullton','CA','90085',345.00,5000.00,'45');
INSERT INTO CUSTOMER
VALUES
('502','Cards and More','167 Hale St.','Mesa','CA','90104',5025.75,5000.00,'15');
INSERT INTO CUSTOMER
VALUES
('586','Almondton General Store','3345 Devon Ave.','Almondton','CA','90125',3456.75,15000.00,'45');
INSERT INTO CUSTOMER
VALUES
('665','Cricket Gift Shop','372 Oxford St.','Grove','CA','90092',678.90,7500.00,'30');
INSERT INTO CUSTOMER
VALUES
('713','Cress Store','12 Rising Sun Ave.','Congaree','CA','90097',4234.60,10000.00,'15');
INSERT INTO CUSTOMER
VALUES
('796','Unique Gifts','786 Passmore St.','Northfield','CA','90098',124.75,7500.00,'45');
INSERT INTO CUSTOMER
VALUES
('824','Kline''s','945 Gilham St.','Mesa','CA','90104',2475.99,15000.00,'30');
INSERT INTO CUSTOMER
VALUES
('893','All Season Gifts','382 Wildwood Ave.','Fullton','CA','90085',935.75,7500.00,'15');
INSERT INTO ORDERS
VALUES
('51608','10-12-2015','126');
INSERT INTO ORDERS
VALUES
('51610','10-12-2015','334');
INSERT INTO ORDERS
VALUES
('51613','10-13-2015','386');
INSERT INTO ORDERS
VALUES
('51614','10-13-2015','260');
INSERT INTO ORDERS
VALUES
('51617','10-15-2015','586');
INSERT INTO ORDERS
VALUES
('51619','10-15-2015','126');
INSERT INTO ORDERS
VALUES
('51623','10-15-2015','586');
INSERT INTO ORDERS
VALUES
('51625','10-16-2015','796');
INSERT INTO ITEM
VALUES
('AH74','Patience',9.00,'GME','3',22.99);
INSERT INTO ITEM
VALUES
('BR23','Skittles',21.00,'GME','2',29.99);
INSERT INTO ITEM
VALUES
('CD33','Wood Block Set (48 piece)',36.00,'TOY','1',89.49);
INSERT INTO ITEM
VALUES
('DL51','Classic Railway Set',12.00,'TOY','3',107.95);
INSERT INTO ITEM
VALUES
('DR67','Giant Star Brain Teaser',24.00,'PZL','2',31.95);
INSERT INTO ITEM
VALUES
('DW23','Mancala',40.00,'GME','3',50.00);
INSERT INTO ITEM
VALUES
('FD11','Rocking Horse',8.00,'TOY','3',124.95);
INSERT INTO ITEM
VALUES
('FH24','Puzzle Gift Set',65.00,'PZL','1',38.95);
INSERT INTO ITEM
VALUES
('KA12','Cribbage Set',56.00,'GME','3',75.00);
INSERT INTO ITEM
VALUES
('KD34','Pentominoes Brain Teaser',60.00,'PZL','2',14.95);
INSERT INTO ITEM
VALUES
('KL78','Pick Up Sticks',110.00,'GME','1',10.95);
INSERT INTO ITEM
VALUES
('MT03','Zauberkasten Brain Teaser',45.00,'PZL','1',45.79);
INSERT INTO ITEM
VALUES
('NL89','Wood Block Set (62 piece)',32.00,'TOY','3',119.75);
INSERT INTO ITEM
VALUES
('TR40','Tic Tac Toe',75.00,'GME','2',13.99);
INSERT INTO ITEM
VALUES
('TW35','Fire Engine',30.00,'TOY','2',118.95);
INSERT INTO ORDER_LINE
VALUES
('51608','CD33',5.00,86.99);
INSERT INTO ORDER_LINE
VALUES
('51610','KL78',25.00,10.95);
INSERT INTO ORDER_LINE
VALUES
('51610','TR40',10.00,13.99);
INSERT INTO ORDER_LINE
VALUES
('51613','DL51',5.00,104.95);
INSERT INTO ORDER_LINE
VALUES
('51614','FD11',1.00,124.95);
INSERT INTO ORDER_LINE
VALUES
('51617','NL89',4.00,115.99);
INSERT INTO ORDER_LINE
VALUES
('51617','TW35',3.00,116.95);
INSERT INTO ORDER_LINE
VALUES
('51619','FD11',2.00,121.95);
INSERT INTO ORDER_LINE
VALUES
('51623','DR67',5.00,29.95);
INSERT INTO ORDER_LINE
VALUES
('51623','FH24',12.00,36.95);
INSERT INTO ORDER_LINE
VALUES
('51623','KD34',10.00,13.10);
INSERT INTO ORDER_LINE
VALUES
('51625','MT03',8.00,45.79);

