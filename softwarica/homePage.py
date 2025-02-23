from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon
from appointment import BookingWindow
import testing



# customtkinter.set_appearance_mode("dark")
# customtkinter.set_default_color_theme("dark-blue")


class HomePage(customtkinter.CTk):
       def __init__(self):
              super().__init__()
              self.title("Afnaighar")
              self.geometry("1200x700")
              self.mainPage()
              self.mainloop()
       def mainPage(self):
              homeTab = customtkinter.CTkTabview(self, width=1450, height=1200,
                                   fg_color="#5c364b",
                                   segmented_button_fg_color="#5c364b",
                                   segmented_button_selected_color="#4a2c3c",
                                   segmented_button_selected_hover_color="#6b3b54",
                                   segmented_button_unselected_color="#6b3b54",
                                   segmented_button_unselected_hover_color="#70425a",
                                   anchor="e")
              homeTab.grid(row=0, column=0, padx=(0, 200))

              # Adding tabs
              home = homeTab.add("HOME")
              room = homeTab.add("ROOMS")
              about = homeTab.add("ABOUT US")
              contact = homeTab.add("CONTACT")
              history = homeTab.add("HISTORY")
                     
              self.home_widgets(home)
              self.room_widgets(room)
              self.about_widgets(about)
              self.history_widgets(history)


              ######################home##################
              # Adding widgets to specific tabs in home

       def home_widgets(self,home):
              homeTitle = customtkinter.CTkLabel(home, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
              homeTitle.grid(row=0, column=0, padx=40, pady=40,)
              menu=["Log Out","Admin"]
              
             
              my_option=customtkinter.CTkComboBox(home,
                                                  values=menu,
                                                  width=90,
                                                  fg_color="#4a2c3c",
                                                  corner_radius=10,
                                                  button_color="#36212c",
                                                  button_hover_color="#6b3b54",
                                                  dropdown_hover_color="#6b3b54",
                                                  command=self.nav)
              my_option.set("Option")
              my_option.grid(row=0,column=0,columnspan=50,padx=(1320,0),pady=(0,120))



              welcomeLabel = customtkinter.CTkLabel(home, text="Welcome Afnaighar", font=("Sitka Banner Semibold", 96, "bold"), text_color="white", fg_color="transparent")
              welcomeLabel.grid(row=1, column=1, sticky='nsew', padx=(80, 0), pady=(150, 0))

              textLabel = customtkinter.CTkLabel(home, text="YOUR ROOM, YOUR STAY", font=("Helvetica", 24), text_color="white", fg_color="transparent")
              textLabel.grid(row=2, column=0, columnspan=6,padx=(350,0))
              

       def nav(self,selection):
              if selection == "Log Out":
                     messagebox.showinfo(title="Successfully Logged Out", message="You have successfully logged out!")
                     self.schedule_transition_login()

       def schedule_transition_login(self):
              self.after(1000, self.transition_to_loginpage)  # Add a delay of 1000 milliseconds (1 second)

       def transition_to_loginpage(self):
              self.destroy()
              testing.App().mainloop()
                     
                     
       

              ################# rooms  ##############

       def room_widgets(self,room):
              homeTitle = customtkinter.CTkLabel(room, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
              homeTitle.grid(row=0, column=0, padx=40, pady=40)

              bookingFrame=customtkinter.CTkScrollableFrame(room,
                                                        width=900,
                                                        height=450,
                                                        label_text="AfnaiGhar",
                                                        label_font=("Comic Sans MS",38,"bold"),
                                                        label_fg_color="#704d0b",
                                                        fg_color="#604b70",
                                                        scrollbar_button_color="gray",
                                                        scrollbar_button_hover_color="gray")
              bookingFrame.grid(row=1,column=1,columnspan=6,padx=(0,20),pady=(80,0))
              

              class RoomFrame:
                     def __init__(self,parent, room_number, room_type, price_per_night, image_path, row, column):

                            # room 1  frame
                            self.frame=customtkinter.CTkFrame(parent,width=30,height=60,fg_color="white",border_color="#db7209",border_width=2)
                            self.frame.grid(row=row,column=column,padx=(70,20),pady=20)

                            self.room_image = customtkinter.CTkImage(light_image=Image.open(image_path), dark_image=Image.open(image_path), size=(300, 200))
                            self.photo = customtkinter.CTkLabel(self.frame,text="", image=self.room_image)
                            self.photo.grid(row=0, column=0, padx=10,pady=10 )
                            self.photo.image = self.room_image


                            # 
                            self.label=customtkinter.CTkLabel(self.frame,text="Afnaighar",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#788B8B")
                            self.label.grid(row=1,column=0,padx=(0,225))
                            self.label1=customtkinter.CTkLabel(self.frame,text=f"Room no.{room_number}",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#788B8B")
                            self.label1.grid(row=2,column=0,padx=(0,220))
                            
                            self.label2=customtkinter.CTkLabel(self.frame,text=f"{room_type}",font=("Helvetica",15,"bold"),fg_color="transparent",text_color="#948E3C")
                            self.label2.grid(row=3,column=0,padx=(0,200),pady=5)
                            self.label3=customtkinter.CTkLabel(self.frame,text=f"Available",font=("Helvetica",13,),fg_color="transparent",text_color="#B7D5B5")
                            self.label3.grid(row=2,column=0,padx=(240,0),pady=5)
                            # 


                            self.roomP=customtkinter.CTkLabel(self.frame,text=f"Rs {price_per_night}",font=("Helvetica",14,"bold"),fg_color="transparent",text_color="#948E3C")
                            self.roomP.grid(row=4,column=0,padx=(200,0),pady=(0,30))
                            self.roomD=customtkinter.CTkLabel(self.frame,text="per night",font=("Helvetica",8,"bold"),fg_color="transparent",text_color="#948E3C")
                            self.roomD.grid(row=4,column=0,padx=(200,0),pady=(10,0))
                            self.bookNow1=customtkinter.CTkButton(self.frame,
                                                        text="BOOK NOW",
                                                        font=("Helvetica",18,"bold"),
                                                        fg_color="#B7D5B5",
                                                        text_color="white",
                                                        corner_radius=10,
                                                        width=60,
                                                        height=30,
                                                        command=self.book_now)
                            self.bookNow1.grid(row=4,column=0,padx=(0,170),pady=(10,30))

                     def book_now(self):
                            app = BookingWindow()
              def place_room_frames(parent, rooms):
                     row = 0
                     column = 0
                     for room in rooms:
                            RoomFrame(parent, room["number"], room["type"], room["price"], room["image_path"], row, column)
                            column += 1
                            if column == 2:  # Move to the next row after 2 columns
                                   column = 0
                                   row += 1


              rooms = [
                     {"number": 1, "type": "Double Room", "price": 17000, "image_path": "softwarica\\photo\\hotel8.png"},
                     {"number": 2, "type": "Single Room", "price": 10000, "image_path": "softwarica\\photo\\hotel12.png"},
                     {"number": 3, "type": "Suite Room", "price": 25000, "image_path": "softwarica\\photo\\hotel5.png"},
                     {"number": 4, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel3.png"}
              ]

              # Place the room frames in the scrollable frame
              place_room_frames(bookingFrame, rooms)

              







              #################### about us #########################

       def about_widgets(self,about):

              homeTitle = customtkinter.CTkLabel(about, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
              homeTitle.grid(row=0, column=0, padx=40, pady=40)

              aboutLabel = customtkinter.CTkLabel(about, text="About Us", font=("Sitka Banner Semibold", 96, "bold"), text_color="white", fg_color="transparent")
              aboutLabel.grid(row=1, column=1,padx=(250,0))

              successLabel = customtkinter.CTkLabel(about, text="Behind The Success", font=("Sitka Banner Semibold", 34, "bold"), text_color="#f7a305", fg_color="transparent")
              successLabel.grid(row=2, column=1,padx=(250,0) )

              success=customtkinter.CTkLabel(about, 
                                          text="""                                                                 Our hotel stands out with exceptional customer service, 
                                                                                    luxurious yet affordable accommodations, and a prime location that 
                                                                             ensures convenience for guests. We prioritize guest satisfaction 
                                                                                           with personalized experiences and top-tier amenities. Our commitment 
                                                                                                  to excellence and innovation makes us the preferred choice over other hotels.""", 
                                          font=("Helvetica", 18),
                                          text_color="#b0883a", 
                                          fg_color="transparent",
                                          anchor="w")
              success.grid(row=3, column=0,columnspan=20 ,pady=50)
              photoLabel= customtkinter.CTkLabel(about,text="",corner_radius=50)
              photoLabel.grid(row=4, column=1, )



       ########################history####################




       def history_widgets(self,history):
              homeTitle = customtkinter.CTkLabel(history, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
              homeTitle.grid(row=0, column=0, padx=40, pady=40)

              #history scrollableframe
              historyFrame=customtkinter.CTkScrollableFrame(history,corner_radius=10,fg_color="white",width=600)
              historyFrame.grid(row=1,column=1,padx=(100,0),pady=(100,0))

              
              

              # history Frame
              class History:
                     def __init__(self,parent):
                            # title
                            self.historyLabel=customtkinter.CTkLabel(parent,
                                                               text="Your booked history",
                                                               font=("Helvetica",20,"bold"),
                                                               text_color="black",
                                                               corner_radius=10,)
                            self.historyLabel.grid(row=0,column=0,padx=10,pady=10)
                            self.bookhistory=customtkinter.CTkFrame(parent,
                                                               corner_radius=10,
                                                               fg_color="#D9D9D9",)
                            self.bookhistory.grid(row=1,column=0)
                            

                            # id
                            self.uniqueId=customtkinter.CTkLabel(self.bookhistory,
                                                        text="Id : ",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.uniqueId.grid(row=0,column=0,padx=(10,0),pady=10)
                            self.uniqueId=customtkinter.CTkLabel(self.bookhistory,
                                                        text="00",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.uniqueId.grid(row=0,column=1)

                            # name
                            self.name=customtkinter.CTkLabel(self.bookhistory,
                                                        text="sumit",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.name.grid(row=0,column=2,padx=30,pady=10)


                            #check-in-date
                            self.checkIn=customtkinter.CTkLabel(self.bookhistory,
                                                        text="check-in-date :",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.checkIn.grid(row=0,column=4,pady=10)
                            self.checkInD=customtkinter.CTkLabel(self.bookhistory,
                                                        text="00/00/00",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.checkInD.grid(row=0,column=5,pady=10,padx=(0,30))
                            # Date book
                            self.book=customtkinter.CTkLabel(self.bookhistory,
                                                        text="Date book:",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.book.grid(row=1,column=0,padx=(10,0),pady=10)

                            self.bookDate=customtkinter.CTkLabel(self.bookhistory,
                                                        text="00/00/00",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.bookDate.grid(row=1,column=1,pady=10)

                            # room no
                            self.room=customtkinter.CTkLabel(self.bookhistory,
                                                        text="room no :",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.room.grid(row=1,column=2,padx=(30,0),pady=10)
                            self.roomN=customtkinter.CTkLabel(self.bookhistory,
                                                        text=" 00 ",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.roomN.grid(row=1,column=3,padx=(0,10),pady=10)


                            # check-out-date
                            self.checkOut=customtkinter.CTkLabel(self.bookhistory,
                                                        text="check-out-date : ",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.checkOut.grid(row=1,column=4,pady=10)
                            self.checkOutD=customtkinter.CTkLabel(self.bookhistory,
                                                        text="00/00/00",
                                                        font=("Helvetica",20),
                                                        text_color="black",)
                            self.checkOutD.grid(row=1,column=5,pady=10,padx=(0,30))
                            
                            #status
                            self.scheduledD=customtkinter.CTkLabel(self.bookhistory,
                                                        text="Booked",
                                                        font=("Helvetica",12),
                                                        text_color="#218200",)
                            self.scheduledD.grid(row=2,column=5,)

                     

                            self.update=customtkinter.CTkButton(self.bookhistory,
                                                        text="update",
                                                        font=("Helvetica",12),
                                                        text_color="white",
                                                        width=40,
                                                        fg_color="#1CCB0C",
                                                        command=self.update
                                                        )
                            self.update.grid(row=2,column=4,padx=(40,0))

                     def update():
                            app=BookingWindow()



if __name__ == "__main__":
       HomePage()
       