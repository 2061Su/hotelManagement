from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3





customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

adminWindow=customtkinter.CTk()
adminWindow.title("Afnaighar ")
adminWindow.geometry("1200x700")



homeTitle=customtkinter.CTkLabel(adminWindow,text="AfnaiGhar", font=("Comic Sans MS",48,"bold"),text_color="white",fg_color="transparent")
homeTitle.grid(row=0,column=0,padx=40,pady=40)

bookingFrame=customtkinter.CTkScrollableFrame(adminWindow,
                                              corner_radius=10,
                                              width=400,
                                              height=600,
                                              fg_color="white",
                                              scrollbar_button_color="gray",
                                              scrollbar_button_hover_color="#5C5C5C",)
bookingFrame.grid(row=1,column=0,columnspan=6,padx=(100,0),pady=(60,0))


class Admin():
    def __init__(self, parent, f_name, l_name, username, address, email, number, check_in_date, check_out_date, n_guest, payment):
        self.adminFrame = customtkinter.CTkFrame(parent, width=30, height=60, fg_color="#D9D9D9")
        self.adminFrame.grid(row=0, column=0, padx=(70,20), pady=20)
        
        self.create_label("Room no :","1",0)
        self.create_label("First Name :", f_name, 1)
        self.create_label("Last Name :", l_name, 2)
        self.create_label("Username :", username, 3)
        self.create_label("Address :", address, 4)
        self.create_label("Email :", email, 5)
        self.create_label("Phone Number :", number, 6)
        self.create_label("Check-in Date :", check_in_date, 7)
        self.create_label("Check-out Date :", check_out_date, 8)
        self.create_label("Number of Guests :", n_guest, 9)
        self.create_label("Payment :", payment, 10)

        self.bookingButton = customtkinter.CTkButton(self.adminFrame, text="CANCEL",
                                                     font=("arial", 18, "bold"),
                                                     corner_radius=10,
                                                     height=30,
                                                     width=40,
                                                     text_color="white",
                                                     fg_color="#C95617",
                                                     hover_color="#b34e17",
                                                     command=self.cancel)
        self.bookingButton.grid(row=11, column=0, columnspan=2, pady=20)

        self.editButton = customtkinter.CTkButton(self.adminFrame, text="EDIT",
                                                  font=("arial", 18, "bold"),
                                                  corner_radius=10,
                                                  height=30,
                                                  width=40,
                                                  text_color="white",
                                                  fg_color="#B7D5B5",
                                                  hover_color="#94bf91",
                                                  cursor="hand2",
                                                  command=self.edit)
        self.editButton.grid(row=11, column=1, columnspan=5, pady=20, padx=20)

    def create_label(self, label_text, info_text, row):
        label = customtkinter.CTkLabel(self.adminFrame, text=label_text, text_color="black")
        label.grid(row=row, column=0, padx=(50, 10))
        info = customtkinter.CTkLabel(self.adminFrame, text=info_text, text_color="black")
        info.grid(row=row, column=1)

    def cancel(self):
        print("Cancel button pressed")
        
    def edit(self):
        print("edit button pressed")
        
users = [
    {"First": "sumit", "Last": "magar", "username": "sumit", "address": "surkhet", "email": "sumit@gmail.com", "number": "9833343347", "check_in_date": "08/12/2025", "check_out_date": "08/12/2025", "n_guest": "2", "payment":"Done"}
]
for i, user in enumerate(users):
    Admin(bookingFrame, user['First'], user['Last'], user['username'], user['address'], user['email'], user['number'], user['check_in_date'], user['check_out_date'], user['n_guest'], user['payment'])
adminWindow.mainloop()

# import customtkinter
# from tkinter import messagebox
# import sqlite3

# class Admin:
#     def __init__(self, parent, booking_id):
#         self.booking_id = booking_id
#         self.adminFrame = customtkinter.CTkFrame(parent, width=30, height=60, fg_color="#D9D9D9")
#         self.adminFrame.grid(row=0, column=0, padx=(70,20), pady=20)

#         self.load_data()

#     def load_data(self):
#         conn = sqlite3.connect('users.db')
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM bookings WHERE id=?", (self.booking_id,))
#         booking = cursor.fetchone()

#         if booking:
#             self.create_label("First Name :", booking[1], 0)
#             self.create_label("Last Name :", booking[2], 1)
#             self.create_label("Username :", booking[3], 2)
#             self.create_label("Address :", booking[4], 3)
#             self.create_label("Email :", booking[5], 4)
#             self.create_label("Phone Number :", booking[6], 5)
#             self.create_label("Check-in Date :", booking[7], 6)
#             self.create_label("Check-out Date :", booking[8], 7)
#             self.create_label("Number of Guests :", booking[9], 8)
#             self.create_label("Payment :", booking[10], 9)

#             self.bookingButton = customtkinter.CTkButton(self.adminFrame, text="CANCEL",
#                                                          font=("arial", 18, "bold"),
#                                                          corner_radius=10,
#                                                          height=30,
#                                                          width=40,
#                                                          text_color="white",
#                                                          fg_color="#C95617",
#                                                          hover_color="#b34e17",
#                                                          command=self.cancel)
#             self.bookingButton.grid(row=10, column=0, columnspan=2, pady=20)

#             self.editButton = customtkinter.CTkButton(self.adminFrame, text="EDIT",
#                                                       font=("arial", 18, "bold"),
#                                                       corner_radius=10,
#                                                       height=30,
#                                                       width=40,
#                                                       text_color="white",
#                                                       fg_color="#B7D5B5",
#                                                       hover_color="#94bf91",
#                                                       cursor="hand2")
#             self.editButton.grid(row=10, column=1, columnspan=5, pady=20, padx=20)
#         else:
#             messagebox.showerror("Error", "No booking found with the provided ID.")
