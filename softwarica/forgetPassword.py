from tkinter import *
import customtkinter
from tkinter import messagebox

def fpassword():
  fpasswordWindow=customtkinter.CTkToplevel()
  fpasswordWindow.title("Forget Password ")
  fpasswordWindow.geometry("800x600")

  fpasswordFrame=customtkinter.CTkFrame(fpasswordWindow,corner_radius=10)
  fpasswordFrame.grid(row=0,column=0,padx=(100,0),pady=(100,0))

  usernameLabel=customtkinter.CTkLabel(fpasswordFrame,text="Username")
  usernameLabel.grid(row=0,column=0,padx=(50,10))

  usernameEntry=customtkinter.CTkEntry(fpasswordFrame,width=200,height=30,placeholder_text="Enter your username")
  usernameEntry.grid(row=0,column=1,padx=(10,60),pady=20)

  numberLabel=customtkinter.CTkLabel(fpasswordFrame,text="Phone Number")
  numberLabel.grid(row=1,column=0,padx=(50,10))

  numberEntry=customtkinter.CTkEntry(fpasswordFrame,placeholder_text="Enter your phone Number",width=200,height=30)
  numberEntry.grid(row=1,column=1,padx=(10,60),pady=20)

  passwordLabel=customtkinter.CTkLabel(fpasswordFrame,text="Password")
  passwordLabel.grid(row=2,column=0,padx=(50,10))
  

  def toggle_password():
    if show.get():
      passwordEntry.configure(show="")
    else:
      passwordEntry.configure(show="*")

    if show1.get():
      rpasswordEntry.configure(show="")
    else:
      rpasswordEntry.configure(show="*")

  passwordEntry=customtkinter.CTkEntry(fpasswordFrame,placeholder_text="Enter new-password",width=200,height=30,show="*",)
  passwordEntry.grid(row=2,column=1,padx=(10,60),pady=20)

  show=customtkinter.CTkCheckBox(fpasswordFrame,text="Show",font=('arial',14),command=toggle_password)
  show.grid(row=2,column=0,columnspan=2,padx=(550,0))

  rpasswordLabel=customtkinter.CTkLabel(fpasswordFrame,text="re-Type password")
  rpasswordLabel.grid(row=3,column=0,padx=(50,10))

  rpasswordEntry=customtkinter.CTkEntry(fpasswordFrame,placeholder_text="Confirm password",width=200,height=30,show="*")
  rpasswordEntry.grid(row=3,column=1,padx=(10,60),pady=20)

  show1=customtkinter.CTkCheckBox(fpasswordFrame,text="Show",font=('arial',14),command=toggle_password)
  show1.grid(row=3,column=0,columnspan=2,padx=(550,0))

  def fpasswordButton():
    password= passwordEntry.get()
    if 8 <= len(password) <= 15 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password):
      messagebox.showinfo(title="successfully changed password ",message="you have successfully changed your password.")
      fpasswordWindow.destroy()
    else:
      messagebox.showinfo(title="password error ",message="""-Password must be at least 8 characters long.\n-Password must be no more than 15 characters long.\n-Password must contain at least one uppercase letter.\n-Password must contain at least one lowercase letter.\n-Password must contain at least one digit.\n-Password must contain at least one special character.""")


  rpasswordButton=customtkinter.CTkButton(fpasswordFrame,text="Confirm",
                                                font=("arial",20,"bold"),
                                                corner_radius=10,
                                                height=30,
                                                width=40,
                                                cursor="hand1",
                                                fg_color="#B7D5B5",
                                                command=fpasswordButton,)
  rpasswordButton.grid(row=4,column=1,padx=(0,190),pady=20)
