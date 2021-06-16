from tkinter import *
from tkinter import messagebox as ms
import tkinter as tk
import sqlite3 


def Log():
    Login = tk.Tk()
    Login.geometry('500x500')
    Login.title('Zaloguj się')

    Login.configure(background='#FFF5EE')
    Login.resizable(width=False, height=False)
    Login.iconbitmap('img/loginlogo.ico')

    top_frame = Label(Login, text='Zaloguj się do systemu',font = ('Avenir Next LT Pro Demi', 25, 'bold'), bg='#FFF5EE',relief='groove',padx=500, pady=30)
    top_frame.pack(side='top')

    frame = LabelFrame(Login, padx=40, pady=30, bg='white')
    frame.place(relx = 0.5, rely = 0.55, anchor = CENTER)
    

    def Search(arg = None):
        if username_entry.get() == '': 
            ms.showerror('Wpisz nazwę użytkownika! ')
            
        elif password_entry.get() == '':
            ms.showerror('Wpisz hasło! ')
            
        else:
            global username
            username = username_entry.get()
            global password
            password = password_entry.get()

            conn = sqlite3.connect('Database.db')

            with conn:
                cursor = conn.cursor()

            find_user = ('SELECT * FROM users WHERE Username = ? AND Password = ?')
            cursor.execute(find_user,(username, password))
            results = cursor.fetchall()

            if results:
                Login.destroy()
                result = tk.Tk()
                result.geometry('500x500')
                result.title('Dziękuję!')

                result.configure()
                result.resizable(width=False, height=False)

                label = tk.Label(result, text = 'Witaj, '+ username +'\n Dziękujemy za skorzystanie z naszych usług',font=('Avenir Next LT Pro Demi',12, 'bold'),bg='#FFF5EE', fg='green').place(relx = 0.5, rely = 0.5, anchor = CENTER)


            else:
                ms.showerror('Nie znaleziono użytkownika! Spróbuj zalogować się ponownie. ')

    username = tk.Label(frame, text = 'Login',font=('Avenir Next LT Pro Demi',12, 'bold'),bg='white', fg='black')
    password = tk.Label(frame, text = 'Hasło', font = ('Avenir Next LT Pro Demi',12,'bold'),bg='white', fg='black')

    username_entry = tk.Entry(frame, font=('calibre',10,'normal'), justify = 'center', bg='#FFF5EE')
    username_entry.bind('<Return>', Search)
    password_entry=tk.Entry(frame, font = ('calibre',10,'normal'), show = '*', justify = 'center', bg='#FFF5EE')
    password_entry.bind('<Return>', Search)

    submit=tk.Button(frame,text = 'Login', command = Search, width="10",bd = '3',  font = ('Avenir Next LT Pro Demi', 12, 'bold'), bg='#FFF5EE', fg='black',relief='groove', justify = 'center', pady='5')

    username.pack()
    username_entry.focus_set()
    username_entry.pack()

    label = Label(frame, bg='white').pack()
    
    password.pack() 
    password_entry.pack()

    label = Label(frame, bg='white').pack()
    
    submit.pack()

    Quit = tk.Button(Login, text = "Zamknij", width="10", command = Login.destroy, bd = '3',  font = ('Avenir Next LT Pro Demi', 12, 'bold'), bg='#FFF5EE', fg='black',relief='groove', justify = 'center', pady='5')
    Quit.place(anchor ='sw',rely=1,relx=0.775)
