from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3





customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

historyWindow=customtkinter.CTk()
historyWindow.title("Afnaighar ")
historyWindow.geometry("1200x700")



homeTitle=customtkinter.CTkLabel(historyWindow,text="AfnaiGhar", font=("Comic Sans MS",48,"bold"),text_color="white",fg_color="transparent")
homeTitle.grid(row=0,column=0,padx=40,pady=40)

hometabLabel=customtkinter.CTkLabel(historyWindow,text="HOME",font=("Helvetica",24),fg_color="transparent")
hometabLabel.grid(row=0,column=1,padx=(480,10),pady=(0,40))
roomtabLabel=customtkinter.CTkLabel(historyWindow,text="ROOMS",font=("Helvetica",24),fg_color="transparent")
roomtabLabel.grid(row=0,column=2,padx=10,pady=(0,40))
abouttabLabel=customtkinter.CTkLabel(historyWindow,text="ABOUT US",font=("Helvetica",24),fg_color="transparent")
abouttabLabel.grid(row=0,column=3,padx=10,pady=(0,40))
contacttabLabel=customtkinter.CTkLabel(historyWindow,text="CONTACT",font=("Helvetica",24),fg_color="transparent")
contacttabLabel.grid(row=0,column=4,padx=10,pady=(0,40))
detailstabLabel=customtkinter.CTkLabel(historyWindow,text="DETAILS",font=("Helvetica",24),fg_color="transparent")
detailstabLabel.grid(row=0,column=5,padx=10,pady=(0,40))


historyFrame=customtkinter.CTkScrollableFrame(historyWindow,corner_radius=10,fg_color="white",width=600)
historyFrame.grid(row=1,column=0,columnspan=6,padx=(100,0),pady=(100,0))
historyLabel=customtkinter.CTkLabel(historyFrame,
                                    text="Your booked history",
                                    font=("Helvetica",20,"bold"),
                                    text_color="black",
                                    corner_radius=10,)
historyLabel.grid(row=0,column=0,padx=10,pady=10)

bookhistory=customtkinter.CTkFrame(historyFrame,
                                   corner_radius=10,
                                   fg_color="#D9D9D9",)
bookhistory.grid(row=1,column=0)

uniqueId=customtkinter.CTkLabel(bookhistory,
                                text="Id : ",
                                font=("Helvetica",20),
                                text_color="black",)
uniqueId.grid(row=0,column=0,padx=(10,0),pady=10)
uniqueId=customtkinter.CTkLabel(bookhistory,
                                text="00",
                                font=("Helvetica",20),
                                text_color="black",)
uniqueId.grid(row=0,column=1)
name=customtkinter.CTkLabel(bookhistory,
                                text="sumit",
                                font=("Helvetica",20),
                                text_color="black",)
name.grid(row=0,column=2,padx=30,pady=10)
checkIn=customtkinter.CTkLabel(bookhistory,
                                text="check-in-date :",
                                font=("Helvetica",20),
                                text_color="black",)
checkIn.grid(row=0,column=4,pady=10)
checkInD=customtkinter.CTkLabel(bookhistory,
                                text="00/00/00",
                                font=("Helvetica",20),
                                text_color="black",)
checkInD.grid(row=0,column=5,pady=10,padx=(0,30))

book=customtkinter.CTkLabel(bookhistory,
                                text="Date book:",
                                font=("Helvetica",20),
                                text_color="black",)
book.grid(row=1,column=0,padx=(10,0),pady=10)

bookDate=customtkinter.CTkLabel(bookhistory,
                                text="00/00/00",
                                font=("Helvetica",20),
                                text_color="black",)
bookDate.grid(row=1,column=1,pady=10)
room=customtkinter.CTkLabel(bookhistory,
                                text="room no :",
                                font=("Helvetica",20),
                                text_color="black",)
room.grid(row=1,column=2,padx=(30,0),pady=10)
roomN=customtkinter.CTkLabel(bookhistory,
                                text=" 00 ",
                                font=("Helvetica",20),
                                text_color="black",)
roomN.grid(row=1,column=3,padx=(0,10),pady=10)
checkOut=customtkinter.CTkLabel(bookhistory,
                                text="check-out-date : ",
                                font=("Helvetica",20),
                                text_color="black",)
checkOut.grid(row=1,column=4,pady=10)
checkOutD=customtkinter.CTkLabel(bookhistory,
                                text="00/00/00",
                                font=("Helvetica",20),
                                text_color="black",)
checkOutD.grid(row=1,column=5,pady=10,padx=(0,30))

scheduledD=customtkinter.CTkLabel(bookhistory,
                                text="Booked",
                                font=("Helvetica",12),
                                text_color="#218200",)
scheduledD.grid(row=2,column=5,)
update=customtkinter.CTkButton(bookhistory,
                                text="update",
                                font=("Helvetica",12),
                                text_color="white",
                                width=40,
                                fg_color="#1CCB0C",
                                )
update.grid(row=2,column=4,padx=(40,0))

      

historyWindow.mainloop()
