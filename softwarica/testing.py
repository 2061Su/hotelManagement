from tkinter import *
import customtkinter
from tkinter import messagebox
from PIL import ImageTk,Image
from signUp import signup
from forgetPassword import fpassword
import sqlite3
import homePage


customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")


class App(customtkinter.CTk):
  def __init__(self):
    super().__init__()
    self.loginPage()
    self.mainloop()

# loginWindow=customtkinter.CTk()
  def loginPage(self):
      self.geometry("1200x800")
      self.title("Hotel Management System")

    

      self.hotelName=customtkinter.CTkLabel(self,text="AfnaiGhar", font=("Comic Sans MS",64,"bold"),text_color="white")
      self.hotelName.grid(row=0,column=0,padx=100,pady=50)

      self.loginFrame=customtkinter.CTkFrame(self,corner_radius=10)
      self.loginFrame.grid(row=1,column=0,padx=500)



      # login frame element
      self.userLabel=customtkinter.CTkLabel(self.loginFrame,text="username")
      self.userLabel.grid(row=0,column=0,padx=(20,10),pady=(60,20))

      self.userEntry=customtkinter.CTkEntry(self.loginFrame,placeholder_text="Enter your username",width=200,height=30)
      self.userEntry.grid(row=0,column=1,padx=(10,60),pady=(60,20))

      self.passwordLabel=customtkinter.CTkLabel(self.loginFrame,text="Password")
      self.passwordLabel.grid(row=1,column=0,padx=(20,10))

      self.passwordEntry=customtkinter.CTkEntry(self.loginFrame,placeholder_text="Enter your password",width=200,height=30,show="*",)
      self.passwordEntry.grid(row=1,column=1,padx=(10,60))

      self.show=customtkinter.CTkCheckBox(self.loginFrame,text="Show",font=('arial',14),command=self.toggle_password)
      self.show.grid(row=1,column=2,)


      self.fpasswordLabel=customtkinter.CTkLabel(self.loginFrame,text="Forget Password?",font=("arial",12,"underline"),cursor="hand2")
      self.fpasswordLabel.grid(row=2,column=1,padx=(0,140),pady=10)
      self.fpasswordLabel.bind("<Button-1>", lambda event: fpassword()) 


      self.loginButton=customtkinter.CTkButton(self.loginFrame,text="LogIn",
                                                    font=("arial",20,"bold"),
                                                    corner_radius=10,
                                                    height=30,
                                                    width=40,
                                                    cursor="hand1",
                                                    fg_color="#B7D5B5",
                                                    command=self.login)
      self.loginButton.grid(row=3,column=1,padx=(0,190),pady=20)

      self.signUpLabel=customtkinter.CTkLabel(self.loginFrame,text="Sign Up", font=("arial",12,"underline"),cursor="hand2")
      self.signUpLabel.grid(row=4,column=0,padx=(170,0),pady=30)
      self.signUpLabel.bind("<Button-1>", lambda event: signup()) 
      self.signUpLabel=customtkinter.CTkLabel(self.loginFrame,text="If you are not registered", font=("arial",12,))
      self.signUpLabel.grid(row=4,column=1,padx=(0,130),pady=30)

  def toggle_password(self):
    if self.show.get():
      self.passwordEntry.configure(show="")
    else:
      self.passwordEntry.configure(show="*")
  def login(self):
    username=self.userEntry.get()
    password=self.passwordEntry.get()
    if authenticate_user(username,password):
      messagebox.showinfo(title="successfully logged in ",message="you have successfully logged in!")
      self.schedule_transition()
    else:
      messagebox.showerror(title="Error",message="invalid username or password!")
  
  def schedule_transition(self):
      self.after(1000, self.transition_to_homepage)  # Add a delay of 1000 milliseconds (1 second)

  def transition_to_homepage(self):
      self.destroy()
      homePage.HomePage().mainloop()
    # self.home_page = HomePage()
    # self.after_id=self.after(100, self.home_page.mainPage())
    
  

def authenticate_user(username,password):
  conn=sqlite3.connect("users.db")
  cursor=conn.cursor()

  cursor.execute("SELECT * FROM users WHERE username=? AND password=?",(username,password))
  user=cursor.fetchone()
  conn.close()
  return user is not None
if __name__=="__main__":
  try:

    conn = sqlite3.connect('users.db')
    cursor = conn.cursor()

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        first_name TEXT NOT NULL,
        last_name TEXT NOT NULL,
        phone_number TEXT NOT NULL
    )
    ''')

   
    conn.commit()
    conn.close()
    App()
    
  except Exception as e:
    print(f"An error occurred: {e}")
