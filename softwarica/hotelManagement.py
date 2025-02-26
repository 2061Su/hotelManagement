import sqlite3

def create_bookings_table():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('hotel_management_user.db')
    c = conn.cursor()

    # Create the bookings table if it doesn't already exist
    c.execute('''
        CREATE TABLE IF NOT EXISTS bookings (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            room_number INTEGER,
            first_name TEXT,
            last_name TEXT,
            username TEXT,
            address TEXT,
            email TEXT,
            phone_number TEXT,
            checkin_date TEXT,
            checkout_date TEXT,
            guests INTEGER,
            payment REAL
        )
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()

# Call this function to ensure the table exists before making any insertions
create_bookings_table()


def create_rooms_table():
    # Connect to the SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('hotel_management_user.db')
    c = conn.cursor()

    # Create the rooms table if it doesn't already exist
    c.execute(''' 
        CREATE TABLE IF NOT EXISTS rooms (
            room_number INTEGER PRIMARY KEY,
            room_type TEXT,
            price_per_night REAL,
            status TEXT
        )
    ''')

    # Commit and close the connection
    conn.commit()
    conn.close()

# Call this function to ensure the table exists before making any insertions
create_rooms_table()

def insert_sample_rooms():
    conn = sqlite3.connect('hotel_management_user.db')
    c = conn.cursor()

    # Insert sample room data into the rooms table
    rooms = [
        (1, "Double Room", 17000, "Available"),
        (2, "Single Room", 10000, "Available"),
        (3, "Suite Room", 25000, "Available"),
        (4, "Deluxe Room", 20000, "Available"),
        (6,"Double Room",10000, "Available")
        (7,"Suite Room",25000, "Available")
        (8,"Deluxe Room",20000, "Available")
        (9,"Double Room",17000, "Available")
        (10,"Single Room",10000, "Available")
        (11,"Suite Room",25000, "Available")
        (12,"Deluxe Room",20000, "Available")
        (13,"Double Room",17000, "Available")
        (14,"Single Room",10000, "Available")
        (15,"Suite Room",25000, "Available")
        (16,"Deluxe Room",20000, "Available")
        (17,"Single Room",10000, "Available")
        (18,"Suite Room",25000, "Available")
        (19,"Deluxe Room",20000, "Available")
        (20,"Deluxe Room",20000, "Available")
        (21,"Deluxe Room",20000, "Available")
        # Add more rooms as needed
    ]

    c.executemany('''
        INSERT INTO rooms (room_number, room_type, price_per_night, status)
        VALUES (?, ?, ?, ?)
    ''', rooms)

    conn.commit()
    conn.close()

# Call this function to insert sample rooms data
insert_sample_rooms()
