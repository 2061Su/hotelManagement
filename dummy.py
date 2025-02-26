from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk, Image
from signUp import signup
from forgetPassword import fpassword
import sqlite3

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x800")
        self.title("Hotel Management System")

        self.hotelName = customtkinter.CTkLabel(self, text="AfnaiGhar", font=("Comic Sans MS", 64, "bold"), text_color="white")
        self.hotelName.grid(row=0, column=0, padx=100, pady=50)

        self.loginFrame = customtkinter.CTkFrame(self, corner_radius=10)
        self.loginFrame.grid(row=1, column=0, padx=500)

        # login frame elements
        self.userLabel = customtkinter.CTkLabel(self.loginFrame, text="Username")
        self.userLabel.grid(row=0, column=0, padx=(50, 10), pady=(60, 20))

        self.userEntry = customtkinter.CTkEntry(self.loginFrame, placeholder_text="Enter your username", width=200, height=30)
        self.userEntry.grid(row=0, column=1, padx=(10, 60), pady=(60, 20))

        self.passwordLabel = customtkinter.CTkLabel(self.loginFrame, text="Password")
        self.passwordLabel.grid(row=1, column=0, padx=(50, 10))

        self.passwordEntry = customtkinter.CTkEntry(self.loginFrame, placeholder_text="Enter your password", width=200, height=30, show="*")
        self.passwordEntry.grid(row=1, column=1, padx=(10, 60))

        self.fpasswordLabel = customtkinter.CTkLabel(self.loginFrame, text="Forget Password?", font=("arial", 12, "underline"))
        self.fpasswordLabel.grid(row=2, column=1, padx=(0, 140), pady=10)
        self.fpasswordLabel.bind("<Button-1>", lambda event: fpassword())

        self.loginButton = customtkinter.CTkButton(self.loginFrame, text="Log In",
                                                  font=("arial", 20),
                                                  corner_radius=10,
                                                  height=30,
                                                  width=40,
                                                  command=self.login)
        self.loginButton.grid(row=3, column=1, padx=(0, 190), pady=20)

        self.signUpLabel = customtkinter.CTkLabel(self.loginFrame, text="Sign Up", font=("arial", 12, "underline"))
        self.signUpLabel.grid(row=4, column=0, padx=(170, 0), pady=30)
        self.signUpLabel.bind("<Button-1>", lambda event: signup())
        
        self.signUpDesc = customtkinter.CTkLabel(self.loginFrame, text="If you are not registered", font=("arial", 12))
        self.signUpDesc.grid(row=4, column=1, padx=(0, 130), pady=30)

    
    def homeP(self):
        messagebox.showinfo(title="Successfully Logged In", message="You have successfully logged in.")
        self.destroy()

        mainWindow = customtkinter.CTk()
        mainWindow.title("Afnaighar")
        mainWindow.geometry("1200x700")

if __name__ == "__main__":
    app = App()
    app.mainloop()
