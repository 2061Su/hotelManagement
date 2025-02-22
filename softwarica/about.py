from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk,ImageDraw
import sqlite3




customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

aboutWindow = customtkinter.CTk()
aboutWindow.title("Afnaighar ")
aboutWindow.geometry("1200x700")

homeTitle = customtkinter.CTkLabel(aboutWindow, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
homeTitle.grid(row=0, column=0, padx=40, pady=40)

hometabLabel = customtkinter.CTkLabel(aboutWindow, text="HOME", font=("Helvetica", 24), fg_color="transparent")
hometabLabel.grid(row=0, column=1, padx=(480, 10), pady=(0, 40))
roomtabLabel = customtkinter.CTkLabel(aboutWindow, text="ROOMS", font=("Helvetica", 24), fg_color="transparent")
roomtabLabel.grid(row=0, column=2, padx=10, pady=(0, 40))
abouttabLabel = customtkinter.CTkLabel(aboutWindow, text="ABOUT US", font=("Helvetica", 24), fg_color="transparent")
abouttabLabel.grid(row=0, column=3, padx=10, pady=(0, 40))
contacttabLabel = customtkinter.CTkLabel(aboutWindow, text="CONTACT", font=("Helvetica", 24), fg_color="transparent")
contacttabLabel.grid(row=0, column=4, padx=10, pady=(0, 40))
detailstabLabel = customtkinter.CTkLabel(aboutWindow, text="DETAILS", font=("Helvetica", 24), fg_color="transparent")
detailstabLabel.grid(row=0, column=5, padx=10, pady=(0, 40))

aboutLabel = customtkinter.CTkLabel(aboutWindow, text="About Us", font=("Sitka Banner Semibold", 96, "bold"), text_color="white", fg_color="transparent")
aboutLabel.grid(row=1, column=0, columnspan=6, sticky='nsew', padx=(130, 0))

successFrame = customtkinter.CTkFrame(aboutWindow)
successFrame.grid(row=2, column=0,columnspan=6)

successLabel = customtkinter.CTkLabel(successFrame, text="Behind The Success", font=("Sitka Banner Semibold", 64, "bold"), text_color="#5C5C5C", fg_color="transparent")
successLabel.grid(row=0, column=0, padx=(160, 0), pady=(100, 0))

success=customtkinter.CTkLabel(successFrame, 
                               text="""     Our hotel stands out with exceptional customer service, 
                        luxurious yet affordable accommodations, and a prime location that 
                  ensures convenience for guests. We prioritize guest satisfaction 
                            with personalized experiences and top-tier amenities. Our commitment 
                                      to excellence and innovation makes us the preferred choice over other hotels.""", 
                               font=("Helvetica", 18),
                               text_color="#6B6B6B", 
                               fg_color="transparent",
                               anchor="w")
success.grid(row=1, column=0, )


# success_image = customtkinter.CTkImage(light_image=Image.open("background.png"), dark_image=Image.open("background.png"), size=(300, 200))
# photo = customtkinter.CTkLabel(successFrame, image=success_image)
# photo.grid(row=1, column=1, padx=10,pady=10 )
# photo.image = success_image

aboutWindow.mainloop()
