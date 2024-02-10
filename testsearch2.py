import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector

def search():
    search_term = searche.get()
    if search_term:
        for row in product_table.get_children():
            product_table.delete(row)
        
        cursor.execute("SELECT * FROM finaldbt WHERE name LIKE %s", (f'%{search_term}%',))
        rows = cursor.fetchall()
        
        for row in rows:
            product_table.insert("", "end", values=row)
    else:
        fetch_data()

def fetch_data():
    cursor.execute("SELECT * FROM finaldbt")
    rows = cursor.fetchall()
    for row in rows:
        product_table.insert("", "end", values=row)

def get_cursor(event=''):
    update.config(state=tk.NORMAL)
    delete.config(state=tk.NORMAL)
    cursor_row = product_table.focus()
    content = product_table.item(cursor_row)
    rowss = content["values"]
    name.delete(0, tk.END)
    w_name.delete(0, tk.END)
    w_contact.delete(0, tk.END)
    cp.delete(0, tk.END)
    sp.delete(0, tk.END)
    quan.delete(0, tk.END)
    exd.delete(0, tk.END)

    name.insert(0, rowss[0])
    w_name.insert(0, rowss[1])
    w_contact.insert(0, rowss[2])
    cp.insert(0, rowss[3])
    sp.insert(0, rowss[4])
    quan.insert(0, rowss[5])
    exd.insert(0, rowss[9])

def update_details():
    query = 'UPDATE finaldbt SET w_name = %s, w_contact = %s, c_price = %s, s_price = %s, quantity = %s, ex_date = %s WHERE name = %s'
    cursor.execute(query, (w_name.get(), w_contact.get(), cp.get(), sp.get(), quan.get(), exd.get(), name.get()))
    conn.commit()
    fetch_data()

def delete_details():
    query = 'DELETE FROM finaldbt WHERE name = %s'
    cursor.execute(query, (name.get(),))
    conn.commit()
    fetch_data()
    name.delete(0, tk.END)
    w_name.delete(0, tk.END)
    w_contact.delete(0, tk.END)
    cp.delete(0, tk.END)
    sp.delete(0, tk.END)
    quan.delete(0, tk.END)
    exd.delete(0, tk.END)

mwindow = tk.Tk()
mwindow.title('Grocery Management System')
mwindow.geometry('1440x750+50+20')

outputframe = tk.Frame(mwindow, bd=10, relief=tk.RIDGE)
outputframe.place(x=0, y=10, width=700, height=650)

outputframe1 = tk.Frame(mwindow, bd=10, relief=tk.RIDGE)
outputframe1.place(x=750, y=10, width=600, height=350)

product_table = ttk.Treeview(outputframe, columns=("NameofProduct", "wholesellername", "wholesellercontact", "costprice", "sellingprice", "quantity", "costpricetotal", "sellingpricetotal", "discount", "exdate"))
product_table.heading("NameofProduct", text="PRODUCT")
product_table.heading("wholesellername", text="WHOLESELLER NAME ")
product_table.heading("wholesellercontact", text="WHOLESELLER CONTACT")
product_table.heading("costprice", text="COST PRICE")
product_table.heading("sellingprice", text="SELLING PRICE")
product_table.heading("quantity", text="QUANTITY")
product_table.heading("costpricetotal", text="COST PRICE TOTAL")
product_table.heading("sellingpricetotal", text="SELLING PRICE TOTAL")
product_table.heading("discount", text="DISCOUNT")
product_table.heading("exdate", text="EXPIRY DATE")

product_table["show"] = "headings"
product_table.column("NameofProduct", width=100)
product_table.column("wholesellername", width=100)
product_table.column("wholesellercontact", width=100)
product_table.column("costprice", width=75)
product_table.column("sellingprice", width=75)
product_table.column("quantity", width=50)
product_table.column("costpricetotal", width=75)
product_table.column("sellingpricetotal", width=75)
product_table.column("discount", width=50)
product_table.column("exdate", width=75)
product_table.pack(fill=tk.BOTH, expand=1)

product_table.bind("<ButtonRelease-1>", get_cursor)
fetch_data()

lb = tk.Label(outputframe1, text='Name of product:', bd=0)
lb.grid(row=0, column=0)
name = tk.Entry(outputframe1, width=30, fg='black', border=2, bg="white", textvariable=1, font=('Microsoft Yahei UI', 10))
name.grid(row=0, column=1)

# Add other labels and entries as you have in your code

add = tk.Button(outputframe1, width=25, pady=7, text='ADD', bg='#006666', activebackground='#006666', activeforeground='white', fg='white')
add.grid(row=8, column=0)

searche = tk.Entry(outputframe1, width=30, fg='black', border=2, bg="white", font=('Microsoft Yahei UI', 10))
searche.grid(row=8, column=1)
searchb = tk.Button(outputframe1, width=10, text='SEARCH', bg='#006666', activebackground='#006666', activeforeground='white', fg='white', command=search)
searchb.grid(row=9, column=2)

update = tk.Button(outputframe1, width=25, pady=7, text='UPDATE', bg='#006666', activebackground='#006666', activeforeground='white', fg='white', command=update_details)
update.grid(row=8, column=2)
update.config(state=tk.DISABLED)

delete = tk.Button(outputframe1, width=25, pady=7, text='DELETE', bg='#006666', activebackground='#006666', activeforeground='white', fg='white', command=delete_details)
delete.grid(row=8, column=1)
delete.config(state=tk.DISABLED)

mwindow.mainloop()
