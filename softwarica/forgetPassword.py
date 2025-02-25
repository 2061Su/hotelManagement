from tkinter import *
import customtkinter
from tkinter import messagebox
import sqlite3
from signUp import signup

def fpassword():


  fpasswordWindow=customtkinter.CTkToplevel()
  fpasswordWindow.title("Forget Password ")
  fpasswordWindow.geometry("800x600")

  fpasswordFrame=customtkinter.CTkFrame(fpasswordWindow,corner_radius=10,fg_color="#5c364b")
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


  rpasswordButton=customtkinter.CTkButton(fpasswordFrame,text="Confirm",
                                                font=("arial",20,"bold"),
                                                corner_radius=10,
                                                height=30,
                                                width=40,
                                                cursor="hand1",
                                                fg_color="#B7D5B5",
                                                hover_color="#94bf91",
                                                command=lambda :fpasswordButton(usernameEntry.get(),numberEntry.get(),passwordEntry.get()),)
  rpasswordButton.grid(row=4,column=1,padx=(0,190),pady=20)

  def fpasswordButton(username,number,password):
    try:
      password= passwordEntry.get()

      if 8 <= len(password) <= 15 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password):
        conn = sqlite3.connect('users.db')
        cursor = conn.cursor()
        
        # Get the list of users (username, phone_number)
        users = signup()

        # Check if the username and phone number match
        cursor.execute("SELECT * FROM users WHERE username=? AND phone_number=?", (username, number))
        user = cursor.fetchone()
        
        
        if user:
            # Update the password
            cursor.execute("UPDATE users SET password=? WHERE username=? AND phone_number=?", (password, username, number))
            conn.commit()
            messagebox.showinfo(title="Password Changed", message="You have successfully changed your password.")
            fpasswordWindow.destroy()
            fpasswordWindow.update()
        else:
          messagebox.showinfo(title="invalid",message="incorrect username and phone number")
      else:
        messagebox.showinfo(title="password error ",message="""-Password must be at least 8 characters long.\n-Password must be no more than 15 characters long.\n-Password must contain at least one uppercase letter.\n-Password must contain at least one lowercase letter.\n-Password must contain at least one digit.\n-Password must contain at least one special character.""")
    except Exception as e:
      messagebox.showinfo(title="Error", message=f"An error occurred: {e}")
    finally:
      if conn:
          conn.close()
