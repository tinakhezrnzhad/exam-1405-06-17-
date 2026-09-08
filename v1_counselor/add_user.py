import tkinter as tk
from tkinter import messagebox as msg 
import sqlite3
from tkinter import ttk

class users:
    def __init__(self):
        self.connection = sqlite3.connect("StoreRoom.db")
        self.cursor = self.connection.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Name TEXT,
            lastName TEXT,
            phoneNumber TEXT,
            password TEXT,
            userName TEXT ,
            role TINYINT ,
            statusDE TINYINT
        )
        """)
        self.connection.commit()
        
    def add_user(self , name , last_name , phone , password , userName, role , statusDE):
        self.cursor.execute("""
        SELECT COUNT(*) AS number_of_user_entry FROM users WHERE userName=?
        """ ,(userName,))
        number_of_user_entry=self.cursor.fetchone()[0]
        # اولین نتیجه ای که پیدا کردی را برگردان
        if number_of_user_entry==0:
            self.cursor = self.connection.cursor()
            if role=="دانش آموز":
                roleNumber=1
            elif role=="مشاور":
                roleNumber=2
            elif role=="معلم":
                roleNumber=3
            elif role=="اولیا":
                roleNumber=4
            
            self.cursor.execute("""
            INSERT INTO users(Name, lastName, phoneNumber,  address , userName ,role , statusDE)
            VALUES (?, ?, ?, ?, ? , ? )
            """,(name, last_name, phone, password, userName , roleNumber , 1))
            self.connection.commit()
            msg.showinfo("موفق!" , "کاربر با موفقیت اضافه شد ")
        else:
            msg.showinfo("نام کاربری تکراری " , "این نام کاربری از قبل استفاده شده است ")
            
    
    # def disable_user(self, user_code ):
    #     self.cursor.execute("""
    #         UPDATE users
    #         SET statusDE = ?
    #         WHERE user_code = ?
    #     """, ("غیرفعال", user_code))

    #     self.connection.commit()  
    
    # def enable_user(self, user_code):
    #     self.cursor.execute("""
    #         UPDATE users
    #         SET status = ?
    #         WHERE user_code = ?
    #     """, ("فعال", user_code))

        self.connection.commit()   
    
    # def search_user(self):
    #     try:
    #         self.cursor.execute('SELECT name, price, pdate, edate, qty FROM Stores WHERE id=?' , (id,))
    #     except:
    #         msg.showinfo("error","invalid input!")
    # این سرچ را برای این میزارم که وقتی یه کاربر برگردانده شد و پیدا شد بعدش اون دکمه های فعال یا غیر فعال را براش بزاریم
    
          
         
user=users()
class tkinter:
    def __init__(self , parent):
        self.win=tk.Toplevel(parent)
        self.win.title("Add User")
        self.win.geometry("500x300")

        tk.Label(self.win , text="name:").grid(row=0, column=0)
        self.Name = tk.Entry(self.win)
        self.Name.grid(row=0, column=1, padx=5, pady=5)

        tk.Label(self.win , text="last name:").grid(row=1, column=0)
        self.lastName = tk.Entry(self.win)
        self.lastName.grid(row=1, column=1, padx=5, pady=5)

        tk.Label(self.win , text="phone number:").grid(row=2, column=0)
        self.phoneNumber = tk.Entry(self.win)
        self.phoneNumber.grid(row=2, column=1, padx=5, pady=5)

        tk.Label(self.win , text="password:").grid(row=3, column=0)
        self.password = tk.Entry(self.win)
        self.password.grid(row=3, column=1, padx=5, pady=5)
        
        tk.Label(self.win , text="User Name").grid(row=5, column=0)
        self.userName = tk.Entry(self.win)
        self.userName.grid(row=5, column=1, padx=5, pady=5)
        
        roles = ["دانش آموز" , "مشاور" , "معلم " , "اولیا"]
        roles_var = tk.StringVar(self.win) #?
        roles_var.set(roles[0])
        ttk.Label(self.win , text="roles").grid(row=6 , column=0)
        self.role_combobox = ttk.Combobox(self.win, textvariable=roles_var, values=roles, state="readonly")
        self.role_combobox.grid(row=6, column=1, padx=5, pady=5)

        btn = tk.Button(self.win , text="Add User" , command=lambda: user.add_user (
            self.Name.get(),
            self.lastName.get(),
            self.phoneNumber.get(),
            self.password.get(),
            self.userName.get().strip(),
            self.role_combobox.get()
        ))
        btn.grid(row=7, column=1)
        
        # btn1=tk.Button(self.win , text="disable user" , command=lambda:user.disable_user(self.win))
        # btn1.grid(row=8 , column=1)
        
        # btn1=tk.Button(self.win , text="enable user" , command=lambda:user.enable_user(self.win))
        # btn1.grid(row=9 , column=1)

        self.win.mainloop()