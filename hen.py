# exec(open("button.py").read())
# import subprocess
#
# subprocess.call("bhanumatii.py", shell=True)
#exec(open("button.py").read())
from tkinter import *
from PIL import ImageTk, Image

import subprocess
from tkinter import messagebox
from tkinter import ttk

# Create an instance of tkinter frame
win= Tk()

# Set the size of the tkinter window
win.geometry("2000x1500")

# Define a function to show the popup message
def show_msg():
   subprocess.call("bhanumatii.py", shell=True)

# Add an optional Label widget

frame = Frame(win, width=300, height=800)
frame.pack()
frame.place(anchor=SW,x=60,y=720)

# Create an object of tkinter ImageTk
img= (Image.open("nk.png"))
resized_image= img.resize((1250,690), Image.ANTIALIAS)
new_image= ImageTk.PhotoImage(resized_image)

# Create a Label Widget to display the text or Image
label = Label(frame, image = new_image,bg='white')
label.pack()

# Create a Button to display the message
btn=Button(win, text= "Click Here", command=show_msg,fg="white",font= ('Helvetica 20 bold '),bg="black")
btn.place(x=1000,y=580)
btn.config(width=12,height=2)



win.attributes('-fullscreen', True)
win.mainloop()








