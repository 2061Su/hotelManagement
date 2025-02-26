import customtkinter
from tkinter import messagebox
import sqlite3

def show_reservation_details(root, booking_id):
    try:
        conn = sqlite3.connect('hotel_management_user.db')
        c = conn.cursor()

        # Fetch the booking details using booking_id
        c.execute("SELECT id, room_number, first_name, last_name, email, phone_number, guests, checkin_date, checkout_date FROM bookings WHERE id = ?", (booking_id,))
        record = c.fetchone()

        if not record:
            messagebox.showerror("Error", "Booking not found.")
            return

        # Extract details
        booking_id, room_number, first_name, last_name, email, phone_number, guests, checkin_date, checkout_date = record

        # Create a new Toplevel window
        details_window = customtkinter.CTkToplevel(root)
        details_window.title("Reservation Details")
        details_window.geometry("400x400")  # Adjust size as needed

        # Display all the details in the window
        labels = [
            ("Id:", booking_id),
            ("Name:", f"{first_name} {last_name}"),
            ("Email:", email),
            ("Phone Number:", phone_number),
            ("Number of Guests:", guests),
            ("Check-in Date:", checkin_date),
            ("Check-out Date:", checkout_date),
            ("Room No:", room_number),
            ("Status:", "Booked"),
        ]

        for i, (label, value) in enumerate(labels):
            customtkinter.CTkLabel(details_window, text=label, font=("Helvetica", 14), text_color="black").grid(row=i, column=0, padx=10, pady=5, sticky="w")
            customtkinter.CTkLabel(details_window, text=str(value), font=("Helvetica", 14), text_color="black").grid(row=i, column=1, padx=10, pady=5, sticky="w")

    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

    finally:
        conn.close()
