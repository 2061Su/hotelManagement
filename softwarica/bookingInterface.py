from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3
from tkcalendar import DateEntry
from datetime import date

import ttkbootstrap as tb


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

def book():
  messagebox.showinfo(title="successfully booked ",message="you have successfully booked !")

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

bookingWindow=customtkinter.CTk()
bookingWindow.title("Afnaighar ")
bookingWindow.geometry("1200x700")



homeTitle=customtkinter.CTkLabel(bookingWindow,text="AfnaiGhar", font=("Comic Sans MS",48,"bold"),text_color="white",fg_color="transparent")
homeTitle.grid(row=0,column=0,padx=40,pady=40)

hometabLabel=customtkinter.CTkLabel(bookingWindow,text="HOME",font=("Helvetica",24),fg_color="transparent")
hometabLabel.grid(row=0,column=1,padx=(480,10),pady=(0,40))
roomtabLabel=customtkinter.CTkLabel(bookingWindow,text="ROOMS",font=("Helvetica",24),fg_color="transparent")
roomtabLabel.grid(row=0,column=2,padx=10,pady=(0,40))
abouttabLabel=customtkinter.CTkLabel(bookingWindow,text="ABOUT US",font=("Helvetica",24),fg_color="transparent")
abouttabLabel.grid(row=0,column=3,padx=10,pady=(0,40))
contacttabLabel=customtkinter.CTkLabel(bookingWindow,text="CONTACT",font=("Helvetica",24),fg_color="transparent")
contacttabLabel.grid(row=0,column=4,padx=10,pady=(0,40))
detailstabLabel=customtkinter.CTkLabel(bookingWindow,text="DETAILS",font=("Helvetica",24),fg_color="transparent")
detailstabLabel.grid(row=0,column=5,padx=10,pady=(0,40))


bookingFrame=customtkinter.CTkFrame(bookingWindow,corner_radius=10,fg_color="white",)
bookingFrame.grid(row=1,column=0,columnspan=6,padx=(100,0),pady=(60,0))

roomLabel=customtkinter.CTkLabel(bookingFrame,text="room no : 00",text_color="black",font=("Helvetica",26,"bold"))
roomLabel.grid(row=0,column=0,columnspan=4)
userLabel=customtkinter.CTkLabel(bookingFrame,text="First Name",text_color="black")
userLabel.grid(row=1,column=0,padx=(50,10))

userEntry=customtkinter.CTkEntry(bookingFrame,placeholder_text="Enter your firstname",width=200,height=30)
userEntry.grid(row=1,column=1,padx=(10,60),pady=(20,10))

user1Label=customtkinter.CTkLabel(bookingFrame,text_color="black",text="Last Name")
user1Label.grid(row=2,column=0,padx=(50,10))

user1Entry=customtkinter.CTkEntry(bookingFrame,placeholder_text="Enter your lastname",width=200,height=30)
user1Entry.grid(row=2,column=1,padx=(10,60),pady=10)

usernameLabel=customtkinter.CTkLabel(bookingFrame,text_color="black",text="Username")
usernameLabel.grid(row=3,column=0,padx=(50,10))

usernameEntry=customtkinter.CTkEntry(bookingFrame,width=200,height=30)
usernameEntry.grid(row=3,column=1,padx=(10,60),pady=10)

addressLabel=customtkinter.CTkLabel(bookingFrame,text_color="black",text="Address")
addressLabel.grid(row=4,column=0,padx=(50,10))

addressEntry=customtkinter.CTkEntry(bookingFrame,placeholder_text="Enter your address",width=200,height=30,)
addressEntry.grid(row=4,column=1,padx=(10,60),pady=10)

emailLabel=customtkinter.CTkLabel(bookingFrame,text_color="black",text="Email")
emailLabel.grid(row=5,column=0,padx=(50,10),)

emailEntry=customtkinter.CTkEntry(bookingFrame,placeholder_text="Enter your email",width=200,height=30,)
emailEntry.grid(row=5,column=1,padx=(10,60),pady=10)





numberLabel=customtkinter.CTkLabel(bookingFrame,text_color="black",text="Phone Number")
numberLabel.grid(row=6,column=0,padx=(50,10))

numberEntry=customtkinter.CTkEntry(bookingFrame,placeholder_text="Enter your number",width=200,height=30)
numberEntry.grid(row=6,column=1,padx=(10,60),pady=10)

numberLabel=customtkinter.CTkLabel(bookingFrame,text_color="black",text="check-in-date")
numberLabel.grid(row=7,column=0,padx=(50,10),pady=10)

date_entry = tb.DateEntry(bookingFrame,bootstyle="primary",width=20,startdate=date(2025, 2,23))
date_entry.grid(row=7,column=1,padx=(0,320))

numberLabel=customtkinter.CTkLabel(bookingFrame,text_color="black",text="check-out-date")
numberLabel.grid(row=8,column=0,padx=(50,10),pady=10)
date_end = tb.DateEntry(bookingFrame,bootstyle="primary",width=20,startdate=date(2025, 2,23))
date_end.grid(row=8,column=1,padx=(0,320))

numberLabel=customtkinter.CTkLabel(bookingFrame,text_color="black",text="Number of guests")
numberLabel.grid(row=9,column=0,padx=(50,10),pady=10)

paymentLabel=customtkinter.CTkLabel(bookingFrame,text="Payment",text_color="black")
paymentLabel.grid(row=10,column=0,padx=(50,10),pady=10)


bookingButton=customtkinter.CTkButton(bookingFrame,text="Book",
                                              font=("arial",20,"bold"),
                                              corner_radius=10,
                                              height=30,
                                              width=40,
                                              text_color="white",
                                              fg_color="#B7D5B5",
                                              command=book
                                              )
bookingButton.grid(row=11,column=0,columnspan=3,pady=20)


      

bookingWindow.mainloop()
