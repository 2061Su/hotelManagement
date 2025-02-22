from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3




def cancel():
  messagebox.showinfo(title="successfully cancelled ",message="you have successfully cacelled !")

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


bookingFrame=customtkinter.CTkScrollableFrame(bookingWindow,
                                              corner_radius=10,
                                              width=400,
                                              height=600,
                                              fg_color="white",
                                              scrollbar_button_color="gray",
                                              scrollbar_button_hover_color="#5C5C5C",)
bookingFrame.grid(row=1,column=0,columnspan=6,padx=(100,0),pady=(60,0))

book1=customtkinter.CTkFrame(bookingFrame,width=30,height=60,fg_color="#D9D9D9")
book1.grid(row=0,column=0,padx=(70,20),pady=20)



userLabel=customtkinter.CTkLabel(book1,text="First Name",text_color="black")
userLabel.grid(row=0,column=0,padx=(50,10))


user1Label=customtkinter.CTkLabel(book1,text_color="black",text="Last Name")
user1Label.grid(row=1,column=0,padx=(50,10))

usernameLabel=customtkinter.CTkLabel(book1,text_color="black",text="Username")
usernameLabel.grid(row=2,column=0,padx=(50,10))

addressLabel=customtkinter.CTkLabel(book1,text_color="black",text="Address")
addressLabel.grid(row=3,column=0,padx=(50,10))


emailLabel=customtkinter.CTkLabel(book1,text_color="black",text="Email")
emailLabel.grid(row=4,column=0,padx=(50,10),)






numberLabel=customtkinter.CTkLabel(book1,text_color="black",text="Phone Number")
numberLabel.grid(row=5,column=0,padx=(50,10))


numberLabel=customtkinter.CTkLabel(book1,text_color="black",text="check-in-date")
numberLabel.grid(row=6,column=0,padx=(50,10))

numberLabel=customtkinter.CTkLabel(book1,text_color="black",text="check-out-date")
numberLabel.grid(row=7,column=0,padx=(50,10))

numberLabel=customtkinter.CTkLabel(book1,text_color="black",text="Number of guests")
numberLabel.grid(row=8,column=0,padx=(50,10))

paymentLabel=customtkinter.CTkLabel(book1,text="Payment",text_color="black")
paymentLabel.grid(row=9,column=0,padx=(50,10))


bookingButton=customtkinter.CTkButton(book1,text="CANCEL",
                                              font=("arial",18,"bold"),
                                              corner_radius=10,
                                              height=30,
                                              width=40,
                                              text_color="white",
                                              fg_color="#C95617",
                                              command=cancel
                                              )
bookingButton.grid(row=10,column=0,columnspan=2,pady=20)


#########
book2=customtkinter.CTkFrame(bookingFrame,width=30,height=60,fg_color="#D9D9D9")
book2.grid(row=1,column=0,padx=(70,20),pady=20)



userLabel=customtkinter.CTkLabel(book2,text="First Name",text_color="black")
userLabel.grid(row=0,column=0,padx=(50,10))


user1Label=customtkinter.CTkLabel(book2,text_color="black",text="Last Name")
user1Label.grid(row=1,column=0,padx=(50,10))

usernameLabel=customtkinter.CTkLabel(book2,text_color="black",text="Username")
usernameLabel.grid(row=2,column=0,padx=(50,10))

addressLabel=customtkinter.CTkLabel(book2,text_color="black",text="Address")
addressLabel.grid(row=3,column=0,padx=(50,10))


emailLabel=customtkinter.CTkLabel(book2,text_color="black",text="Email")
emailLabel.grid(row=4,column=0,padx=(50,10),)






numberLabel=customtkinter.CTkLabel(book2,text_color="black",text="Phone Number")
numberLabel.grid(row=5,column=0,padx=(50,10))


numberLabel=customtkinter.CTkLabel(book2,text_color="black",text="check-in-date")
numberLabel.grid(row=6,column=0,padx=(50,10))

numberLabel=customtkinter.CTkLabel(book2,text_color="black",text="check-out-date")
numberLabel.grid(row=7,column=0,padx=(50,10))

numberLabel=customtkinter.CTkLabel(book2,text_color="black",text="Number of guests")
numberLabel.grid(row=8,column=0,padx=(50,10))

paymentLabel=customtkinter.CTkLabel(book2,text="Payment",text_color="black")
paymentLabel.grid(row=9,column=0,padx=(50,10))


bookingButton=customtkinter.CTkButton(book2,text="CANCEL",
                                              font=("arial",18,"bold"),
                                              corner_radius=10,
                                              height=30,
                                              width=40,
                                              text_color="white",
                                              fg_color="#C95617",
                                              command=cancel
                                              )
bookingButton.grid(row=10,column=0,columnspan=2,pady=20)



      

bookingWindow.mainloop()
