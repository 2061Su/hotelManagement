from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon
from appointment import BookingWindow



# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")


class HomePage:
       def __init__(self):
              self.mainPage()
       def mainPage(self):
              
              mainWindow = customtkinter.CTk()
              mainWindow.title("Afnaighar")
              mainWindow.geometry("1200x700")



              homeTab = customtkinter.CTkTabview(mainWindow, 
                                                 width=1450, 
                                                 height=1200,
                                          #  segmented_button_fg_color="gray",
                                                 segmented_button_selected_color="#7e8282",
                                                 segmented_button_selected_hover_color="#626363",
                                                 anchor="e")
              homeTab.grid(row=0, column=0,padx=(0,200))



              # Adding tabs

              home=homeTab.add("HOME")
              room=homeTab.add("ROOMS")
              about=homeTab.add("ABOUT US")
              contact=homeTab.add("CONTACT")
              history=homeTab.add("HISTORY")


              ######################home##################
              # Adding widgets to specific tabs in home

              def home_widgets():
                     homeTitle = customtkinter.CTkLabel(home, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
                     homeTitle.grid(row=0, column=0, padx=40, pady=40,)
                     

                     def nav():
                            pass
                            
                     menu=["Log Out","Admin"]

                     my_option=customtkinter.CTkComboBox(home,values=menu,width=90,command=nav)
                     my_option.grid(row=0,column=0,columnspan=50,padx=(1320,0),pady=(0,120))



                     welcomeLabel = customtkinter.CTkLabel(home, text="Welcome Afnaighar", font=("Sitka Banner Semibold", 96, "bold"), text_color="white", fg_color="transparent")
                     welcomeLabel.grid(row=1, column=1, sticky='nsew', padx=(80, 0), pady=(150, 0))

                     textLabel = customtkinter.CTkLabel(home, text="YOUR ROOM, YOUR STAY", font=("Helvetica", 24), text_color="white", fg_color="transparent")
                     textLabel.grid(row=2, column=0, columnspan=6,padx=(350,0))

              ################# rooms  ##############

              def room_widgets():
                     homeTitle = customtkinter.CTkLabel(room, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
                     homeTitle.grid(row=0, column=0, padx=40, pady=40)

                     bookingFrame=customtkinter.CTkScrollableFrame(room,
                                                               width=800,
                                                               height=600,
                                                               label_text="AfnaiGhar",
                                                               label_font=("Comic Sans MS",38,"bold"),
                                                               scrollbar_button_color="gray",
                                                               scrollbar_button_hover_color="#5C5C5C")
                     bookingFrame.grid(row=1,column=1,columnspan=6,padx=(50,0),pady=(80,0))

                     # room 1  frame
                     room1Frame=customtkinter.CTkFrame(bookingFrame,width=30,height=60,fg_color="white")
                     room1Frame.grid(row=0,column=0,padx=(70,20),pady=20)

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



                     def bookNow():
                            app = BookingWindow()
                     
                     bookNow1=customtkinter.CTkButton(room1Frame,
                                                 text="BOOK NOW",
                                                 font=("Helvetica",18,"bold"),
                                                 fg_color="#B7D5B5",
                                                 text_color="white",
                                                 corner_radius=10,
                                                 width=60,
                                                 height=30,
                                                 
                                                 command=bookNow)
                     bookNow1.grid(row=4,column=0,padx=(0,170),pady=(10,30))








              #################### about us #########################

              def about_widgets():

                     homeTitle = customtkinter.CTkLabel(about, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
                     homeTitle.grid(row=0, column=0, padx=40, pady=40)

                     aboutLabel = customtkinter.CTkLabel(about, text="About Us", font=("Sitka Banner Semibold", 96, "bold"), text_color="white", fg_color="transparent")
                     aboutLabel.grid(row=1, column=1,padx=(250,0))

                     successFrame = customtkinter.CTkFrame(about)
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


              ########################history####################




              def history_widgets():
                     homeTitle = customtkinter.CTkLabel(history, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
                     homeTitle.grid(row=0, column=0, padx=40, pady=40)

                     #history scrollableframe
                     historyFrame=customtkinter.CTkScrollableFrame(history,corner_radius=10,fg_color="white",width=600)
                     historyFrame.grid(row=1,column=1,padx=(100,0),pady=(100,0))

                     # title
                     historyLabel=customtkinter.CTkLabel(historyFrame,
                                                        text="Your booked history",
                                                        font=("Helvetica",20,"bold"),
                                                        text_color="black",
                                                        corner_radius=10,)
                     historyLabel.grid(row=0,column=0,padx=10,pady=10)
                     

                     # history Frame
                     bookhistory=customtkinter.CTkFrame(historyFrame,
                                                        corner_radius=10,
                                                        fg_color="#D9D9D9",)
                     bookhistory.grid(row=1,column=0)
                     

                     # id
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

                     # name
                     name=customtkinter.CTkLabel(bookhistory,
                                                 text="sumit",
                                                 font=("Helvetica",20),
                                                 text_color="black",)
                     name.grid(row=0,column=2,padx=30,pady=10)


                     #check-in-date
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
                     # Date book
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

                     # room no
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


                     # check-out-date
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
                     
                     #status
                     scheduledD=customtkinter.CTkLabel(bookhistory,
                                                 text="Booked",
                                                 font=("Helvetica",12),
                                                 text_color="#218200",)
                     scheduledD.grid(row=2,column=5,)

                     def update():
                            app=BookingWindow()

                     update=customtkinter.CTkButton(bookhistory,
                                                 text="update",
                                                 font=("Helvetica",12),
                                                 text_color="white",
                                                 width=40,
                                                 fg_color="#1CCB0C",
                                                 command=update
                                                 )
                     update.grid(row=2,column=4,padx=(40,0))



              if __name__ == "__main__":
                     
                     home_widgets()
                     room_widgets()
                     about_widgets()
                     history_widgets()
                     mainWindow.mainloop()