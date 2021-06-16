from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from login import Log
from register import Register
from PIL import ImageTk, Image


system = tk.Tk()
system.geometry('500x500')

system.resizable(width=False, height=False)
system.title('Centrum szkoleń - Logowanie i rejestracja')

system.iconbitmap('img/Logo.ico')

top_frame = Label(system, text='',font = ('Arial Nova Cond Light', 40, 'bold'),relief='groove',padx=500, pady=5)
top_frame.pack(side='top')

canvas = Canvas(system, width=500, height=350)


image = ImageTk.PhotoImage(Image.open('img/bg.jpg'))
canvas.create_image(0,0, anchor=NW, image=image)
canvas.pack()

frame = LabelFrame(system, padx=30, pady=40, bd='5', relief='groove')
frame.place(relx = 0.5, rely = 0.5, anchor = CENTER)


login = tk.Button(frame, text = "Zaloguj", width="10", bd = '3', command = Log, font = ('Avenir Next LT Pro Demi', 12, 'bold'), bg='#FFF5EE',relief='groove', justify = 'center', pady='5')
login.pack()

label = Label(frame, bg='white').pack()

register = tk.Button(frame, text = "Rejestracja", width="10", bd = '3',  command = Register, font = ('Avenir Next LT Pro Demi', 12, 'bold'), bg='#FFF5EE',fg='black', relief='groove', justify = 'center', pady='5')
register.pack()


def Quit():
    response = ms.askokcancel('Zamknięcie systemu', 'Czy chcesz zamknąć system ?')
    if response == 1:
        system.destroy()
    else:
        pass
    
Quit = tk.Button(system, text = "Zamknij", width="10", command = Quit, bd = '3',  font = ('Avenir Next LT Pro Demi', 12, 'bold'), bg='#FFF5EE', fg='black',relief='groove', justify = 'center', pady='5')
Quit.place(anchor ='sw',rely=1,relx=0.775)
system.mainloop()
    
