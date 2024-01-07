import sqlite3

def create_tables():
    # Establish a connection
    conn = sqlite3.connect('CAR-RENTAL.db')

    # Create a cursor
    cursor = conn.cursor()

    # Execute SQL to create the Customers table
    create_customers_table_sql = """
        CREATE TABLE IF NOT EXISTS Customers (
            CustomerID INTEGER PRIMARY KEY,
            Name TEXT,
            Phone TEXT,
            Address TEXT,
            StatusName TEXT,
            FOREIGN KEY (CustomerID) REFERENCES Credentials(Customer_ID)
        )
    """

    cursor.execute(create_customers_table_sql)

    # Other tables follow the same pattern...
    # Create Cars table
    create_cars_table_sql = """
        CREATE TABLE IF NOT EXISTS Cars (
            CarID INTEGER PRIMARY KEY,
            Make TEXT,
            Model TEXT,
            Year INTEGER,
            LicensePlate TEXT,
            RentalPricePerDay REAL,
            Availability INT
        )
    """
    cursor.execute(create_cars_table_sql)

    # Create Rentals table
    create_rentals_table_sql = """
        CREATE TABLE IF NOT EXISTS Rentals (
            RentalID INTEGER PRIMARY KEY,
            CustomerID INTEGER,
            CarID INTEGER,
            RentalStartDate DATE,
            RentalEndDate DATE,
            TotalCost REAL,
            FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID),
            FOREIGN KEY (CarID) REFERENCES Cars(CarID)
        )
    """
    cursor.execute(create_rentals_table_sql)

    # Create Locations table
    create_locations_table_sql = """
        CREATE TABLE IF NOT EXISTS Locations (
            LocationID INTEGER PRIMARY KEY,
            Name TEXT,
            Address TEXT
        )
    """
    cursor.execute(create_locations_table_sql)

    # Create Payments table
    create_payments_table_sql = """
        CREATE TABLE IF NOT EXISTS Payments (
            PaymentID INTEGER PRIMARY KEY,
            RentalID INTEGER,
            PaymentDate DATE,
            PaymentAmount REAL,
            PaymentMethod TEXT,
            FOREIGN KEY (RentalID) REFERENCES Rentals(RentalID)
        )
    """
    cursor.execute(create_payments_table_sql)

    # Create Credentials table
    create_credentials_table_sql = """
        CREATE TABLE IF NOT EXISTS Credentials (
            AccountID INTEGER PRIMARY KEY,
            Email TEXT,
            PASSWORD VARCHAR
        )
    """
    cursor.execute(create_credentials_table_sql)
    conn.commit()
    conn.close()

def DeleteTables():
    conn = sqlite3.connect('CAR-RENTAL.db')  
    cursor = conn.cursor()

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    table_names = cursor.fetchall()

    for table_name in table_names:
        drop_table_sql = f"DROP TABLE IF EXISTS {table_name[0]};"
        cursor.execute(drop_table_sql)

    conn.commit()
    cursor.close()
    conn.close()

def PATH():
    import os
    database_file = 'CAR-RENTAL.db'
    db_path = os.path.abspath(database_file)
    print(f"The database is located at: {db_path}")



def insert_customers_data():
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()

    customer_data = [
        (1, 'Emily White','555-123-4567', '456 Elm Rd', 'Active'),
        (2, 'James Johnson','555-234-5678', '789 Oak Ave', 'Active'),
        (3, 'Olivia Davis','555-345-6789', '987 Pine Blvd', 'Returned'),
    	(4, 'William Wilson','555-456-7890', '654 Cedar Ln', 'Cancelled'),
    	(5, 'Sophia Brown','555-567-8901', '321 Birch St', 'Returned'),
    	(6, 'Michael Lee','555-678-9012', '555 Willow Ave', 'Active'),
    	(7, 'Ava Martinez','555-789-0123', '777 Oak Ave', 'Active'),
    	(8, 'Liam Taylor','555-890-1234', '999 Elm Rd', 'Active'),
    	(9, 'Emma Jackson','555-901-2345', '111 Maple Ln', 'Returned'),
    	(10, 'Noah Williams','555-012-3456', '222 Oak St', 'Active')
    ]

    insert_customer_sql = "INSERT INTO Customers (CustomerID, Name,Phone, Address, StatusName) VALUES (?, ?, ?, ?, ?)"
    cursor.executemany(insert_customer_sql, customer_data)

    conn.commit()
    cursor.close()
    conn.close()

def insert_cars_data():
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()

    car_data = [
        (1,"Toyota", "Camry", 2022, "ABC123", 45.00, 11),
        (2,"Honda", "Civic", 2021, "XYZ456", 40.00, 9),
        (3,"Ford", "Escape", 2022, "DEF789", 50.00, 3),
    	(4,"Chevrolet", "Malibu", 2020, "GHI123", 45.00, 2),
    	(5,"Nissan", "Altima", 2021, "JKL456", 42.00, 13),
    	(6,"Hyundai", "Elantra", 2022, "MNO789", 38.00, 6),
    	(7,"Kia", "Optima", 2020, "PQR123", 46.00, 7),
    	(8,"Subaru", "Legacy", 2021, "STU456", 48.00, 10),
    	(9,"Volkswagen", "Jetta", 2022, "VWX789", 44.00, 5),
    	(10,"Mazda", "Mazda6", 2020, "YZA123", 47.00, 8),
        (11,"Lamborghini", "Revuolto",2023,"HAKRENX",999,3)
    ]

    insert_car_sql = "INSERT INTO Cars (CarID,Make, Model, Year, LicensePlate, RentalPricePerDay, Availability) VALUES (?, ?, ?, ?, ?, ?,?)"
    cursor.executemany(insert_car_sql, car_data)

    conn.commit()
    cursor.close()
    conn.close()

def insert_rentals_data():
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()

    rental_data = [
        (11,1, 1, '2023-01-01', '2023-01-05', 225.00),
        (22,2, 2, '2023-01-02', '2023-01-06', 200.00),
        (33,3, 3, '2023-01-03', '2023-01-07', 250.00),
    	(44,4, 4, '2023-01-04', '2023-01-08', 275.00),
    	(55,5, 5, '2023-01-05', '2023-01-09', 240.00),
    	(66,6, 6, '2023-01-06', '2023-01-10', 260.00),
    	(77,7, 7, '2023-01-07', '2023-01-11', 230.00),
    	(88,8, 8, '2023-01-08', '2023-01-12', 220.00),
    	(99,9, 9, '2023-01-09', '2023-01-13', 280.00),
    	(101,10, 10, '2023-01-10', '2023-01-14', 265.00),
    ]

    insert_rental_sql = "INSERT INTO Rentals (RentalID,CustomerID, CarID, RentalStartDate, RentalEndDate, TotalCost) VALUES (?, ?, ?, ?, ?,?)"
    cursor.executemany(insert_rental_sql, rental_data)

    conn.commit()
    cursor.close()
    conn.close()


def insert_locations_data():
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()

    location_data = [
    (1, 'Downtown Office', '123 Main St'),
    (2, 'Airport Location', '456 Airport Rd'),
    (3, 'Suburban Office', '789 Elm St'),
    (4, 'Beachfront Location', '987 Ocean Blvd'),
    (5, 'Mountain Office', '321 Pine Rd'),
    (6, 'City Center Office', '555 Center St'),
    (7, 'Shopping Mall Location', '777 Mall Ave'),
    (8, 'Industrial Area Office', '999 Factory Ln'),
    (9, 'Business District Location', '111 Commerce St'),
    (10, 'Rural Office', '222 Farm Rd')
]

    insert_location_sql = "INSERT INTO Locations (LocationID, Name, Address) VALUES (?, ?, ?)"
    cursor.executemany(insert_location_sql, location_data)

    conn.commit()
    cursor.close()
    conn.close()

def insert_payments_data():
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()

    payment_data = [
        (1, 11, '2023-01-01', 225.00, 'Credit Card'),
        (2, 22, '2023-01-02', 200.00, 'Cash'),
        (3, 33, '2023-01-03', 250.00, 'Credit Card'),
    	(4, 44, '2023-01-04', 275.00, 'Credit Card'),
    	(5, 55, '2023-01-05', 240.00, 'Cash'),
    	(6, 66, '2023-01-06', 260.00, 'Credit Card'),
    	(7, 77, '2023-01-07', 230.00, 'Cash'),
    	(8, 88, '2023-01-08', 220.00, 'Credit Card'),
    	(9, 99, '2023-01-09', 280.00, 'Credit Card'),
    	(10, 101, '2023-01-10', 265.00, 'Cash')
    ]

    insert_payment_sql = "INSERT INTO Payments (PaymentID, RentalID, PaymentDate, PaymentAmount, PaymentMethod) VALUES (?, ?, ?, ?, ?)"
    cursor.executemany(insert_payment_sql, payment_data)

    conn.commit()
    cursor.close()
    conn.close()


def delete_all_rows(table_name):
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()
    delete_all_rows_sql = f"DELETE FROM {table_name}"
    cursor.execute(delete_all_rows_sql)
    conn.commit()
    cursor.close()
    conn.close()

def display_table_rows(table_name):
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()
    cursor.execute(f"SELECT * FROM {table_name}")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.commit()
    cursor.close()
    conn.close()

import sqlite3
import random

pcustomer_id=0
print("\t\tWelcome to Hakrenx's Car Rental")
def Login(Email, password):
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()
    cursor.execute("SELECT NAME FROM Credentials WHERE Email = ? AND password = ?", (Email, password))
    user = cursor.fetchone()
    conn.close()
    return user

def Signup(Name,Email, password):
    conn = sqlite3.connect('CAR-RENTAL.db')
    cursor = conn.cursor()
    #CustomerID=random.randint(1000,9999)
    pcustomer_id= 1
    cursor.execute("INSERT INTO Credentials (Customer_ID,Name,Email, password) VALUES (?, ?, ?, ?)", (pcustomer_id,Name,Email, password))
    conn.commit()
    conn.close()

def Layout():

    print("\t1.Login(If you already have an account)\t\t2.Signup(If you don't have an account/Or want to create a new one)")
    ans = int(input())
    if ans == 1:
        Email = input("Enter your Email: ")
        password = input("Enter your password: ")
        user = Login(Email, password)
        if user:
            print("Login successful!")
        else:
            print("Login failed. Please check your credentials.")
    elif ans == 2:
        New_Name = input("Enter your Full Name")
        New_Email = input("Enter your Email: ")
        New_password = input("Create your password: ")
        Signup(New_Name,New_Email, New_password)
        print("Signup successful!")
    else:
        print("Wrong Input Pressed!")

#Layout()

#ALL FUNCTIONS FOR DATABASE CREATION,DELETION,INSERTION and DISPLAYING
create_tables()
insert_customers_data()
insert_cars_data()
insert_rentals_data()
insert_locations_data()
insert_payments_data()
# DeleteTables()
# display_table_rows('Credentials')  
# delete_all_rows('Payments')     



import sqlite3

# 


#def Price()


#def AdminAdd()

#def AdminUpdate()