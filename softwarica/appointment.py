from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class BookingWindow(customtkinter.CTkToplevel):
    def __init__(self,):
        super().__init__()
        self.title("Afnaighar")
        self.geometry("600x700")
        self.resizable(False, False)
        self.create_widgets()

    def create_widgets(self):
        bookingFrame = customtkinter.CTkFrame(self, corner_radius=10, fg_color="white")
        bookingFrame.grid(row=0, column=0,padx=(70,0))

        roomLabel = customtkinter.CTkLabel(bookingFrame, text="room no : 00", text_color="black", font=("Helvetica", 26, "bold"))
        roomLabel.grid(row=0, column=0, columnspan=4)
        
        # First Name
        userLabel = customtkinter.CTkLabel(bookingFrame, text="First Name", text_color="black")
        userLabel.grid(row=1, column=0, padx=(50, 10))
        userEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your firstname", width=200, height=30)
        userEntry.grid(row=1, column=1, padx=(10, 60), pady=(20, 10))

        # Last Name
        user1Label = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Last Name")
        user1Label.grid(row=2, column=0, padx=(50, 10))
        user1Entry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your lastname", width=200, height=30)
        user1Entry.grid(row=2, column=1, padx=(10, 60), pady=10)

        # Username
        usernameLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Username")
        usernameLabel.grid(row=3, column=0, padx=(50, 10))
        usernameEntry = customtkinter.CTkEntry(bookingFrame, width=200, height=30)
        usernameEntry.grid(row=3, column=1, padx=(10, 60), pady=10)

        # Address
        addressLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Address")
        addressLabel.grid(row=4, column=0, padx=(50, 10))
        addressEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your address", width=200, height=30)
        addressEntry.grid(row=4, column=1, padx=(10, 60), pady=10)

        # Email
        emailLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Email")
        emailLabel.grid(row=5, column=0, padx=(50, 10))
        emailEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your email", width=200, height=30)
        emailEntry.grid(row=5, column=1, padx=(10, 60), pady=10)

        # Phone Number
        numberLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Phone Number")
        numberLabel.grid(row=6, column=0, padx=(50, 10))
        numberEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter your number", width=200, height=30)
        numberEntry.grid(row=6, column=1, padx=(10, 60), pady=10)

        # Check-in Date
        checkinLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Check-in Date")
        checkinLabel.grid(row=7, column=0, padx=(50, 10), pady=10)
        checkinEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter check-in date", width=200, height=30)
        checkinEntry.grid(row=7, column=1, padx=(10, 60), pady=10)

        # Check-out Date
        checkoutLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Check-out Date")
        checkoutLabel.grid(row=8, column=0, padx=(50, 10), pady=10)
        checkoutEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter check-out date", width=200, height=30)
        checkoutEntry.grid(row=8, column=1, padx=(10, 60), pady=10)

        # Number of Guests
        guestsLabel = customtkinter.CTkLabel(bookingFrame, text_color="black", text="Number of Guests")
        guestsLabel.grid(row=9, column=0, padx=(50, 10), pady=10)
        guestsEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter number of guests", width=200, height=30)
        guestsEntry.grid(row=9, column=1, padx=(10, 60), pady=10)

        # Payment
        paymentLabel = customtkinter.CTkLabel(bookingFrame, text="Payment", text_color="black")
        paymentLabel.grid(row=10, column=0, padx=(50, 10), pady=10)
        paymentEntry = customtkinter.CTkEntry(bookingFrame, placeholder_text="Enter payment details", width=200, height=30)
        paymentEntry.grid(row=10, column=1, padx=(10, 60), pady=10)

        # Book Button
        bookingButton = customtkinter.CTkButton(bookingFrame, text="Book", font=("arial", 20, "bold"), corner_radius=10, height=30, width=40, text_color="white", fg_color="#B7D5B5", command=self.book)
        bookingButton.grid(row=11, column=0, columnspan=3, pady=20)

    def book(self):
        messagebox.showinfo(title="Successfully Booked", message="You have successfully booked!")
        self.destroy()


