import tkinter as tk
from tkinter import messagebox as msg 
import sqlite3
from tkinter import ttk

    
class show_users:
    def __init__(self , parent):
        self.connection = sqlite3.connect("Counsoler.db")
        self.cursor = self.connection.cursor()
        
        dataWindow=tk.Toplevel(parent)
        dataWindow.title('Show users')
        # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
        \
        table=ttk.Treeview(dataWindow,columns=("id" ,"Name","lastName","phoneNumber","password", "userName" ,"role"), show="headings")
        table.heading("id", text="ایدی ")
        table.heading("Name", text="نام ")
        table.heading("lastName", text="نام خانوادگی ")
        table.heading("phoneNumber", text="شماره تلفن ")
        table.heading("password", text="پسورد")
        table.heading("userName", text="نام کاربری")
        table.heading("role", text="نقش")
        
        table.column("id" , width=60)
        table.column("Name", width=120)
        table.column("lastName", width=120)
        table.column("phoneNumber", width=80)
        table.column("password", width=60)
        table.column("userName", width=60)
        table.column("role", width=60)
        
        
        self.cursor.execute("SELECT * FROM users")       
        users_data=self.cursor.fetchall()
        
        for item in users_data:
            table.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4] ,item[5] ,item[6]))

        table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)