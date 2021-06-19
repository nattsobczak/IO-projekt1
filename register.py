from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3
from PIL import ImageTk, Image


def Register():
    Reg = tk.Tk()
    Reg.title('Zarejestruj się w Centrum szkoleń')
    Reg.geometry('700x700')

    Reg.configure(background='#3B2C35')
    Reg.resizable(width=False, height=False)
    Reg.iconbitmap('img/reglogo.ico')

    top_frame = Label(Reg, text='Rejestracja',font = ('Avenir Next LT Pro Demi', 25, 'bold'), bg='#7268A6',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')

    frame = LabelFrame(Reg, padx=30, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    

    def database(arg=None):
        name = name_entry.get()
        email = email_entry.get()
        mobile = mobile_entry.get()
        try:
            mobile = int(mobile)
        except:
            ms.showerror('Błąd! ', 'Zły numer telefonu')
        username = username_entry.get()
        password = password_entry.get()
        confirm = confirm_entry.get()

        validation = []

        validation.append(name)
        validation.append(email)
        validation.append(mobile)
        validation.append(username)
        validation.append(password)
        validation.append(confirm)
        condition = True

        for ele in validation:
            if ele == '':
                condition = False
                break

        if condition:

            if password != confirm:
                ms.showerror('Błąd!', 'Hasło nie pasuje')
                
            else:
                conn = sqlite3.connect('Database.db')

                with conn:
                    cursor = conn.cursor()

<<<<<<< HEAD
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (FullName TEXT NOT NULL, Email TEXT NOT NULL, Mobile TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)')

                cursor.execute('INSERT INTO Users (FullName, Email, Mobile, Username, Password) VALUES (?,?,?,?,?)', (name, email, mobile, username, password))
=======
                cursor.execute('CREATE TABLE IF NOT EXISTS Users (Imię_nazwisko TEXT NOT NULL, Email TEXT NOT NULL, Telefon TEXT NOT NULL, Username TEXT NOT NULL, Password TEXT NOT NULL)')

                cursor.execute('INSERT INTO Users (Imię_nazwisko, Email, Telefon, Login, Hasło) VALUES (?,?,?,?,?)', (name, email, mobile, username, password))
>>>>>>> c6d13d0af0a8d3a8882c8454f9400ea341ed8cc6
                conn.commit()

                ms.showinfo('Sukces', 'Konto zostało utworzone, możesz się zalogować')

                Reg.destroy()
            
        else:
            ms.showerror('Błąd!', 'Wypełnij wszystkie pola!')

    name = tk.Label(frame, text = 'Imię i nazwisko', font=('Avenir Next LT Pro Demi',12, 'bold'), bg='white', fg='black')
    email = tk.Label(frame, text = 'Email', font=('Avenir Next LT Pro Demi',12, 'bold'), bg='white', fg='black')
    mobile = tk.Label(frame, text = 'Numer telefonu', font=('Avenir Next LT Pro Demi',12, 'bold'), bg='white', fg='black')
    username = tk.Label(frame, text = 'Login', font=('Avenir Next LT Pro Demi',12, 'bold'), bg='white', fg='black')
    password = tk.Label(frame, text = 'Hasło', font = ('Avenir Next LT Pro Demi',12,'bold'), bg='white', fg='black')
    confirm = tk.Label(frame, text = 'Ponownie wpisz hasło', font=('Avenir Next LT Pro Demi',12, 'bold'), bg='white', fg='black')

    name_entry = tk.Entry(frame ,font=('Avenir Next LT Pro Demi',12,'normal'), bg='#FFF5EE')
    name_entry.bind("<Return>", database)
    email_entry = tk.Entry(frame,font=('Avenir Next LT Pro Demi',12,'normal'), bg='#FFF5EE')
    email_entry.bind("<Return>",database)
    mobile_entry = tk.Entry(frame,font=('Avenir Next LT Pro Demi',12,'normal'), bg='#FFF5EE')
    mobile_entry.bind("<Return>",database)
    username_entry = tk.Entry(frame,font=('Avenir Next LT Pro Demi',12,'normal'), bg='#FFF5EE')
    username_entry.bind("<Return>",database)
    password_entry=tk.Entry(frame, font = ('Avenir Next LT Pro Demi',12,'normal'), show = '*', bg='#FFF5EE')
    password_entry.bind("<Return>",database)
    confirm_entry=tk.Entry(frame, font = ('Avenir Next LT Pro Demi',12,'normal'), show = '*', bg='#FFF5EE')
    confirm_entry.bind("<Return>",database)

    submit=tk.Button(frame,text = 'Rejestracja', command = database, width="10",bd = '3',  font = ('Avenir Next LT Pro Demi', 12, 'bold'),bg='#FFF5EE', fg='black',relief='groove', justify = 'center', pady='5'  )

    name.pack()
    name_entry.focus_set()
    name_entry.pack()

    label = Label(frame, bg='white').pack()
    
    email.pack()
    email_entry.pack()

    label = Label(frame, bg='white').pack()
    mobile.pack()
    mobile_entry.pack()
    label = Label(frame, bg='white').pack()
    
    username.pack() 
    username_entry.pack()
    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()
    label = Label(frame, bg='white').pack()
    
    confirm.pack()
    confirm_entry.pack()

    label = Label(frame, bg='white').pack()
    
    submit.pack()


    Quit = tk.Button(Reg, text = "Zamknij", width="10", command = Reg.destroy, bd = '3',  font = ('Avenir Next LT Pro Demi', 12, 'bold'), bg='black', fg='white',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.84)
