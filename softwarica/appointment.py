from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3



customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")



class BookingWindow(customtkinter.CTkToplevel):
    def __init__(self, room_number, booking_id, update_room_status,refresh_callback=None):
        super().__init__()
        self.booking_id = booking_id
        self.room_number = room_number
        self.update_room_status = update_room_status
        self.refresh_callback = refresh_callback
        self.title("Afnaighar")
        self.geometry("600x700")
        self.resizable(False, False)
        self.create_widgets()
        if self.booking_id:
            self.prefill_booking_details()
    
    

    def create_widgets(self,):
        
        bookingFrame = customtkinter.CTkFrame(self, corner_radius=10, fg_color="white")
        bookingFrame.grid(row=0, column=0,padx=(70,0))

        self.roomLabel = customtkinter.CTkLabel(bookingFrame, text=f"room no :{self.room_number}", text_color="black", font=("Helvetica", 26, "bold"))
        self.roomLabel.grid(row=0, column=0, columnspan=4)
        
        # First Name
        self.userLabel = customtkinter.CTkLabel(bookingFrame, text="First Name", text_color="black")
        self.userLabel.grid(row=1, column=0, padx=(50, 10))
        self.userEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your firstname", width=200, height=30)
        self.userEntry.grid(row=1, column=1, padx=(10, 60), pady=(20, 10))

        # Last Name
        self.user1Label = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Last Name")
        self.user1Label.grid(row=2, column=0, padx=(50, 10))
        self.user1Entry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your lastname", width=200, height=30)
        self.user1Entry.grid(row=2, column=1, padx=(10, 60), pady=10)

        # Username
        self.usernameLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Username")
        self.usernameLabel.grid(row=3, column=0, padx=(50, 10))
        self.usernameEntry = customtkinter.CTkEntry(bookingFrame, width=200, height=30)
        self.usernameEntry.grid(row=3, column=1, padx=(10, 60), pady=10)

        # Address
        self.addressLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Address")
        self.addressLabel.grid(row=4, column=0, padx=(50, 10))
        self.addressEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your address", width=200, height=30)
        self.addressEntry.grid(row=4, column=1, padx=(10, 60), pady=10)

        # Email
        self.emailLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Email")
        self.emailLabel.grid(row=5, column=0, padx=(50, 10))
        self.emailEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your email", width=200, height=30)
        self.emailEntry.grid(row=5, column=1, padx=(10, 60), pady=10)

        # Phone Number
        self.numberLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Phone Number")
        self.numberLabel.grid(row=6, column=0, padx=(50, 10))
        self.numberEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your number", width=200, height=30)
        self.numberEntry.grid(row=6, column=1, padx=(10, 60), pady=10)

        # Check-in Date
        self.checkinLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Check-in Date")
        self.checkinLabel.grid(row=7, column=0, padx=(50, 10), pady=10)
        self.checkinEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter DD/MM/YYYY", width=200, height=30)
        self.checkinEntry.grid(row=7, column=1, padx=(10, 60), pady=10)

        # Check-out Date
        self.checkoutLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Check-out Date")
        self.checkoutLabel.grid(row=8, column=0, padx=(50, 10), pady=10)
        self.checkoutEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter DD/MM/YYYY", width=200, height=30)
        self.checkoutEntry.grid(row=8, column=1, padx=(10, 60), pady=10)

        # Number of Guests
        self.guestsLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Number of Guests")
        self.guestsLabel.grid(row=9, column=0, padx=(50, 10), pady=10)
        self.guestsEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter number of guests", width=200, height=30)
        self.guestsEntry.grid(row=9, column=1, padx=(10, 60), pady=10)

        # Payment
        self.paymentLabel = customtkinter.CTkLabel(bookingFrame, text="Payment", text_color="black")
        self.paymentLabel.grid(row=10, column=0, padx=(50, 10), pady=10)
        
        # Create a StringVar to hold the value of the selected payment option
        self.payment_option = StringVar(value="Cash")

        # Create and place the "Cash" radio button
        self.radio_cash = customtkinter.CTkRadioButton(bookingFrame, text="Cash", variable=self.payment_option, value="Cash", )
        self.radio_cash.grid(row=10,column=0,columnspan=2)

        # Create and place the "eSewa" radio button
        self.radio_esewa = customtkinter.CTkRadioButton(bookingFrame, text="eSewa", variable=self.payment_option, value="eSewa",)
        self.radio_esewa.grid(row=10,column=1,columnspan=3)
        

        
        # Book Button
        bookingButton = customtkinter.CTkButton(bookingFrame, text="Book", font=("arial", 20, "bold"), corner_radius=10, height=30, width=40, text_color="white", fg_color="#B7D5B5", command=self.book)
        bookingButton.grid(row=11, column=0, columnspan=3, pady=20)

        booking_details = self.get_booking_details()

    def prefill_booking_details(self):
        conn = sqlite3.connect('hotel_management_user.db')
        c = conn.cursor()
        c.execute("SELECT room_number, first_name, last_name, username, address, email, phone_number, checkin_date, checkout_date, guests, payment FROM bookings WHERE id = ?", (self.booking_id,))
        details = c.fetchone()
        conn.close()
        if details:
            (self.room_number, first_name, last_name, username, address, email, phone_number, checkin_date, checkout_date, guests, payment) = details
            self.userEntry.insert(0, first_name)
            self.user1Entry.insert(0, last_name)
            self.usernameEntry.insert(0, username)
            self.addressEntry.insert(0, address)
            self.emailEntry.insert(0, email)
            self.numberEntry.insert(0, phone_number)
            self.checkinEntry.insert(0, checkin_date)
            self.checkoutEntry.insert(0, checkout_date)
            self.guestsEntry.insert(0, guests)
            self.payment_option.set(payment)
            self.roomLabel.configure(text=f"Room No: {self.room_number}")
    def update_booking(self):
   
        if self.refresh_callback:
            self.refresh_callback()

    def get_booking_details(self):
        # Retrieve booking details by booking_id
        conn = sqlite3.connect('hotel_management_user.db')
        c = conn.cursor()
        c.execute("SELECT * FROM bookings WHERE id = ?", (self.booking_id,))
        details = c.fetchone()
        conn.close()
        return details

    def validate_input(self, first_name, last_name, username, address, email, phone_number, checkin_date, checkout_date, guests):
        if not all([first_name, last_name, username, address, email, phone_number, checkin_date, checkout_date, guests]):
            return "Please fill in all the fields."
        if "@" not in email or '.' not in email.split('@')[-1]:
            return "Please enter a valid email address."
        if not phone_number.isdigit() or len(phone_number) < 10:
            return "Please enter a valid phone number."
        
        return True

    def book(self):
        first_name = self.userEntry.get()
        last_name = self.user1Entry.get()
        username = self.usernameEntry.get()
        address = self.addressEntry.get()
        email = self.emailEntry.get()
        phone_number = self.numberEntry.get()
        checkin_date = self.checkinEntry.get()
        checkout_date = self.checkoutEntry.get()
        guests = self.guestsEntry.get()
        payment = self.payment_option.get()

        validation_result = self.validate_input(first_name, last_name, username, address, email, phone_number, checkin_date, checkout_date, guests)
        if validation_result is True:
            if self.room_number:
                conn = sqlite3.connect('hotel_management_user.db')
                c = conn.cursor()
                c.execute('''INSERT INTO bookings (room_number,first_name, last_name, username, address, email, phone_number, checkin_date, checkout_date, guests, payment) VALUES (?,?, ?, ?, ?, ?, ?, ?, ?, ?, ?)''',
                        (self.room_number,first_name, last_name, username, address, email, phone_number, checkin_date, checkout_date, guests, payment))
                conn.commit()
                conn.close()

                self.update_room_status(self.room_number, "Booked")

                messagebox.showinfo(title="Successfully Booked", message="You have successfully booked!") 
                self.destroy()
                self.update()

                
            else:
                messagebox.showerror(title="Error", message="Please fill in all the fields.")
        
       


