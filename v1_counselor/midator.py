import tkinter as tk 
# from tkinter import messagebox as msg
# فقط کلاس رابط کاربری امده است 
# و رابط کاربری جوری طراحی شده است که با اجرای ان بقیه ی کلاس ها نیز اجرا خواهد شد 
from add_report import tkinter_report
from add_user import tkinter
from show_users import show_users
from show_reports import show_reports


class user_interface:
    def __init__(self , parent):
        self.win=tk.Toplevel(parent)
        self.win.title("برنامه ی مشاوره ")
        self.win.geometry("800x800")

        btn_main=tk.Button(self.win , text="ثبت کاربر "  , command=self.conn_users)
        btn_main.grid(row=0 , column=1)

        btn_users=tk.Button(self.win , text="ثبت گزارش" , command=self.conn_reports)
        btn_users.grid(row=1  , column=1 , padx=50 , pady=50)
        
        btn_users=tk.Button(self.win , text="لیست کاربران ", command=self.conn_show_users)
        btn_users.grid(row=2  , column=1 , padx=50 , pady=50)
        
        btn_users=tk.Button(self.win , text="لیست گزارشات" , command=self.conn_show_reports )
        btn_users.grid(row=3  , column=1 , padx=50 , pady=50)
        
        btn_users=tk.Button(self.win , text="تنظیمات" )
        btn_users.grid(row=4  , column=1 , padx=50 , pady=50)
                

        self.win.mainloop()
        
    def conn_reports(self):
        tkinter_report(self.win)
    def conn_users(self):
        tkinter(self.win)
    def conn_show_users(self):
        show_users(self.win)
    def conn_show_reports(self):
        show_reports(self.win)
    
        