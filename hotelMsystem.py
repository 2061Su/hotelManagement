from tkinter import *
from PIL import ImageTk, Image
from tkinter import ttk
from tkinter import messagebox



# login function
def login():
  # if usernameB.get() == "sumit2061" and passwordB.get()=="123":

    # home page 
    homeP=Toplevel()
    width= homeP.winfo_screenwidth() 
    height= homeP.winfo_screenheight()
    homeP.geometry("%dx%d" % (width, height))

    s3 = ttk.Style()
    s3.configure('homeFrame.TFrame', background="#434343", relief="raised")


    homeFrame = ttk.Frame(homeP, style='homeFrame.TFrame')
    homeFrame.pack(fill="both",expand=True)



    # hotel logo
    hLogo=Label(homeFrame,
                text="Afnaighar",
                font=("Comic Sans MS", 48, "bold"),
                fg="white")
    hLogo.place(x=50,y=40)
    hHome=Label(homeFrame,
                text="HOME",
                font=("Comic Sans MS", 16),
                fg="white")
    hHome.place(x=800,y=40)
    hRooms=Label(homeFrame,
                text="ROOMS",
                font=("Comic Sans MS", 16),
                fg="white")
    hRooms.place(x=900,y=40)
    hAbout=Label(homeFrame,
                text="ABOUT US",
                font=("Comic Sans MS", 16),
                fg="white")
    hAbout.place(x=1000,y=40)
    hContact=Label(homeFrame,
                text="CONTACT",
                font=("Comic Sans MS", 16),
                fg="white")
    hContact.place(x=1130,y=40)
    hDetails=Label(homeFrame,
                text="DETAILS",
                font=("Comic Sans MS", 16),
                fg="white")
    hDetails.place(x=1250,y=40)


    
    # s4 = ttk.Style()
    # s4.configure('homeEFrame.TFrame', background="#oCoCoC", relief="raised")

    



# forget password submit  function
def submit():
  messagebox.showinfo(title="Password changed ",message="you have successfully changed your password.")


# signup function 
def create():
  messagebox.showinfo(title="Account created ",message="you have successfully created your account.")


    
# forget password interface
def forgetP ():
  global submit
  forgetPage=Toplevel()
  width= forgetPage.winfo_screenwidth() 
  height= forgetPage.winfo_screenheight()
  forgetPage.geometry("%dx%d" % (width, height))

  s1 = ttk.Style()
  s1.configure('forgetPFrame.TFrame', background="#434343", relief="raised")


  forgetPFrame = ttk.Frame(forgetPage, width=599, height=462, style='forgetPFrame.TFrame')
  forgetPFrame.place(x=450,y=250)
  # username line
  usernameL=Label(forgetPFrame,text="Username :" ,font=("Arial",20))
  usernameL.place(x=50,y=80)
  usernameB=Entry(forgetPFrame,font=("Arial",20))
  usernameB.place(x=200,y=80)

  # phone n line
  phoneNumberL=Label(forgetPFrame,text="Phone-N :" ,font=("Arial",20))
  phoneNumberL.place(x=50,y=150)
  phoneNumberB=Entry(forgetPFrame,font=("Arial",20))
  phoneNumberB.place(x=200,y=150)

  # new  password line
  
  newPasswordL=Label(forgetPFrame,text="Password :",font=("Arial",20))
  newPasswordL.place(x=50,y=220)
  newPasswordB=Entry(forgetPFrame,text="New password",font=("Arial",20))
  newPasswordB.place(x=200,y=220)
  confirmPasswordL=Label(forgetPFrame,text="Password :",font=("Arial",20))
  confirmPasswordL.place(x=50,y=290)
  confirmPasswordB=Entry(forgetPFrame,text="New password",font=("Arial",20))
  confirmPasswordB.place(x=200,y=290)

  submit= Button(forgetPFrame, command=submit,
               text="Submit",
               font=('Microsoft Sans Serif',24,'bold'),
               fg="#FFFFFF",
               bg="#B7D5B5",
               activebackground="#CAEAC8",
               activeforeground="#FFFFFF")
  submit.place(x=250,y=350)




    
# sign up  interface
def signUp():
  global create
  signUpPage=Toplevel()
  width= signUpPage.winfo_screenwidth() 
  height= signUpPage.winfo_screenheight()
  signUpPage.geometry("%dx%d" % (width, height))

  s2 = ttk.Style()
  s2.configure('signUpFrame.TFrame', background="#434343", relief="raised")


  signUpFrame = ttk.Frame(signUpPage, width=599, height=462, style='signUpFrame.TFrame')
  signUpFrame.place(x=450,y=250)
  # username line
  usernameL=Label(signUpFrame,text="Username :" ,font=("Arial",20))
  usernameL.place(x=50,y=80)
  usernameB=Entry(signUpFrame,font=("Arial",20))
  usernameB.place(x=200,y=80)

  # phone n line
  phoneNumberL=Label(signUpFrame,text="Phone-N :" ,font=("Arial",20))
  phoneNumberL.place(x=50,y=150)
  phoneNumberB=Entry(signUpFrame,font=("Arial",20))
  phoneNumberB.place(x=200,y=150)

  # new  password line
  
  newPasswordL=Label(signUpFrame,text="Password :",font=("Arial",20))
  newPasswordL.place(x=50,y=220)
  newPasswordB=Entry(signUpFrame,text="New password",font=("Arial",20))
  newPasswordB.place(x=200,y=220)
  confirmPasswordL=Label(signUpFrame,text="Password :",font=("Arial",20))
  confirmPasswordL.place(x=50,y=290)
  confirmPasswordB=Entry(signUpFrame,text="New password",font=("Arial",20))
  confirmPasswordB.place(x=200,y=290)

  create= Button(signUpFrame, command=create,
               text="Create",
               font=('Microsoft Sans Serif',24,'bold'),
               fg="#FFFFFF",
               bg="#B7D5B5",
               activebackground="#CAEAC8",
               activeforeground="#FFFFFF")
  create.place(x=250,y=350)



  

window = Tk()
# main login window

window.title("Afnaighar")
window.iconbitmap('logo1.jpg')


width= window.winfo_screenwidth() 
height= window.winfo_screenheight()
window.geometry("%dx%d" % (width, height))

# hotel name
logo = Label(text="Afnaighar",
             font=("Comic Sans MS", 64, "bold"),
             fg="white",
             )
logo.place(x=550,y=80)

s = ttk.Style()
s.configure('loginFrame.TFrame', background="#434343", relief="raised")


loginFrame = ttk.Frame(window, width=599, height=462, style='loginFrame.TFrame')
loginFrame.place(x=450,y=250)

usernameL=Label(loginFrame,text="Username :" ,font=("Arial",20))
usernameL.place(x=50,y=80)
usernameB=Entry(loginFrame,font=("Arial",20))
usernameB.place(x=200,y=80)
passwordL=Label(loginFrame,text="Password :" ,font=("Arial",20),)
passwordL.place(x=50,y=150)
passwordB=Entry(loginFrame,font=("Arial",20),show="*")
passwordB.place(x=200,y=150)
show=Checkbutton(loginFrame,text="show",font=('Microsoft Sans Serif',15))
show.place(x=515,y=150)
passwordF=Button(loginFrame,command=forgetP,text="Forget password ?",font=('Microsoft Sans Serif',15))

passwordF.place(x=200,y=200)

login = Button(loginFrame, command=login,
               text="Login",
               font=('Microsoft Sans Serif',24,'bold'),
               fg="#FFFFFF",
               bg="#B7D5B5",
               activebackground="#CAEAC8",
               activeforeground="#FFFFFF")
login.place(x=250,y=280)

signUp=Button(loginFrame,command=signUp,
             text="Sign up",
             font=('Microsoft Sans Serif',16,'bold'))

signUp.place(x=180,y=395)

signT=Label(loginFrame,
             text="if you are not registered",
             font=('Microsoft Sans Serif',16))
signT.place(x=290,y=400)


window.mainloop()
