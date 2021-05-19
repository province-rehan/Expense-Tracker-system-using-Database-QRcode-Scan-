
from tkinter import ttk
import tkinter as tk
import sqlite3





root = tk.Tk()

root.title("python Project")



def init():
   connection = sqlite3.connect('sqlite_data01.db')


   cursor = connection.cursor()



   cursor.execute('create table  expenses (iid int,amount number,category string,date string)')

   connection.commit()


def new(id, amount: int, category: str):
   from datetime import datetime
   date = str(datetime.now())


   connection = sqlite3.connect('sqlite_data01.db')
   cursor = connection.cursor()
   sql = '''
       insert into expenses values (

            {},
            '{}',
           '{}',
           '{}'
           )
       '''.format(id, amount, category, date)
   cursor.execute(sql)

   connection.commit()


def view(iid: int):
   connection = sqlite3.connect('sqlite_data01.db')
   cursor = connection.cursor()
   if iid:

       sql = '''
       select * from expenses where iid = '{}'
       '''.format(iid)
       sql1 = '''
        select sum(amount) from expenses where iid = '{}'
       '''.format(iid)

   else:
       sql = '''
               select * from expenses
               '''.format(iid)
       sql1 = '''
               select sum(amount) from expenses
               '''.format(iid)
   cursor.execute(sql)

   rows = cursor.fetchall()
   for row in rows:

       print(row)

       tree.insert("", tk.END, values=row)


   cursor.execute(sql1)
   connection.commit()

   connection.close()

   return rows





#init()

#new(1001,50,'soap')
#new(1002,100,'Burger')



while True:
   print("1.Add item")
   print("2.display item")
   print("3.EXIT")
   print("\n")
   nn = int(input("Which platform You want to go :"))
   if nn == 1:
       nu = int(input("How many products :"))

       for i in range(nu):
           p_ident = int(input("Product id :"))
           p_amou = int(input("Product price :"))
           p_na = input("Product Name :")
           new(p_ident, p_amou, p_na)
       print("\n")
       print("products are saved")




   if nn == 2:
       file1 = open("myfile1.txt", "r")

       ab = file1.readlines()

       for i in ab:
           dataa = int(i)

       file1.close()

       tree = ttk.Treeview(root, column=("c1", "c2", "c3", "c4"), show='headings')

       tree.column("#1", anchor=tk.CENTER)

       tree.heading("#1", text="Product ID")

       tree.column("#2", anchor=tk.CENTER)

       tree.heading("#2", text="Product Amount")

       tree.column("#3", anchor=tk.CENTER)

       tree.heading("#3", text="Product NAME")

       tree.column("#4", anchor=tk.CENTER)

       tree.heading("#4", text="Time")
       tree.pack()

       button1 = tk.Button(text="Display data", command=lambda: view(dataa))

       button1.pack(pady=10)

       root.mainloop()

   if nn == 3:
       break



#view(data11)


