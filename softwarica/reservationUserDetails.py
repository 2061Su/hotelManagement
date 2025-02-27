import customtkinter
from tkinter import messagebox
import sqlite3
import os



def show_reservation_details(root):
    Reservation_class(root)
class Reservation_class:
    def __init__(self, parent):
        self.parent = parent

        self.search_label = customtkinter.CTkLabel(self.parent, text="Search Booking ID:", font=("Helvetica", 16))
        self.search_label.grid(row=0, column=0)

        self.search_entry = customtkinter.CTkEntry(self.parent, width=200)
        self.search_entry.grid(row=0, column=1)

        self.search_button = customtkinter.CTkButton(
            self.parent, text="Search", command=self.search_booking, fg_color="#8e99ab", hover_color="#747d8c"
        )
        self.search_button.grid(row=0, column=2)

        self.scrollable_frame = customtkinter.CTkScrollableFrame(self.parent, corner_radius=10, fg_color="white", width=400, height=400)
        self.scrollable_frame.grid(row=1, column=0, columnspan=30)

    def search_booking(self):
        """Handles the search functionality for a booking ID."""
        search_id = self.search_entry.get().strip()
        
        if not search_id:
            messagebox.showwarning("Input Error", "Please enter a Booking ID.")
            return

        # Connect to the database
        conn = sqlite3.connect('hotel_management_user.db')
        c = conn.cursor()

        # Query for specific booking ID
        c.execute("SELECT id, room_number, first_name, last_name, email, phone_number, guests, checkin_date, checkout_date FROM bookings WHERE id=?", (search_id,))
        record = c.fetchone()
        conn.close()

        # Clear previous search results
        for widget in self.scrollable_frame.winfo_children():
            widget.destroy()

        if not record:
            messagebox.showinfo("Not Found", f"No reservation found with ID {search_id}.")
            return

        # Display the found record
        booking_id, room_number, first_name, last_name, email, phone_number, guests, checkin_date, checkout_date = record
        record_frame = customtkinter.CTkFrame(self.scrollable_frame, corner_radius=10, fg_color="#D9D9D9")
        record_frame.pack(padx=10, pady=5, fill='x')

        details_text = f"""
        Booking ID: {booking_id}
        Name: {first_name} {last_name}
        Email: {email}
        Phone Number: {phone_number}
        Number of Guests: {guests}
        Check-in Date: {checkin_date}
        Check-out Date: {checkout_date}
        Room No: {room_number}
        """

        customtkinter.CTkLabel(record_frame, text=details_text, font=("Helvetica", 16), text_color="black").pack()

        # Print Button
        print_button = customtkinter.CTkButton(record_frame, text="Print", font=("Helvetica", 12), text_color="#218200",
                                               command=lambda: self.print_booking(details_text))
        print_button.pack(pady=5)

    def print_booking(self, details):
        """Prints the booking details to a text file and opens it for printing."""
        filename = "booking_details.txt"

        try:
            with open(filename, "w") as f:
                f.write(details)

            os.startfile(filename, "print")
            messagebox.showinfo("Print", "Reservation details sent to printer.")

        except Exception as e:
            messagebox.showerror("Print Error", f"Failed to print: {e}")
