import tkinter as tk
from tkinter import ttk
from tkinter import *
import customtkinter
 
class Scrollable(tk.Frame):
    """
       Make a frame scrollable with scrollbar on the right.
       After adding or removing widgets to the scrollable frame, 
       call the update() method to refresh the scrollable area.
    """
 
    def __init__(self, frame, width=16):
 
        scrollbar = tk.Scrollbar(frame, width=width)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)#, expand=False)
 
        self.canvas = tk.Canvas(frame, yscrollcommand=scrollbar.set)
        self.canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
 
        scrollbar.config(command=self.canvas.yview)
 
        self.canvas.bind('<Configure>', self.__fill_canvas)
 
        # base class initialization
        tk.Frame.__init__(self, frame)         
 
        # assign this obj (the inner frame) to the windows item of the canvas
        self.windows_item = self.canvas.create_window(0,0, window=self, anchor=tk.NW)
 
 
    def __fill_canvas(self, event):
        "Enlarge the windows item to the canvas width"
 
        canvas_width = event.width
        self.canvas.itemconfig(self.windows_item, width = canvas_width)        
 
    def update(self):
        "Update the canvas and the scrollregion"
 
        self.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox(self.windows_item))
 
 

 
root.geometry('1000x700+100+50')
root.resizable('False','False')
header = Frame(root)
body = Frame(root)
footer = Frame(root)
header.pack()
body.pack(fill='x')
footer.pack()
header.configure(width=200, height=100)
 
 
l1=Label(header, text="The header")
l1.grid(column=0,row=0)
ttk.Label(footer, text="The Footer").pack()
 
 
scrollable_body = Scrollable(body, width=32)
 
for i in range(30):
    ttk.Button(scrollable_body, text="I'm a button in the scrollable frame").grid(column=0,row=i)
    ttk.Button(scrollable_body, text="I'm").grid(column=1,row=i)
 
scrollable_body.update()
 
root