from tkinter import *
import customtkinter
from tkinter import messagebox
import sqlite3

def signup():
  signupWindow=customtkinter.CTkToplevel()
  signupWindow.title("signup")
  signupWindow.geometry("1000x600")

  signupFrame=customtkinter.CTkFrame(signupWindow,corner_radius=10,fg_color="#5c364b")
  signupFrame.grid(row=0,column=0,padx=(100,0),pady=(100,0))



  # login frame element
  userLabel=customtkinter.CTkLabel(signupFrame,text="First Name")
  userLabel.grid(row=0,column=0,padx=(50,10),pady=(60,20))

  userEntry=customtkinter.CTkEntry(signupFrame,placeholder_text="Enter your firstname",width=200,height=30)
  userEntry.grid(row=0,column=1,padx=(10,60),pady=(60,20))

  user1Label=customtkinter.CTkLabel(signupFrame,text="Last Name")
  user1Label.grid(row=1,column=0,padx=(50,10))

  user1Entry=customtkinter.CTkEntry(signupFrame,placeholder_text="Enter your lastname",width=200,height=30)
  user1Entry.grid(row=1,column=1,padx=(10,60))

  usernameLabel=customtkinter.CTkLabel(signupFrame,text="Username")
  usernameLabel.grid(row=2,column=0,padx=(50,10))

  usernameEntry=customtkinter.CTkEntry(signupFrame,width=200,height=30)
  usernameEntry.grid(row=2,column=1,padx=(10,60),pady=20)

  passwordLabel=customtkinter.CTkLabel(signupFrame,text="Password")
  passwordLabel.grid(row=3,column=0,padx=(50,10))

  def toggle_password():
    if show.get():
        passwordEntry.configure(show="")
    else:
        passwordEntry.configure(show="*")
    
    if show1.get():
        rpasswordEntry.configure(show="")
    else:
        rpasswordEntry.configure(show="*")

  


  passwordEntry=customtkinter.CTkEntry(signupFrame,placeholder_text="Enter new-password",width=200,height=30,show="*")
  passwordEntry.grid(row=3,column=1,padx=(10,60))

  show=customtkinter.CTkCheckBox(signupFrame,text="Show",font=('arial',14),command=toggle_password)
  show.grid(row=3,column=0,columnspan=2,padx=(550,0))


  rpasswordLabel=customtkinter.CTkLabel(signupFrame,text="re-Type password")
  rpasswordLabel.grid(row=4,column=0,padx=(50,10))

  rpasswordEntry=customtkinter.CTkEntry(signupFrame,placeholder_text="Confirm password",width=200,height=30,show="*")
  rpasswordEntry.grid(row=4,column=1,padx=(10,60),pady=20)

  show1=customtkinter.CTkCheckBox(signupFrame,text="Show",font=('arial',14),command=toggle_password)
  show1.grid(row=4,column=0,columnspan=2,padx=(550,0))

  numberLabel=customtkinter.CTkLabel(signupFrame,text="Phone Number")
  numberLabel.grid(row=5,column=0,padx=(50,10))

  numberEntry=customtkinter.CTkEntry(signupFrame,placeholder_text="Enter your number",width=200,height=30)
  numberEntry.grid(row=5,column=1,padx=(10,60))
  

  def fpasswordButton():
    password= passwordEntry.get()
    if 8 <= len(password) <= 15 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password):
      messagebox.showinfo(title="successfully changed password ",message="you have successfully changed your password.")
      fpasswordWindow.destroy()
    else:
      messagebox.showinfo(title="password error ",message="""-Password must be at least 8 characters long.\n-Password must be no more than 15 characters long.\n-Password must contain at least one uppercase letter.\n-Password must contain at least one lowercase letter.\n-Password must contain at least one digit.\n-Password must contain at least one special character.""")

  


  def register_user(username,password,first_name,last_name,phone_number):
    password=passwordEntry.get()
    conn=None
    
    
    try:
      if 8 <= len(password) <= 15 and any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(not c.isalnum() for c in password):
        conn=sqlite3.connect("users.db")
        cursor=conn.cursor()

        cursor.execute('INSERT INTO users(username,password,first_name,last_name,phone_number) VALUES (?,?,?,?,?)',(username,password,first_name,last_name,phone_number))
        conn.commit()
        messagebox.showinfo(title="successfully signedUp ",message="you have successfully created your account.")
        signupWindow.destroy()
      else:
        messagebox.showinfo(title="password error ",message="""-Password must be at least 8 characters long.\n-Password must be no more than 15 characters long.\n-Password must contain at least one uppercase letter.\n-Password must contain at least one lowercase letter.\n-Password must contain at least one digit.\n-Password must contain at least one special character.""")

    except sqlite3.IntegrityError:
      messagebox.showerror("Error", "Username already exists!")
    finally:
      if conn:
        conn.close()
    
    


  signupButton=customtkinter.CTkButton(signupFrame,text="SignUp",
                                                font=("arial",20,"bold"),
                                                corner_radius=10,
                                                height=30,
                                                width=40,
                                                cursor="hand1",
                                                fg_color="#B7D5B5",
                                                hover_color="#94bf91",
                                                command=lambda : register_user(usernameEntry.get(),passwordEntry.get(),userEntry.get(),user1Entry.get(),numberEntry.get(),),)
  signupButton.grid(row=6,column=1,padx=(0,190),pady=20)

  
