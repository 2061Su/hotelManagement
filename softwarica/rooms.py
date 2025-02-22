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


#  scrollabel frame

bookingFrame=customtkinter.CTkScrollableFrame(mainWindow,
                                              width=800,
                                              height=600,
                                              label_text="AfnaiGhar",
                                              label_font=("Comic Sans MS",38,"bold"),
                                              scrollbar_button_color="gray",
                                              scrollbar_button_hover_color="#5C5C5C")
bookingFrame.grid(row=1,column=0,columnspan=6,padx=(100,0),pady=(100,0))

# room 1  frame
room1Frame=customtkinter.CTkFrame(bookingFrame,width=30,height=60,fg_color="white")
room1Frame.grid(row=0,column=0,padx=(70,20),pady=20)

# 
room1_image = customtkinter.CTkImage(light_image=Image.open("softwarica\\background.png"), dark_image=Image.open("softwarica\\background.png"), size=(300, 200))
photo = customtkinter.CTkLabel(room1Frame, image=room1_image)
photo.grid(row=0, column=0, padx=10,pady=10 )
photo.image = room1_image


# 
label=customtkinter.CTkLabel(room1Frame,text="Afnaighar",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#788B8B")
label.grid(row=1,column=0,padx=(0,225))
label1=customtkinter.CTkLabel(room1Frame,text="Room no.1",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#788B8B")
label1.grid(row=2,column=0,padx=(0,220))
label2=customtkinter.CTkLabel(room1Frame,text="Double Room",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#948E3C")
label2.grid(row=3,column=0,padx=(0,200),pady=5)
# 


roomP=customtkinter.CTkLabel(room1Frame,text="Rs 17,000",font=("Helvetica",14,"bold"),fg_color="transparent",text_color="#948E3C")
roomP.grid(row=4,column=0,padx=(200,0),pady=(0,30))
roomD=customtkinter.CTkLabel(room1Frame,text="per night",font=("Helvetica",8,"bold"),fg_color="transparent",text_color="#948E3C")
roomD.grid(row=4,column=0,padx=(200,0),pady=(10,0))


bookNow1=customtkinter.CTkButton(room1Frame,text="BOOK NOW",font=("Helvetica",18,"bold"),fg_color="#B7D5B5",text_color="white",corner_radius=10,width=60,height=30)
bookNow1.grid(row=4,column=0,padx=(0,170),pady=(10,30))


# room 2 frame
room2Frame=customtkinter.CTkFrame(bookingFrame,width=40,height=100,fg_color="white")
room2Frame.grid(row=0,column=1,padx=40,pady=20)

room2_image = customtkinter.CTkImage(light_image=Image.open("softwarica\\background.png"), dark_image=Image.open("softwarica\\background.png"), size=(300, 200))
photo2 = customtkinter.CTkLabel(room2Frame, image=room1_image)
photo2.grid(row=0, column=0,padx=10,pady=10 )
photo2.image = room2_image

label3=customtkinter.CTkLabel(room2Frame,text="Afnaighar",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#788B8B")
label3.grid(row=1,column=0,padx=(0,225))
label4=customtkinter.CTkLabel(room2Frame,text="Room no.2",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#788B8B")
label4.grid(row=2,column=0,padx=(0,220))
label5=customtkinter.CTkLabel(room2Frame,text="Double Room",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#948E3C")
label5.grid(row=3,column=0,padx=(0,200),pady=5)

roomP=customtkinter.CTkLabel(room2Frame,text="Rs 17,000",font=("Helvetica",14,"bold"),fg_color="transparent",text_color="#948E3C")
roomP.grid(row=4,column=0,padx=(200,0),pady=(0,30))
roomD=customtkinter.CTkLabel(room2Frame,text="per night",font=("Helvetica",8,"bold"),fg_color="transparent",text_color="#948E3C")
roomD.grid(row=4,column=0,padx=(200,0),pady=(10,0))


bookNow2=customtkinter.CTkButton(room2Frame,text="BOOK NOW",font=("Helvetica",18,"bold"),fg_color="#B7D5B5",text_color="white",corner_radius=10,width=60,height=30)
bookNow2.grid(row=4,column=0,padx=(0,170),pady=(10,30))


      

mainWindow.mainloop()
