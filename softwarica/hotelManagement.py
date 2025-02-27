import sqlite3

def create_bookings_table():
    
    conn = sqlite3.connect('hotel_management_user.db')
    c = conn.cursor()

   
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

   
    conn.commit()
    conn.close()




def create_rooms_table():
    
    conn = sqlite3.connect('hotel_management_user.db')
    c = conn.cursor()

    
    c.execute(''' 
        CREATE TABLE IF NOT EXISTS rooms (
            room_number INTEGER PRIMARY KEY,
            room_type TEXT,
            price_per_night REAL,
            status TEXT
        )
    ''')

    
    conn.commit()
    conn.close()




def insert_sample_rooms():
    conn = sqlite3.connect('hotel_management_user.db')
    c = conn.cursor()

    
    c.execute("SELECT COUNT(*) FROM rooms")
    if c.fetchone()[0] > 0:
        print("Rooms are already inserted.")
        conn.close()
        return

    
    rooms = [
        (1, "Double Room", 17000, "Available"),
        (2, "Single Room", 10000, "Available"),
        (3, "Suite Room", 25000, "Available"),
        (4, "Deluxe Room", 20000, "Available"),
        (5, "Double Room", 17000, "Available"),
        (6, "Single Room", 10000, "Available"),
        (7, "Suite Room", 25000, "Available"),
        (8, "Deluxe Room", 20000, "Available"),
        (9, "Double Room", 17000, "Available"),
        (10, "Single Room", 10000, "Available"),
        (11, "Suite Room", 25000, "Available"),
        (12, "Deluxe Room", 20000, "Available"),
        (13, "Double Room", 17000, "Available"),
        (14, "Single Room", 10000, "Available"),
        (15, "Suite Room", 25000, "Available"),
        (16, "Deluxe Room", 20000, "Available"),
        (17, "Single Room", 10000, "Available"),
        (18, "Suite Room", 25000, "Available"),
        (19, "Deluxe Room", 20000, "Available"),
        (20, "Deluxe Room", 20000, "Available"),
        (21, "Deluxe Room", 20000, "Available"),
    ]

    
    c.executemany(''' 
        INSERT INTO rooms (room_number, room_type, price_per_night, status)
        VALUES (?, ?, ?, ?)
    ''', rooms)

    conn.commit()
    conn.close()
    print("Sample rooms inserted successfully.")

if __name__ == "__main__":
    create_rooms_table()
    create_bookings_table()
    insert_sample_rooms()