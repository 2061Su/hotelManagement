from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import Image, ImageTk
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

mainWindow = customtkinter.CTk()
mainWindow.title("Afnaighar ")
mainWindow.geometry("1200x700")

# Scrollable frame
bookingFrame = customtkinter.CTkScrollableFrame(mainWindow,
                                                width=1000,
                                                height=600,
                                                label_text="AfnaiGhar",
                                                label_font=("Comic Sans MS", 38, "bold"),
                                                scrollbar_button_color="gray",
                                                scrollbar_button_hover_color="#5C5C5C")
bookingFrame.grid(row=1, column=1, columnspan=6, padx=(0, 20), pady=(80, 0))

class RoomFrame:
    def __init__(self, parent, room_number, room_type, price_per_night, image_path, row, column):
        self.frame = customtkinter.CTkFrame(parent, width=30, height=60, fg_color="white")
        self.frame.grid(row=row, column=column, padx=(70, 20), pady=20)

        self.room_image = customtkinter.CTkImage(light_image=Image.open(image_path),
                                                 dark_image=Image.open(image_path), size=(300, 200))
        self.photo = customtkinter.CTkLabel(self.frame, image=self.room_image)
        self.photo.grid(row=0, column=0, padx=10, pady=10)
        self.photo.image = self.room_image

        self.label = customtkinter.CTkLabel(self.frame, text="Afnaighar", font=("Helvetica", 15, "bold"), fg_color="transparent", text_color="#788B8B")
        self.label.grid(row=1, column=0, padx=(0, 225))
        self.label1 = customtkinter.CTkLabel(self.frame, text=f"Room no.{room_number}", font=("Helvetica", 15, "bold"), fg_color="transparent", text_color="#788B8B")
        self.label1.grid(row=2, column=0, padx=(0, 220))
        self.label2 = customtkinter.CTkLabel(self.frame, text=room_type, font=("Helvetica", 15, "bold"), fg_color="transparent", text_color="#948E3C")
        self.label2.grid(row=3, column=0, padx=(0, 200), pady=5)

        self.roomP = customtkinter.CTkLabel(self.frame, text=f"Rs {price_per_night}", font=("Helvetica", 14, "bold"), fg_color="transparent", text_color="#948E3C")
        self.roomP.grid(row=4, column=0, padx=(200, 0), pady=(0, 30))
        self.roomD = customtkinter.CTkLabel(self.frame, text="per night", font=("Helvetica", 8, "bold"), fg_color="transparent", text_color="#948E3C")
        self.roomD.grid(row=4, column=0, padx=(200, 0), pady=(10, 0))

        self.bookNow = customtkinter.CTkButton(self.frame, text="BOOK NOW", font=("Helvetica", 18, "bold"), fg_color="#B7D5B5", text_color="white", corner_radius=10, width=60, height=30,command=self.book_now)
        self.bookNow.grid(row=4, column=0, padx=(0, 170), pady=(10, 30))

    def book_now(self):
      messagebox.showinfo("Booking", f"Room booked successfully!")

# Function to place frames in a grid with 2 columns
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
    {"number": 1, "type": "Double Room", "price": 17000, "image_path": "softwarica\\hotel11.png"},
    {"number": 2, "type": "Single Room", "price": 10000, "image_path": "softwarica\\hotel11.png"},
    {"number": 3, "type": "Suite Room", "price": 25000, "image_path": "softwarica\\hotel11.png"},
    {"number": 4, "type": "Deluxe Room", "price": 20000, "image_path": "softwarica\\hotel11.png"}
]

# Place the room frames in the scrollable frame
place_room_frames(bookingFrame, rooms)

mainWindow.mainloop()
