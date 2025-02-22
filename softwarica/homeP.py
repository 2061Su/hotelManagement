from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image,ImageTk
import sqlite3




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

mainWindow=customtkinter.CTk()
mainWindow.title("Afnaighar ")
mainWindow.geometry("1200x700")



homeTitle=customtkinter.CTkLabel(mainWindow,text="AfnaiGhar", font=("Comic Sans MS",48,"bold"),text_color="white",fg_color="transparent")
homeTitle.grid(row=0,column=0,padx=40,pady=40)

hometabLabel=customtkinter.CTkLabel(mainWindow,text="HOME",font=("Helvetica",24),fg_color="transparent")
hometabLabel.grid(row=0,column=1,padx=(480,10),pady=(0,40))
roomtabLabel=customtkinter.CTkLabel(mainWindow,text="ROOMS",font=("Helvetica",24),fg_color="transparent")
roomtabLabel.grid(row=0,column=2,padx=10,pady=(0,40))
abouttabLabel=customtkinter.CTkLabel(mainWindow,text="ABOUT US",font=("Helvetica",24),fg_color="transparent")
abouttabLabel.grid(row=0,column=3,padx=10,pady=(0,40))
contacttabLabel=customtkinter.CTkLabel(mainWindow,text="CONTACT",font=("Helvetica",24),fg_color="transparent")
contacttabLabel.grid(row=0,column=4,padx=10,pady=(0,40))
detailstabLabel=customtkinter.CTkLabel(mainWindow,text="DETAILS",font=("Helvetica",24),fg_color="transparent")
detailstabLabel.grid(row=0,column=5,padx=10,pady=(0,40))


welcomeLabel=customtkinter.CTkLabel(mainWindow,text="Welcome Afnaighar", font=("Sitka Banner Semibold",96,"bold"),text_color="white",fg_color="transparent")
welcomeLabel.grid(row=1,column=0, columnspan=6, sticky='nsew',padx=(80,0),pady=(250,0))

textLabel=customtkinter.CTkLabel(mainWindow,text="YOUR ROOM, YOUR STAY", font=("Helvetica",24),text_color="white",fg_color="transparent")
textLabel.grid(row=2,column=0, columnspan=6,)


      

mainWindow.mainloop()
