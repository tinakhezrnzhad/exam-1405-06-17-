import tkinter as tk
from tkinter import messagebox as msg 
import sqlite3
from tkinter import ttk

class gozareshat:
    def __init__(self):
        self.connection = sqlite3.connect("Counsoler.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS gozareshat (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_code TEXT,
            title TEXT,
            date TEXT,
            state TEXT
        )
        """)
        self.connection.commit()
    
    def add_report(self ,user_code , title , date, state):
        
        if state=="در حال بررسی ":
            roleNumber=0
        elif state=="پاسخ داده شده":
            roleNumber=1
        self.cursor.execute("""
        INSERT INTO gozareshat(user_code, title, date, state )
        VALUES (?, ?, ?, ?)
        """,(user_code, title, date, roleNumber ))
        self.connection.commit()
        msg.showinfo("موفق!" , "گزارش با موفقیت اضافه شد ")
        
        self.connection.commit()
        
report=gozareshat()


class tkinter_report():    
    def __init__(self , parent):
        self.win=tk.Toplevel(parent)
        self.win.title("اضافه کردن گزارش")
        self.win.geometry("500x300")

        tk.Label(self.win , text="کد کاربر").grid(row=0, column=0)
        self.code = tk.Entry(self.win)
        self.code.grid(row=0, column=1, padx=5, pady=5) 
        
        tk.Label(self.win , text="عنوان گزارش ").grid(row=1, column=0)
        self.title = tk.Entry(self.win)
        self.title.grid(row=1, column=1, padx=5, pady=5)  
        
        tk.Label(self.win , text="تاریخ درج").grid(row=2, column=0)
        self.date = tk.Entry(self.win)
        self.date.grid(row=2, column=1, padx=5, pady=5) 
        
        states = [ "پاسخ داده شده" , "در حال بررسی "]
        states_var = tk.StringVar(self.win) #?
        states_var.set(states[0])
        ttk.Label(self.win , text="roles").grid(row=3 , column=0)
        self.state_combobox = ttk.Combobox(self.win, textvariable=states_var, values=states, state="readonly")
        self.state_combobox.grid(row=3, column=1, padx=5, pady=5) 
        
        btn = tk.Button(self.win , text="Add report" , command=lambda: report.add_report (
            self.code.get(),
            self.title.get(),
            self.date.get(),
            self.state_combobox.get()
        ))
        btn.grid(row=4, column=1)
        
        self.win.mainloop()

