import tkinter as tk
from tkinter import messagebox as msg 
import sqlite3
from tkinter import ttk

    
class show_reports:
    def __init__(self , parent):
        self.connection = sqlite3.connect("Counsoler.db")
        self.cursor = self.connection.cursor()
        
        dataWindow=tk.Toplevel(parent)
        dataWindow.title('Show reports')
        # اماده کردن بستر خروجی برای مشاهده ی اطلاعات
        
        table=ttk.Treeview(dataWindow,columns=("id" ,"user_code","title","date","state"), show="headings")
        table.heading("id", text="ایدی ")
        table.heading("user_code", text="کد کاربر")
        table.heading("title", text="عنوان گزارش")
        table.heading("date", text="تاریخ درج")
        table.heading("state", text="وضعیت ")
        
        table.column("id" , width=60)
        table.column("user_code", width=120)
        table.column("title", width=120)
        table.column("date", width=80)
        table.column("state", width=60)
        
        
        self.cursor.execute("SELECT * FROM gozareshat")       
        reports_data=self.cursor.fetchall()
        
        for item in reports_data:
            table.insert("", "end", values=(item[0], item[1], item[2], item[3], item[4]))

        table.pack(padx=2, pady=10, fill=tk.BOTH, expand=True)