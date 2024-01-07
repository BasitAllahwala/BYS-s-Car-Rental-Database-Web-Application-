from flask import Flask, render_template, request, jsonify , session, redirect, url_for
import subprocess
import sqlite3
from werkzeug.security import check_password_hash, generate_password_hash
import random
from datetime import datetime

table_name = None
search_column = None
search_row = None
email= None
account_id=None

app = Flask(__name__)
app.secret_key = '123'

def get_db_connection():
    connection = sqlite3.connect('CAR-RENTAL.db') 
    connection.row_factory = sqlite3.Row
    return connection

def get_car_data():
    try:
        connection = get_db_connection()
        cursor = connection.cursor()

        cursor.execute("SELECT Make, Model,Year,LicensePlate,RentalPricePerDay,Availability")
        car_data = cursor.fetchall()

        connection.close()
        return car_data

    except Exception as e:
        print(f"Error fetching car data: {e}")
        return []
    
@app.route("/get_cars")
def get_cars():
    car_data = get_car_data()
    return jsonify({"success": True, "data": car_data})    

@app.route("/admin", methods=["POST"])
def display_table():
    try:
        data = request.get_json()

        # Extract the tableName from the JSON data
        global table_name
        table_name = data.get("tableName")

        # Fetch column names from the database
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute(f"PRAGMA table_info({table_name})")
        column_info = cursor.fetchall()
        column_names = [info['name'] for info in column_info]
        connection.close()

        # Fetch data from the database
        connection = get_db_connection()
        cursor = connection.cursor()
        print(table_name)
        print(search_column)
        print(search_row)
        s_column = search_column
        s_row = search_row
        # Build the SQL query based on search parameters
        if s_column is not None and s_row is not None:
            cursor.execute(f"SELECT * FROM {table_name} WHERE {s_column} = ?", (s_row,))
        else:
            cursor.execute(f"SELECT * FROM {table_name}")

        rows = cursor.fetchall()
        connection.close()
        rows_as_dicts = [dict(row) for row in rows]
        
        print("Column Names:", column_names)
        # print(f"Rows: {rows_as_dicts}")
        # search_column = None
        # search_row = None
        # Render the HTML template with the data and dynamic headers
        # return render_template("admin.html", rows=rows_as_dicts, column_names=column_names, table_names=get_table_names()) and jsonify({"success": True, "message": "Data received successfully"})
        return jsonify({"success": True, "data": {"column_names": column_names, "rows": rows_as_dicts}})

    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error: {e}")

        # Return a JSON response indicating failure
        return jsonify({"success": False, "message": "An error occurred on the server."})


def get_table_names():
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    table_names = [row['name'] for row in cursor.fetchall()]
    connection.close()
    return table_names

@app.route("/Search", methods=["POST"])
def search_specific():
    data = request.get_json()
    global search_column
    search_column = data.get('searchColumn')
    global search_row
    search_row = data.get('searchRow')
    
    if data.get('searchColumn') == None:
        search_column = None
    
    if data.get('searchRow') == None :
        search_row = None

        # connection = get_db_connection()
        # cursor = connection.cursor()

        # cursor.execute(f"PRAGMA table_info({table_name})")
        # column_info = cursor.fetchall()
        # column_names = [info['name'] for info in column_info]
        # connection.close()

        # connection = get_db_connection()
        # cursor = connection.cursor()

        # print(f"Search Column: {search_column}")
        # print(f"Search Row: {search_row}")
        
        # query = f"SELECT * FROM {table_name} WHERE {search_column} = ?"
        # print(f"Generated Query: {query}")
        # cursor.execute(query, (search_row,))
        # rows = cursor.fetchall()
        # # print(f"Number of Rows Fetched: {len(rows)}")
        # connection.close()
        # rows_as_dicts = [dict(row) for row in rows]
        # print(f"Number of Rows Fetched: {len(rows_as_dicts)}")
        # # Return a JSON response with the filtered data
        # return jsonify({"success": True, "data": {"column_names": get_column_names(table_name), "rows": rows_as_dicts}})

    # except Exception as e:
    #     # Log the error for debugging purposes
    #     print(f"Error: {e}")

    #     # Return a JSON response indicating failure
    #     return jsonify({"success": False, "message": "An error occurred on the server."})
    
def get_column_names(table_name):
    connection = get_db_connection()
    cursor = connection.cursor()
    cursor.execute(f"PRAGMA table_info({table_name})")
    column_info = cursor.fetchall()
    column_names = [info['name'] for info in column_info]
    connection.close()
    return column_names    

@app.route("/")
def index():
    result = subprocess.run(['python', 'db_project.py'], stdout=subprocess.PIPE)
    output = result.stdout.decode('utf-8')
    return render_template("frontend.html", result=output)

@app.route("/cars")
def cars():
    return render_template("cars.html")

@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    # Extract email, password, and rememberMe from the JSON data
    global email
    email = data.get("email")
    password = data.get("password")
    #remember_me = data.get("rememberMe")
    print(email)
    if email == "admin" and password == "admin":
        
        # Store admin information in session
        session['is_admin'] = True
        return jsonify({"success": True, "message": "Admin LoggedIn"})

    # Authenticate the user against the SQLite database
    connection = get_db_connection()
    cursor = connection.cursor()

    # Replace 'users' with your actual table name and 'email' with the actual column name
    cursor.execute("SELECT * FROM Credentials WHERE Email=?", (email,))
    user = cursor.fetchone()

    if user and check_password_hash(user['password'], password):
        # Store user information in session
        session['user_id'] = user['AccountID']
        #session['is_admin'] = user['is_admin']

        # Authentication successful
        return render_template("cars.html") and jsonify({"success": True, "message": "Login successful!"})
    else:
        # Authentication failed
        return jsonify({"success": False, "message": "Invalid credentials"})
    
    
def generate_unique_customer_id():
    conn = get_db_connection()
    cursor = conn.cursor()
    while True:
        # Generate a random CustomerID
        customer_id = random.randint(100, 999)
        
        # Check if the CustomerID already exists in the database
        cursor.execute("SELECT * FROM Customers WHERE CustomerID = ?", (customer_id,))
        result = cursor.fetchone()
        
        # If the CustomerID doesn't exist, return it
        if not result:
            return customer_id
            
def generate_unique_payment_id():
    conn = get_db_connection()
    cursor = conn.cursor()
    while True:
        # Generate a random CustomerID
        payment_id = random.randint(100, 999)
        
        # Check if the CustomerID already exists in the database
        cursor.execute("SELECT * FROM Payments WHERE PaymentID = ?", (payment_id,))
        result = cursor.fetchone()
        
        # If the CustomerID doesn't exist, return it
        if not result:
            return payment_id
        
def generate_unique_rental_id():
    conn = get_db_connection()
    cursor = conn.cursor()
    while True:
        # Generate a random CustomerID
        rental_id = random.randint(100, 999)
        
        # Check if the CustomerID already exists in the database
        cursor.execute("SELECT * FROM Rentals WHERE RentalID = ?", (rental_id,))
        result = cursor.fetchone()
        
        # If the CustomerID doesn't exist, return it
        if not result:
            return rental_id
        
def generate_unique_location_id():
    conn = get_db_connection()
    cursor = conn.cursor()
    while True:
        # Generate a random CustomerID
        location_id = random.randint(100, 999)
        
        # Check if the CustomerID already exists in the database
        cursor.execute("SELECT * FROM Locations WHERE LocationID = ?", (location_id,))
        result = cursor.fetchone()
        
        # If the CustomerID doesn't exist, return it
        if not result:
            return location_id                  
    
@app.route("/cars", methods=["POST"])
def book_car():
    try:
        data = request.get_json()
        today_date = datetime.now().date()
        print(today_date)
        # Extract form data
        CustomerID = account_id
        name = data.get("name")
        address = data.get("address")
        location = data.get("location")
        location_address = data.get("location_address")
        phone = data.get("phone")
        booking_date = data.get("bookingDate")
        return_date = data.get("returnDate")
        Make = data.get("carName")
        year = data.get("carYear")
        cost = data.get("carPrice")
        RentalID = generate_unique_rental_id()
        CarID = data.get("CarID")
        LocationID = generate_unique_location_id()
        PaymentID = generate_unique_payment_id()
        Payment = data.get("Payment")
        PaymentMethod = data.get("PaymentMethod")
        print(CarID)
        print(Make)
        print(year)
        print(cost)
        print(email)
        print(Payment)
        print(PaymentMethod)
        print(location_address)
        # Insert form data into the database (replace this with your actual database insert code)
        connection = get_db_connection()
        cursor = connection.cursor()
        insert_query = "INSERT INTO Customers (CustomerID, name,phone, Address, StatusName) VALUES (?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (CustomerID,name,phone,address,"Active"))
        insert_query = "INSERT INTO Rentals (RentalID,CustomerID,CarID,RentalStartDate,RentalEndDate,TotalCost) VALUES (?, ?, ?, ?, ?, ?)"
        cursor.execute(insert_query, (RentalID,CustomerID,CarID,booking_date,return_date,cost))
        insert_query = "INSERT INTO Locations (LocationID,Name,Address) VALUES(?,?,?)"
        cursor.execute(insert_query, (LocationID,location,location_address))
        insert_query = "INSERT INTO Payments(PaymentID,RentalID,PaymentDate,PaymentAmount,PaymentMethod) VALUES(?,?,?,?,?)"
        cursor.execute(insert_query, (PaymentID,RentalID,booking_date,Payment,PaymentMethod))
        cursor.execute("SELECT Availability FROM Cars WHERE CarID = ?", (CarID,))
        availability_row = cursor.fetchone()
        print(f"Availability_row: {availability_row}")
        if availability_row:
            availability = availability_row['Availability']  # Adjust the key based on the actual column name
            print(f"Availability: {availability}")
        else:
            print("Availability data not found")
        
        cursor.execute("SELECT RentalID, CarID,CustomerID, RentalEndDate FROM Rentals WHERE RentalEndDate < ? ", (today_date,))
        overdue_rentals = cursor.fetchall()

        # Update StatusName for rentals with past RentalEndDate
        for rental in overdue_rentals:
            customer_id = rental['CustomerID']
            car_id = rental['CarID']

            # Update Rental status to "Returned"
            cursor.execute("UPDATE Customers SET StatusName = 'Returned' WHERE CustomerID = ?", (customer_id,))

            # Increment availability of the corresponding car by 1
            cursor.execute("UPDATE Cars SET Availability = Availability + 1 WHERE CarID = ?", (car_id,))    
        connection.commit()
        connection.close()
        
        return jsonify({"success": True, "availability": availability, "message": "Booking successful"})
    except Exception as e:
        # Log the error for debugging purposes
        print(f"Error: {e}")
        return jsonify({"success": False, "message": "An error occurred on the server."}) 
    
@app.route("/update", methods=['POST'])
def update_availability():
    try:
        # Get car_id and new_availability from the request
        car_id = request.json.get('carID')
        new_availability = request.json.get('availability')

        # Connect to the SQLite database
        conn = get_db_connection()
        cursor = conn.cursor()

        # Update the availability of the specific car in the database
        cursor.execute('UPDATE Cars SET Availability = ? WHERE CarID = ?', (new_availability, car_id))
        conn.commit()

        # Fetch the updated car details from the database
        cursor.execute('SELECT * FROM Cars WHERE CarID = ?', (car_id,))
        car = cursor.fetchone()

        conn.close()

        # Check if the car exists and return the updated details
        if car:
            return jsonify({'success': True, 'message': 'Availability updated successfully', 'car': car}), 200
        else:
            return jsonify({'success': False, 'message': 'Car not found'}), 404

    except Exception as e:
        return jsonify({'success': False, 'message': 'An error occurred', 'error': str(e)}), 500    

@app.route("/signup", methods=["POST"])
def signup():
    # Get the JSON data from the request
    data = request.get_json()
    global email
    global account_id
    account_id = random.randint(11,999)
    # Extract registration data from the JSON data
    name = data.get("name")
    email = data.get("email")
    password = data.get("password")
    #remember_me = data.get("rememberMe")

    # Validate the registration data (you may add more validation logic)
    if not name or not email or not password:
        return jsonify({"success": False, "message": "Incomplete registration data"})
    connection = get_db_connection()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM Credentials WHERE email=?", (email,))
    existing_users = cursor.fetchall()

    # If there are existing accounts with the same email, allow signup with a new password
    if existing_users:
        for user in existing_users:
            if check_password_hash(user['password'], password):
                return jsonify({"success": False, "message": "Account with this email and password already exists"})
    else:        
    # Hash the password before storing it in the database
        hashed_password = generate_password_hash(password)
        global CustomerID
        CustomerID = generate_unique_customer_id()
    # Insert the new user into the SQLite database

    # Replace 'users' with your actual table name and provide the correct column names
        insert_user_sql = "INSERT INTO Credentials (AccountID,email, password) VALUES (?, ?,?)"
        cursor.execute(insert_user_sql, (account_id,email, hashed_password))
        connection.commit()
    # Check if the insertion was successful
    if cursor.rowcount > 0:
        return jsonify({"success": True, "message": "Signup successful!"})
    else:
        return jsonify({"success": False, "message": "Signup failed"})   
    
@app.route("/admin")
def admin():
    if 'is_admin' in session and session['is_admin']:
        table_names = get_table_names()
        return render_template("admin.html", table_names=table_names)
    else:
        # Redirect to the login page if not logged in or not an admin
        return redirect(url_for('login'))
    
    
# def get_column_names(current_table):
#     connection = get_db_connection()
#     cursor = connection.cursor()
#     cursor.execute(f"PRAGMA table_info({current_table})")  # Use a parameterized query
#     column_info = cursor.fetchall()
#     column_names = [info['name'] for info in column_info]
#     connection.close()
#     return column_names

@app.route('/add_admin', methods=['POST'])
def add_admin():
    try:
        data = request.get_json()
        connection = get_db_connection()
        cursor = connection.cursor()
        cursor.execute('''
    INSERT INTO Cars (CarID, Make, Model, Year, LicensePlate, RentalPricePerDay, Availability)
    VALUES (?, ?, ?, ?, ?, ?, ?)
''', (
    data.get('cid'),
    data.get('make'),
    data.get('model'),
    data.get('year'),
    data.get('license_plate'),
    data.get('RentalPricePerday'),
    data.get('availability')
))
        connection.commit()
        
        return jsonify({"success": True, "message": "Data added successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})
    
    
def trigger_exists(cursor, trigger_name):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='trigger' AND name=?", (trigger_name,))
    return cursor.fetchone() is not None

def create_trigger(cursor, trigger_name, trigger_sql):
    if not trigger_exists(cursor, trigger_name):
        cursor.execute(trigger_sql)

def create_triggers():
    connection = get_db_connection()
    cursor = connection.cursor()

    # Trigger to update availability when a new rental is added
    create_trigger(cursor, 'decrement_availability_trigger', '''
        CREATE TRIGGER decrement_availability_trigger
        AFTER INSERT ON Rentals
        FOR EACH ROW
        BEGIN
            UPDATE Cars
            SET Availability = Availability - 1
            WHERE CarID = NEW.CarID;
        END;
    ''')
    
    create_trigger(cursor, 'update_availability_trigger', '''
        CREATE TRIGGER update_availability_trigger
        AFTER INSERT ON Rentals
        FOR EACH ROW
        WHEN NEW.RentalEndDate < CURRENT_DATE
        BEGIN
            UPDATE Customers
            SET StatusName = 'Returned'
            WHERE CustomerID = NEW.CustomerID;

            UPDATE Cars
            SET Availability = Availability + 1
            WHERE CarID = NEW.CarID;
        END;
    ''')

    # Trigger to update customer status when a rental is marked as returned
    create_trigger(cursor, 'update_customer_status_trigger', '''
        CREATE TRIGGER update_customer_status_trigger
        AFTER UPDATE OF StatusName ON Customers
        FOR EACH ROW
        WHEN NEW.StatusName = 'Returned'
        BEGIN
            UPDATE Rentals
            SET RentalEndDate = CURRENT_DATE
            WHERE CustomerID = NEW.CustomerID AND RentalEndDate IS NULL;
        END;
    ''')

    connection.commit()
    connection.close()
    
@app.route('/delete_admin', methods=['DELETE'])
def delete_car():
    try:
        data = request.get_json()
        connection = get_db_connection()
        cursor = connection.cursor()

        # Assuming the 'id' field is used to uniquely identify the row to delete
        car_id = data.get('car_id')

        # Execute the SQL DELETE statement
        cursor.execute('''
            DELETE FROM Cars
            WHERE CarID = ?
        ''', (car_id,))

        connection.commit()

        return jsonify({"success": True, "message": "Data deleted successfully"})
    except Exception as e:
        return jsonify({"success": False, "message": str(e)})    

if __name__ == "__main__":
    create_triggers()
    
    app.run(debug=True)