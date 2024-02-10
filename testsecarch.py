from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkcalendar import Calendar
import tkinter as tk

mwindow=Tk()
mwindow.title=('Grocery Management System')
mwindow.geometry('1440x750+50+20')
def search():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    query='use crud'
    mycursor.execute(query)
    
    search_term = searche.get()
    if search_term:
        # Clear the current content of the treeview
        query="select * from finaldbt"
        mycursor.execute(query)
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
        # for row in product_table.get_children():
        #     product_table.delete(row)
    
        # Execute SQL query to fetch names matching the search term
        mycursor.execute("SELECT * FROM finaldbt WHERE name LIKE %s", (f'%{search_term}%',))
        
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
            for i in row:
                product_table.insert("",END,values=i)
            con.commit()
        con.close() 
        
        
        # Display results in the treeview
        # for name in names:
        #     product_table.insert("", "end", values=name)
    else:
        
        query="select * from finaldbt"
        mycursor.execute(query)
        row=mycursor.fetchall()
        if len(row)!=0:
            product_table.delete(*product_table.get_children())
            for i in row:
                product_table.insert("",END,values=i)
            con.commit()
        con.close() 
        # If search term is empty, show all names
        
        # mycursor.execute("SELECT * FROM finaldbt")
        # names = mycursor.fetchall()
      
        # for name in names:
        #     product_table.insert("", "end", values=name)

    
    

    
    
def on_vertical_scroll(*args):
    outputframe.yview(*args)

def on_horizontal_scroll(*args):
    outputframe.xview(*args)
    
    
    
def delete_details():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    query="delete from finaldbt where name =%s"
    mycursor.execute(query,name.get())
    con.commit()
    name.delete(0,END)
    w_name.delete(0,END)
    w_contact.delete(0,END)
    cp.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    exd.delete(0,END)
    fetch_data()
    
    con.close()
    
    

def add_details():
    try:
        con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
        mycursor= con.cursor()
    except:
        messagebox.showerror("Error",'Connection Failed With Database')
        return
    query='use crud'
    mycursor.execute(query)
    
    
    query='select * from finaldbt where name=%s'

    mycursor.execute(query,(name.get()))

    row=mycursor.fetchone()
    if row != None:
        messagebox.showerror('Error','Product Already Exist')
    else:
        cp_value = float(cp.get())  
        quan_value = int(quan.get())  
        ctotal = cp_value * quan_value
        sp_value = float(sp.get())  
        quan_value = int(quan.get())  
        stotal = sp_value * quan_value

        
        query='insert into finaldbt(name ,w_name,w_contact,c_price,s_price,quantity,ex_date,c_total,s_total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
        mycursor.execute(query,(name.get(),w_name.get(),w_contact.get(),cp.get(),sp.get(),quan.get(),exd.get(),ctotal,stotal ))
        con.commit()
        fetch_data()
        con.close()
        messagebox.showinfo('Sucsess',' Item Added Successfully')

def fetch_data():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    query="select * from finaldbt"
    mycursor.execute(query)
    row=mycursor.fetchall()
    if len(row)!=0:
        product_table.delete(*product_table.get_children())
        for i in row:
            product_table.insert("",END,values=i)
        con.commit()
    con.close() 
    
    
def get_cursor(event=''):
    update=Button(outputframe1,width=25,pady=7,text='UPDATE',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=update_details)
    update.grid(row=8,column=2)
    
    delete=Button(outputframe1,width=25,pady=7,text='delete',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=delete_details)
    delete.grid(row=8,column=1)
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    cursor_row=product_table.focus()
    content=product_table.item(cursor_row)
    rowss=content["values"]
    name.delete(0,END)
    w_name.delete(0,END)
    w_contact.delete(0,END)
    cp.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    exd.delete(0,END)
    
    
    
    name.insert(0,rowss[0])
    w_name.insert(0,rowss[1])
    w_contact.insert(0,rowss[2])
    cp.insert(0,rowss[3])
    sp.insert(0,rowss[4])
    quan.insert(0,rowss[5])
    exd.insert(0,rowss[9])
    
   
    
    
def update_details():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    query='update finaldbt set w_name=%s,w_contact=%s,c_price=%s,s_price=%s,quantity=%s,ex_date=%s where name=%s'
    mycursor.execute(query,(w_name.get(),w_contact.get(),cp.get(),sp.get(),quan.get(),exd.get(),name.get()))
    con.commit()
    fetch_data()
    con.close()
    
def open_cal():
    select.config(state=tk.DISABLED)
    def get_date():
        selected_date = cal.get_date()
        exd.delete(0,END)
        exd.insert(0,selected_date)
        root.destroy()
        select.config(state=tk.NORMAL)
      
        
    
    # You can do whatever you want with the selected date, such as updating a label or entry field

    root = tk.Tk()
    root.title("Date Picker")

    cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    cal.pack(padx=10, pady=10)

    btn=Button(root, text="Get Date", command=get_date)
    btn.pack(pady=5)
    

    root.mainloop()
      
    
        
    
    
    
    
    

outputframe=Frame(mwindow,bd=10,relief=RIDGE)
outputframe.place(x=0,y=10,width=700,height=650)

outputframe1=Frame(mwindow,bd=10,relief=RIDGE)
outputframe1.place(x=750,y=10,width=600,height=350)
scroll_x=ttk.Scrollbar(outputframe,orient=HORIZONTAL, command=on_vertical_scroll)
scroll_y=ttk.Scrollbar(outputframe,orient=VERTICAL ,command=on_horizontal_scroll)

product_table=ttk.Treeview(outputframe,columns=("NameofProduct","wholesellername","wholesellercontact","costprice","sellingprice","quantity","costpricetotal","sellingpricetotal","discount","exdate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x=ttk.Scrollbar(command=product_table.xview)
scroll_y=ttk.Scrollbar(command=product_table.yview)
product_table.heading("NameofProduct",text="PRODUCT")
product_table.heading("wholesellername",text="WHOLESELLER NAME ")
product_table.heading("wholesellercontact",text="WHOLESELLER CONTACT")
product_table.heading("costprice",text="COST PRICE")
product_table.heading("sellingprice",text="SELLING PRICE")
product_table.heading("quantity",text="QUANTITY") 
product_table.heading("costpricetotal",text="COST PRICE TOTAL") 
product_table.heading("sellingpricetotal",text="SELLING PRICE TOTAL") 
product_table.heading("discount",text="DISCOUNT") 
product_table.heading("exdate",text="EXPIRY DATE") 

product_table["show"]="headings"
product_table.column("NameofProduct",width=100)
product_table.column("wholesellername",width=100)
product_table.column("wholesellercontact",width=100)
product_table.column("costprice",width=75)
product_table.column("sellingprice",width=75)
product_table.column("quantity",width=50)
product_table.column("costpricetotal",width=75)
product_table.column("sellingpricetotal",width=75)
product_table.column("discount",width=50)
product_table.column("exdate",width=75)
product_table.pack(fill=BOTH,expand=1)

product_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()

lb=Label(outputframe1,text='Name of product:',bd=0)
lb.grid(row=0,column=0)
name = Entry(outputframe1,width=30,fg='black',border=2,bg="white",textvariable=1,font=('Microsoft Yahei UI',10))
name.grid(row=0,column=1)



lb1=Label(outputframe1,text='Quantity:')
lb1.grid(row=5,column=0)
quan = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
quan.grid(row=5,column=1)


lb2=Label(outputframe1,text='Cost price:')
lb2.grid(row=3,column=0)
cp = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
cp.grid(row=3,column=1)

lb3=Label(outputframe1,text="Wholesaller's name:")
lb3.grid(row=1,column=0)
w_name = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
w_name.grid(row=1,column=1)

lb4=Label(outputframe1,text="Wholesaller's contact:")
lb4.grid(row=2,column=0)
w_contact = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
w_contact.grid(row=2,column=1)

lb5=Label(outputframe1,text="Selling price:")
lb5.grid(row=4,column=0)
sp = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
sp.grid(row=4,column=1)

lb6=Label(outputframe1,text="Expiry date:")
lb6.grid(row=6,column=0)
exd = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
exd.grid(row=6,column=1)
select=Button(outputframe1,width=10,text='select',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=open_cal)
select.grid(row=6,column=2)



add=Button(outputframe1,width=25,pady=7,text='ADD',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=add_details)
add.grid(row=8,column=0)

searche = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
searche.grid(row=8,column=1)
searchb=Button(outputframe1,width=10,text='SEARCH',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=search)
searchb.grid(row=9,column=2)


mwindow.mainloop()