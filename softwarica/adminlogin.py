
import customtkinter
from tkinter import messagebox

def adminLoginPage(callback):
    global passwordEntry
    global adminloginWindow
    adminloginWindow = customtkinter.CTkToplevel()
    adminloginWindow.title("Admin login")
    adminloginWindow.geometry("450x200")
    adminloginWindow.resizable(False, False)

    loginFrame = customtkinter.CTkFrame(adminloginWindow, corner_radius=10, fg_color="#5c364b")
    loginFrame.grid(row=0, column=0, pady=20, padx=20)

    adminLabel = customtkinter.CTkLabel(loginFrame, text="Username")
    adminLabel.grid(row=0, column=0, padx=(20, 10), pady=(10, 10))

    adminEntry = customtkinter.CTkEntry(loginFrame, placeholder_text="Enter your username", width=200, height=30)
    adminEntry.grid(row=0, column=1, padx=(5, 10), pady=5)

    passwordLabel = customtkinter.CTkLabel(loginFrame, text="Password")
    passwordLabel.grid(row=1, column=0, padx=(20, 10), pady=5)

    passwordEntry = customtkinter.CTkEntry(loginFrame, placeholder_text="Enter your password", width=200, height=30, show="*")
    passwordEntry.grid(row=1, column=1, padx=(5, 10), pady=5)

    def toggle_password():
        if show.get():
            passwordEntry.configure(show="")
        else:
            passwordEntry.configure(show="*")

    show = customtkinter.CTkCheckBox(loginFrame, text="Show", font=('arial', 14), command=toggle_password)
    show.grid(row=1, column=2)
    

    def validate_login():
        username = adminEntry.get()
        password = passwordEntry.get()

        
        if username == "admin" and password == "admin123":
            adminloginWindow.destroy()
            callback() 
        else:
            messagebox.showerror("Login Failed", "Invalid username or password")

    adminLoginButton = customtkinter.CTkButton(
        loginFrame,
        text="Login",
        font=("arial", 20, "bold"),
        corner_radius=10,
        height=30,
        width=40,
        cursor="hand1",
        fg_color="#B7D5B5",
        hover_color="#94bf91",
        command=validate_login
    )
    adminLoginButton.grid(row=2, column=0, columnspan=3, pady=20)
