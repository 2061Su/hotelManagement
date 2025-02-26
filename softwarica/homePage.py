from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3
import ttkbootstrap as tb
from ttkbootstrap.icons import Icon

import testing
from adminlogin import adminLoginPage



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
              self.homeTab = customtkinter.CTkTabview(self, width=1450, height=1200,
                                   fg_color="#5c364b",
                                   segmented_button_fg_color="#5c364b",
                                   segmented_button_selected_color="#4a2c3c",
                                   segmented_button_selected_hover_color="#6b3b54",
                                   segmented_button_unselected_color="#6b3b54",
                                   segmented_button_unselected_hover_color="#70425a",
                                   anchor="e")
              self.homeTab.grid(row=0, column=0, padx=(0, 200))

              # Adding tabs
              home = self.homeTab.add("HOME")
              room = self.homeTab.add("ROOMS")
              about = self.homeTab.add("ABOUT US")
              contact = self.homeTab.add("CONTACT")
              history = self.homeTab.add("HISTORY")

              self.homeTab._segmented_button._buttons_dict["HISTORY"].bind("<Button-1>", self.on_history_tab_click)
              self.home_widgets(home)
              self.room_widgets(room)
              self.about_widgets(about)
              



              ######################home##################
              # Adding widgets to specific tabs in home

       def home_widgets(self,home):
              
              homeTitle = customtkinter.CTkLabel(home, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
              homeTitle.grid(row=0, column=0, padx=40, pady=40,)
              menu=["Log Out"]
              
             
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

                     result = messagebox.askquestion(title="Confirm Logout", message="Are you sure you want to log out?")
            
                     if result =="yes":
                            messagebox.showinfo(title="Successfully Logged Out", message="You have successfully logged out!")
                            self.schedule_transition_login()
              
       def schedule_transition_login(self):
              self.after(1000, self.transition_to_loginpage)  # Add a delay of 1000 milliseconds (1 second)

       def transition_to_loginpage(self):
              self.destroy()
              self.update()
              testing.App().mainloop()
                     
                     
       

              ################# rooms  ##############

       def room_widgets(self,room):
              homeTitle = customtkinter.CTkLabel(room, text="AfnaiGhar", font=("Comic Sans MS", 48, "bold"), text_color="white", fg_color="transparent")
              homeTitle.grid(row=0, column=0, padx=40, pady=40)

              bookingFrame=customtkinter.CTkScrollableFrame(room,
                                                        width=1400,
                                                        height=450,
                                                        label_text="AfnaiGhar",
                                                        label_font=("Comic Sans MS",38,"bold"),
                                                        label_fg_color="#704d0b",
                                                        fg_color="#604b70",
                                                        scrollbar_button_color="gray",
                                                        scrollbar_button_hover_color="gray")
              bookingFrame.grid(row=1,column=0,columnspan=70,padx=0,pady=(80,0))
              

              # Define the function to get room status
              def get_room_status(room_number):
                     conn = sqlite3.connect('hotel_management_user.db')
                     c = conn.cursor()
                     
                     # Fetch the status of the room from the database
                     c.execute("SELECT status FROM rooms WHERE room_number = ?", (room_number,))
                     status = c.fetchone()
                     
                     conn.close()
              
                     if status:
                            return status[0]  # return the status if found (Booked or Available)
                     return "Available"  # default to "Available" if no status found


              class RoomFrame:
                     def __init__(self,parent, room_number, room_type, price_per_night, image_path, row, column,status):
                            self.room_number = room_number
                            self.room_type = room_type
                            self.price_per_night = price_per_night
                            self.image_path = image_path
                            self.status = get_room_status(room_number)  # This keeps track of the current status

                            self.status_text_color = "#B7D5B5" if status == "Available" else "red"

                            # room 1  frame
                            self.frame=customtkinter.CTkFrame(parent,width=30,height=60,fg_color="white",border_color="#db7209",border_width=2)
                            self.frame.grid(row=row,column=column,padx=(100,20),pady=20)

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
                            self.label3=customtkinter.CTkLabel(self.frame,text=f"{status}",font=("Helvetica",13,),fg_color="transparent",text_color=self.status_text_color)
                            self.label3.grid(row=2,column=0,padx=(240,0),pady=5)
                            # 


                            self.roomP=customtkinter.CTkLabel(self.frame,text=f"Rs {price_per_night}",font=("Helvetica",14,"bold"),fg_color="transparent",text_color="#948E3C")
                            self.roomP.grid(row=4,column=0,padx=(200,0),pady=(0,30))
                            self.roomD=customtkinter.CTkLabel(self.frame,text="per night",font=("Helvetica",8,"bold"),fg_color="transparent",text_color="#948E3C")
                            self.roomD.grid(row=4,column=0,padx=(200,0),pady=(10,0))
                            self.bookNow1 = customtkinter.CTkButton(self.frame, text="BOOK NOW", font=("Helvetica", 18, "bold"), fg_color="#B7D5B5", text_color="white", corner_radius=10, width=60, height=30, command=lambda: self.book_now(room_number))
                            self.bookNow1.grid(row=4, column=0, padx=(0, 170), pady=(10, 30))
                           
                     def refresh_ui(self):
                            # Update the status of the room
                            self.status = get_room_status(self.room_number)
                            
                            # Update the status label text and color
                            new_status_text_color = "#B7D5B5" if self.status == "Available" else "red"
                            self.label3.configure(text=self.status, text_color=new_status_text_color)
                            
                            # Update the button based on the new status
                            if self.status == "Available":
                                   self.bookNow1.configure(text="BOOK NOW", fg_color="#B7D5B5", state="normal", command=lambda: self.book_now(self.room_number))
                            else:
                                   self.bookNow1.configure(text="BOOKED", fg_color="#FF4D4D", state="disabled", command=None)
                     def book_now(self, room_number):
                            from appointment import BookingWindow
                            app = BookingWindow(room_number, self.update_room_status, self.refresh_ui)
                            self.frame.wait_window(app)
                            self.update_room_status(room_number, "Booked")
                            self.update_status()

                     def update_room_status(self,room_number,status):
                                   conn = sqlite3.connect('hotel_management_user.db')
                                   c = conn.cursor()

                                   # Update the status of the room in the database
                                   c.execute("UPDATE rooms SET status = ? WHERE room_number = ?", (status, room_number))
                                   conn.commit()

                                   conn.close()

                     
        
                     def update_status(self):
                            self.bookNow1.configure(text="BOOKED", fg_color="#FF4D4D", state="disabled")

                            # Update the status label to "Booked" with red color
                            self.label3.configure(text="Booked", text_color="red")                    

              

              def place_room_frames(parent, rooms):
                     row = 0
                     column = 0
                     for room in rooms:
                            RoomFrame(parent, room["room_number"], room["type"], room["price"], room["image_path"], row, column,room["status"])
                            column += 1
                            if column == 3:  # Move to the next row after 2 columns
                                   column = 0
                                   row += 1


              rooms = [
                     {"room_number": 1, "type": "Double Room", "price": 17000, "image_path": "softwarica\\photo\\hotel.png","status":"Available"},
                     {"room_number": 2, "type": "Single Room", "price": 10000, "image_path": "softwarica\\photo\\hotel1.png","status":"Available"},
                     {"room_number": 3, "type": "Suite Room", "price": 25000, "image_path": "softwarica\\photo\\hotel2.png","status":"Available"},
                     {"room_number": 4, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel3.png","status":"Available"},
                     {"room_number": 5, "type": "Double Room", "price": 17000, "image_path": "softwarica\\photo\\hotel4.png","status":"Available"},
                     {"room_number": 6, "type": "Single Room", "price": 10000, "image_path": "softwarica\\photo\\hotel5.png","status":"Available"},
                     {"room_number": 7, "type": "Suite Room", "price": 25000, "image_path": "softwarica\\photo\\hotel5.png","status":"Available"},
                     {"room_number": 8, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel7.png","status":"Available"},
                     {"room_number": 9, "type": "Double Room", "price": 17000, "image_path": "softwarica\\photo\\hotel8.png","status":"Available"},
                     {"room_number": 10, "type": "Single Room", "price": 10000, "image_path": "softwarica\\photo\\hotel9.png","status":"Available"},
                     {"room_number": 11, "type": "Suite Room", "price": 25000, "image_path": "softwarica\\photo\\hotel11.png","status":"Available"},
                     {"room_number": 12, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel3.png","status":"Available"},
                     {"room_number": 13, "type": "Double Room", "price": 17000, "image_path": "softwarica\\photo\\hotel8.png","status":"Available"},
                     {"room_number": 14, "type": "Single Room", "price": 10000, "image_path": "softwarica\\photo\\hotel12.png","status":"Available"},
                     {"room_number": 15, "type": "Suite Room", "price": 25000, "image_path": "softwarica\\photo\\hotel5.png","status":"Available"},
                     {"room_number": 16, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel3.png","status":"Available"},
                     {"room_number": 17, "type": "Single Room", "price": 10000, "image_path": "softwarica\\photo\\hotel12.png","status":"Available"},
                     {"room_number": 18, "type": "Suite Room", "price": 25000, "image_path": "softwarica\\photo\\hotel7.png","status":"Available"},
                     {"room_number": 19, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel.png","status":"Available"},
                     {"room_number": 20, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel3.png","status":"Available"},
                     {"room_number": 21, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\photo\\hotel5.png","status":"Available"},
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

       
              
       def on_history_tab_click(self, event):
              """ Authenticate admin before showing the History tab """
              adminLoginPage(self.show_history_tab)

       def show_history_tab(self):
              """ Show History widgets after successful login """
              self.history_widgets(self.homeTab.tab("HISTORY"))
       def history_widgets(self, history):

              class History:
                     def __init__(self, parent):
                            self.parent = parent
                            self.scrollable_frame = customtkinter.CTkScrollableFrame(self.parent, corner_radius=10, fg_color="white", width=1000,height=600)
                            self.scrollable_frame.grid(row=0, column=0, padx=20, pady=20)

                     def load_booking_history(self):
                           
                            for widget in self.scrollable_frame.winfo_children():
                                   widget.destroy()

                            conn = sqlite3.connect('hotel_management_user.db')
                            c = conn.cursor()
                            c.execute("""SELECT id, room_number, first_name, last_name, checkin_date, checkout_date
                                          FROM bookings""")
                            result = c.fetchall()
                            conn.close()

                            for record in result:
                                   booking_id, room_number, first_name, last_name, checkin_date, checkout_date = record
                                   record_frame = customtkinter.CTkFrame(self.scrollable_frame, corner_radius=10, fg_color="#D9D9D9")
                                   record_frame.pack(padx=10, pady=5, fill='x')

                                   uniqueId = customtkinter.CTkLabel(record_frame, text=f"Id: {booking_id}", font=("Helvetica", 20), text_color="black")
                                   uniqueId.grid(row=0, column=0, padx=(10, 0), pady=10)

                                   name = customtkinter.CTkLabel(record_frame, text=f"{first_name} {last_name}", font=("Helvetica", 20), text_color="black")
                                   name.grid(row=0, column=1, padx=30, pady=10)

                                   checkIn = customtkinter.CTkLabel(record_frame, text="Check-in-date:", font=("Helvetica", 20), text_color="black")
                                   checkIn.grid(row=0, column=2, pady=10)
                                   checkInD = customtkinter.CTkLabel(record_frame, text=checkin_date, font=("Helvetica", 20), text_color="black")
                                   checkInD.grid(row=0, column=3, pady=10, padx=(0, 30))

                                   checkOut = customtkinter.CTkLabel(record_frame, text="Check-out-date:", font=("Helvetica", 20), text_color="black")
                                   checkOut.grid(row=1, column=2, pady=10)
                                   checkOutD = customtkinter.CTkLabel(record_frame, text=checkout_date, font=("Helvetica", 20), text_color="black")
                                   checkOutD.grid(row=1, column=3, pady=10, padx=(0, 30))

                                   room = customtkinter.CTkLabel(record_frame, text="Room no:", font=("Helvetica", 20), text_color="black")
                                   room.grid(row=1, column=0, padx=(30, 0), pady=10)
                                   roomN = customtkinter.CTkLabel(record_frame, text=room_number, font=("Helvetica", 20), text_color="black")
                                   roomN.grid(row=1, column=1, padx=(0, 10), pady=10)

                                   book = customtkinter.CTkLabel(record_frame, text="Date booked:", font=("Helvetica", 20), text_color="black")
                                   book.grid(row=2, column=0, padx=(10, 0), pady=10)
                                   bookDate = customtkinter.CTkLabel(record_frame, text="00/00/00", font=("Helvetica", 20), text_color="black")
                                   bookDate.grid(row=2, column=1, pady=10)

                                   scheduledD = customtkinter.CTkLabel(record_frame, text="Booked", font=("Helvetica", 12), text_color="#218200")
                                   scheduledD.grid(row=2, column=3)

                                   update = customtkinter.CTkButton(record_frame, text="Update", font=("Helvetica", 12), text_color="white", width=40, fg_color="#1CCB0C",command=lambda bid=booking_id, room=room_number: self.open_booking_window(bid,room))
                                   update.grid(row=2, column=2, padx=(40, 0))

                                   delete_button = customtkinter.CTkButton(record_frame, text="Delete", font=("Helvetica", 12), text_color="white", width=40, fg_color="red",command=lambda room_number=room_number: self.delete_booking(room_number))
                                   delete_button.grid(row=1, column=4, padx=(40, 0))
                     def delete_booking(self,room_number):
                            try:
                                   conn = sqlite3.connect('hotel_management_user.db')
                                   c = conn.cursor()
                                   
                                   # Check if the bookings table exists
                                   c.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='bookings'")
                                   if not c.fetchone():
                                          raise sqlite3.OperationalError("The 'bookings' table does not exist.")

                                   # Execute the DELETE statement
                                   c.execute('DELETE FROM bookings WHERE room_number = ?', (room_number,))

                                   c.execute("UPDATE rooms SET status = ? WHERE room_number = ?", ('Available', room_number))
                                   conn.commit()

                                   self.load_booking_history()
                                   
                                   messagebox.showinfo(title="Success", message="Booking deleted successfully.")
                            except sqlite3.Error as e:
                                   messagebox.showerror(title="Error", message=f"An error occurred: {e}")
                            finally:
                                   conn.close()

                     def update_room_status(self, room_number, status):
                            # Code to update the room status in the database
                            conn = sqlite3.connect('hotel_management_user.db')
                            c = conn.cursor()
                            c.execute("UPDATE rooms SET status = ? WHERE room_number = ?", (status, room_number))
                            conn.commit()
                            conn.close()
                     def open_booking_window(self, booking_id,room_number):
                            from appointment import BookingWindow
                            booking_window = BookingWindow(booking_id=booking_id, 
                                                           room_number=room_number,
                                                           update_room_status=self.update_room_status,
                                                           refresh_callback=self.load_booking_history )
                            booking_window.grab_set()

                     def update_booking(self, booking_id):
                            # This method can be used to update the booking info if necessary
                            app = BookingWindow(booking_id)
                            app.mainloop()

                     # Create an instance of the History class and load booking history
              history_instance = History(history)
              history_instance.load_booking_history()


if __name__ == "__main__":
       HomePage()
       