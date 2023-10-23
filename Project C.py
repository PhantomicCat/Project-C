import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter import filedialog
import random
import webbrowser

# Window

Base = tk.Tk()
Base.geometry ("570x350")
Base.title ("Project C")

# Label 

L1 = ttk.Label (Base, text = "Project C", font = ("Montserrat Bold", 30))
L1.pack(pady = 50)

# Buttons

#! Break Button function

def Delta ():
    messagebox.showwarning ("Delta", "Warning, Delta can't break every file. For more information visit Project-C's GitHub page.")
    File_Explorer = filedialog.askopenfilename()
    with open (File_Explorer, 'w') as file:
        for corrupt in range (1000):
            random.randint (1, 555555)
            file.write (str(corrupt))
        messagebox.showinfo ('Delta', 'File broken or rewritten successfully!')
            
## Break! Button

B1 = ttk.Button (text = "Brake!", command = Delta)
B1.place(x = 170, y = 235, width= 225, height = 75)

## GitHub Button

def GitHub ():
    webbrowser.open ("https://github.com/PhantomicCat/Project-C")


B2 = ttk.Button (text = "GitHub", command = GitHub)
B2.place (x = 70, y = 235, width= 90, height = 75)

#! About Function

def AT ():
    About = tk.Tk()
    About.geometry ("500x350")
    About.title ("About Project-C")

    AL1 = ttk.Label (About, text = "Project C", font = ("Montserrat Bold", 20))
    AL1.pack(pady = 5)

    AL2 = ttk.Label (About, text = "GitHub Version 1.0", font = ("Montserrat Medium", 15))
    AL2.pack()

    AL3 = ttk.Label (About, text = "This is an Open Source Project, you can download .EXE and Source Code on GitHub!", font = ("Montserrat Medium", 8))
    AL3.pack(pady = 10)

    AL4 = ttk.Label (About, text = "Created by PhantomicCat", font = ("Montserrat Medium", 12))
    AL4.pack(pady = 85)

    About.mainloop ()

# About Button

B3 = ttk.Button (text = "About", command = AT)
B3.place (x = 405, y = 235, width= 90, height = 75)

# Window mainloop

Base.mainloop ()