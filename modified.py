import datetime
from tkinter import *
from tkinter import messagebox
from tkinter import ttk
from PIL import Image,ImageTk
import pymysql
from tkcalendar import Calendar
import tkinter as tk
from docxtpl import DocxTemplate

mwindow=Tk()
mwindow.title=('Grocery Management System')
mwindow.geometry('1440x750+50+20')

    
    
def merge_billing_data():
    merged_data = {}
    for item in billing_table.get_children():
        values = billing_table.item(item, 'values')
        name_of_product = values[0]
        quantity = int(values[2])
        if name_of_product in merged_data:
            merged_data[name_of_product]['quantity'] += quantity
        else:
            merged_data[name_of_product] = {
                'name_of_product': name_of_product,
                'sellingprice': values[1],
                'quantity': quantity,
                'discount': values[3],
                'exdate': values[4],
                'total': values[5]
            }
    
    # Clear existing data in billing table
    for item in billing_table.get_children():
        billing_table.delete(item)
        
    
    # Insert merged data into billing table
    for data in merged_data.values():
        billing_table.insert('', 'end', values=(
            data['name_of_product'],
            data['sellingprice'],
            data['quantity'],
            data['discount'],
            data['exdate'],
            data['total']
        ))

def on_vertical_scroll(*args):
    outputframe.yview(*args)

def on_horizontal_scroll(*args):
    outputframe.xview(*args)

def sell_detail():   
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    for row in billing_table.get_children():
        # Extract data from the treeview
        name_of_product = billing_table.item(row)['values'][0]
        query="select quantity from finaldbt where name=%s"
        mycursor.execute(query,name_of_product)
        pquantity=mycursor.fetchone()
        quantint1=int(pquantity[0])
        
        quantity = billing_table.item(row)['values'][2]
        quantint2=int(quantity)
        finalquantity=quantint1-quantint2
        # Execute SQL update statement
        sql = "UPDATE finaldbt SET quantity = %s WHERE name = %s"
        val = (finalquantity, name_of_product)
        mycursor.execute(sql, val)

    con.commit()    
    fetch_data()    
    con.close()
    messagebox.showinfo('Sucsess',' Product SOLD')
    clear_entryfield
    for item in billing_table.get_children():
        billing_table.delete(item)
    
    
    
    
def delete_details():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
        # Get the currently selected item
    selected_item = billing_table.focus()

    # Delete the selected item
    if selected_item:
        billing_table.delete(selected_item)
    
    # query="delete from finaldbt where name =%s"
    # mycursor.execute(query,name.get())
    # con.commit()
    # name.delete(0,END)
    # w_name.delete(0,END)
    # w_contact.delete(0,END)
    # cp.delete(0,END)
    # sp.delete(0,END)
    # quan.delete(0,END)
    # exd.delete(0,END)
    # fetch_data()
    
    # con.close()
# def get_tree_data(tree):
#     data = []
#     for item in tree.get_children():
#         values = tree.item(item, 'values')
#         data.append(list(values))
#     return data

# def print_tree_data():
#     data = get_tree_data(billing_table)

    
    
def generate_invoice():
    if c_contacte.get()=='' or c_namee.get()=="":
        messagebox.showerror("Error",'Please Enter The Name and Contact of the Customer')
        return
    
    doc = DocxTemplate("miniproject.docx")
    i_name= c_namee.get()
    i_contact= c_contacte.get()
    data = []
    for item in billing_table.get_children():
        values = billing_table.item(item, 'values')
        data.append(list(values))
    # Assuming item[5] contains string representations of numbers
    subtotal = sum(float(item[5]) for item in data)

    salestax = 0.18   #18%
    subttotal = subtotal * (1 + salestax)
    doc.render({"name":i_name,
                "phone":i_contact,
                "invoice_list":data,
                "subtotal":subtotal,
                "salestax":"18%",
                "total":subttotal})

    doc_name = "new_invoice" + str(name) + datetime.datetime.now().strftime("%Y-%m-%d-%H%M%S") + ".docx"

    doc.save(doc_name)
    
    messagebox.showinfo("Invoice Complete", "Invoice Complete")

    data.clear
        
def clear_entryfield():
    quan.delete(0,END)
    name.delete(0,END)
    stotal.delete(0,END)
    sp.delete(0,END)
    exd.delete(0,END)
    updatequantity.delete(0,END)
        

def add_details():
    try:
        con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
        mycursor= con.cursor()
    except:
        messagebox.showerror("Error",'Connection Failed With Database')
        return
    query='use crud'
    mycursor.execute(query)
    

    if quan.get()=='':
        messagebox.showerror("Error",'Please Enter The Quantity')
        return
    
    namev=name.get()
    
    quantityv=quan.get()
    query="select quantity from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    quantityq=mycursor.fetchone()
    quantint=int(quantityq[0])
    quantinte=int(quantityv)
 
    
    if quantint < quantinte :
        messagebox.showerror('Error','NOT ENOUGH STOCK(REENTER QUANTITY)')
        return
    query="select discount from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    discountv=mycursor.fetchone()
    
  
    sellingp=sp.get()
    query="select ex_date from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    date=mycursor.fetchone()
    total=float(quantityv) * float(sellingp)
    

    # for i in sellingp:
    #     product_table.insert("",END,values=i)
    con.commit()
    
    
    
    # name_of_product = name.get()
    # selling_price = sp.get()
    # quantity = quan.get()
    # discount = ""  # Not sure where you get discount value from
    # expiry_date = exd.get()
    # total = float(selling_price) * int(quantity)
    
    # Check if the product already exists in billing table
    for item in billing_table.get_children():
        values = billing_table.item(item, 'values')
        if values[0] == namev:
            # Update quantity and total
            new_quantity = int(values[2]) + int(quantinte)
            if quantint < new_quantity :
                messagebox.showerror('Error','NOT ENOUGH STOCK(REENTER QUANTITY)')
                return
            new_total = float(values[5]) + total
            billing_table.item(item, values=(values[0], values[1], new_quantity, values[3], values[4], new_total))
            break
    else:
        # Insert new row
        billing_table.insert('', 'end', values=(namev, sellingp, quantityv, discountv, date, total))
    
    # Merge data to combine rows with the same product name
    merge_billing_data()
    
    # Clear entry fields
    clear_entryfield()
   
   
   
   
    # billing_table.insert("", "end", values=(namev,sellingp,quantityv,discountv,date,total))
    product_table.selection_remove(product_table.selection())
    
    clear_entryfield()
    # query='select * from finaldbt where name=%s'

    # mycursor.execute(query,(name.get()))

    # row=mycursor.fetchone()
    # if row != None:
    #     messagebox.showerror('Error','Product Already Exist')
    # else:
    #     cp_value = float(cp.get())  
    #     quan_value = int(quan.get())  
    #     ctotal = cp_value * quan_value
    #     sp_value = float(sp.get())  
    #     quan_value = int(quan.get())  
    #     stotal = sp_value * quan_value

        
    #     query='insert into finaldbt(name ,w_name,w_contact,c_price,s_price,quantity,ex_date,c_total,s_total) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)'
    #     mycursor.execute(query,(name.get(),w_name.get(),w_contact.get(),cp.get(),sp.get(),quan.get(),exd.get(),ctotal,stotal ))
    #     con.commit()
    #     fetch_data()
    #     con.close()
    #     messagebox.showinfo('Sucsess',' Item Added Successfully')



    

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
def fetch_data():

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    query="select name,s_price,quantity,s_total,discount,ex_date from finaldbt"
    mycursor.execute(query)
    row=mycursor.fetchall()
    
    if len(row)!=0:
        product_table.delete(*product_table.get_children())
        for i in row:
            product_table.insert("",END,values=i)
        con.commit()
        
    con.close() 
    
    
def get_cursor(event=''):

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    cursor_row=product_table.focus()
    content=product_table.item(cursor_row)
    rowss=content["values"]
    name.delete(0,END)
    # w_name.delete(0,END)
    # w_contact.delete(0,END)
    # cp.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    stotal.delete(0,END)
    exd.delete(0,END)
    
    
    
    name.insert(0,rowss[0])
    # w_name.insert(0,rowss[1])
    # w_contact.insert(0,rowss[2])
    # cp.insert(0,rowss[3])
    sp.insert(0,rowss[1])
    quan.insert(0,rowss[2])
    quan.delete(0,END)
    stotal.insert(0,rowss[3])
    exd.insert(0,rowss[5])

def get_cursor2(event=''):

    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
    cursor_row=billing_table.focus()
    content=billing_table.item(cursor_row)
    rowss=content["values"]
    name.delete(0,END)
    # w_name.delete(0,END)
    # w_contact.delete(0,END)
    # cp.delete(0,END)
    sp.delete(0,END)
    quan.delete(0,END)
    stotal.delete(0,END)
    exd.delete(0,END)
    
    
    
    name.insert(0,rowss[0])
    # w_name.insert(0,rowss[1])
    # w_contact.insert(0,rowss[2])
    # cp.insert(0,rowss[3])
    sp.insert(0,rowss[1])
    quan.insert(0,rowss[2])
   
    stotal.insert(0,rowss[5])
    exd.insert(0,rowss[4])  
   
    

    
def update_details():
    con=pymysql.connect(host='localhost',user='root',password='travelmanagement')
    mycursor= con.cursor()
    
    query='use crud'
    mycursor.execute(query)
    
        # Get the currently selected item
    selected_item = billing_table.focus()
    
    query="select discount from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    discountv=mycursor.fetchone()
    
    if updatequantity.get()=='':
        messagebox.showerror("Error",'Please Enter The Quantity')
        return
    namev=name.get()
    
    quantityv=updatequantity.get()
    query="select quantity from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    quantityq=mycursor.fetchone()
    quantint=int(quantityq[0])
    quantinte=int(quantityv)
 
    
    if quantint < quantinte :
        messagebox.showerror('Error','NOT ENOUGH STOCK(REENTER QUANTITY)')
        return
    query="select discount from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    discountv=mycursor.fetchone()
    
  
    sellingp=sp.get()
    query="select ex_date from finaldbt where name=%s"
    mycursor.execute(query,name.get())
    date=mycursor.fetchone()
    total=float(quantityv) * float(sellingp)
 
    # Update the values of the selected item
    if selected_item:
        billing_table.item(selected_item, values=(namev, sp.get(), updatequantity.get(),discountv,date,total))
    billing_table.selection_remove(billing_table.selection())
    
    clear_entryfield() 
    
    # query='update finaldbt set w_name=%s,w_contact=%s,c_price=%s,s_price=%s,quantity=%s,ex_date=%s where name=%s'
    # mycursor.execute(query,(w_name.get(),w_contact.get(),cp.get(),sp.get(),quan.get(),exd.get(),name.get()))
    # con.commit()
    # fetch_data()
    # con.close()
    
# def open_cal():
#     select.config(state=tk.DISABLED)
#     def get_date():
#         selected_date = cal.get_date()
#         exd.delete(0,END)
#         exd.insert(0,selected_date)
#         root.destroy()
#         select.config(state=tk.NORMAL)
      
        
    
    # You can do whatever you want with the selected date, such as updating a label or entry field

    # root = tk.Tk()
    # root.title("Date Picker")

    # cal = Calendar(root, selectmode="day", date_pattern="yyyy-mm-dd")
    # cal.pack(padx=10, pady=10)

    # btn=Button(root, text="Get Date", command=get_date)
    # btn.pack(pady=5)
    

    # root.mainloop()
      
    
        
    
    
    
    
    
head=Label(mwindow,text="BILLING SECTION")
head.place(x=720,y=0)
head1=Label(mwindow,text="SELECT PRODUCTS TO BE SOLD")
head1.place(x=100,y=30)
outputframe=Frame(mwindow,bd=10,relief=RIDGE)
outputframe.place(x=20,y=50,width=1400,height=200)
head2=Label(mwindow,text="SEARCH : ")
head2.place(x=20,y=265)
searche = Entry(mwindow,width=48,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
searche.place(x=100,y=265)
searchb=Button(mwindow,width=10,text='SEARCH',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=search)
searchb.place(x=500,y=265)


outputframe1=Frame(mwindow,bd=10,relief=GROOVE)
outputframe1.place(x=700,y=265,width=600,height=100)
outputframe2=Frame(mwindow,bd=10,relief=RIDGE)
outputframe2.place(x=20,y=400,width=1400,height=200)
outputframe3=Frame(mwindow,bd=4,relief=RIDGE,pady=6)
outputframe3.place(x=800,y=620,height=80,width=400)


c_namel=Label(outputframe3,text='Name of customer:',bd=0)
c_namel.grid(row=0,column=0,padx=20)
c_namee = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
c_namee.grid(row=0,column=1)

c_contactl=Label(outputframe3,text='Customer contact:',bd=0)
c_contactl.grid(row=1,column=0,padx=20)
c_contacte = Entry(outputframe3,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
c_contacte.grid(row=1,column=1)


scroll_x=ttk.Scrollbar(outputframe,orient=HORIZONTAL, command=on_vertical_scroll)
scroll_y=ttk.Scrollbar(outputframe,orient=VERTICAL ,command=on_horizontal_scroll)
scroll_x2=ttk.Scrollbar(outputframe2,orient=HORIZONTAL, command=on_vertical_scroll)
scroll_y2=ttk.Scrollbar(outputframe2,orient=VERTICAL ,command=on_horizontal_scroll)
scroll_x2.pack(side=BOTTOM,fill=X)
scroll_y2.pack(side=RIGHT,fill=Y)
product_table=ttk.Treeview(outputframe,columns=("name_of_product","sellingprice","quantity","sellingpricetotal","discount","exdate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x=ttk.Scrollbar(command=product_table.xview)
scroll_y=ttk.Scrollbar(command=product_table.yview)
product_table.heading("name_of_product",text="PRODUCT")
product_table.heading("sellingprice",text="SELLING PRICE")
product_table.heading("quantity",text="QUANTITY") 
product_table.heading("sellingpricetotal",text="SELLING PRICE TOTAL") 
product_table.heading("discount",text="DISCOUNT") 
product_table.heading("exdate",text="EXPIRY DATE") 

product_table["show"]="headings"
product_table.column("name_of_product",width=100)
product_table.column("sellingprice",width=75)
product_table.column("quantity",width=50)
product_table.column("sellingpricetotal",width=75)
product_table.column("discount",width=50)
product_table.column("exdate",width=75)
product_table.pack(fill=BOTH,expand=1)

product_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()

lb=Label(outputframe1,text='Name of product:',bd=0)
lb.grid(row=0,column=0,padx=20)
name = Entry(outputframe1,width=15,fg='black',border=2,bg="white",textvariable=1,font=('Microsoft Yahei UI',10))
name.grid(row=0,column=1)



lb1=Label(outputframe1,text='Quantity:')
lb1.grid(row=0,column=2)
quan = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
quan.grid(row=0,column=3)


# lb2=Label(outputframe1,text='Cost price:')
# lb2.grid(row=3,column=0)
# cp = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
# cp.grid(row=3,column=1)

# lb3=Label(outputframe1,text="Wholesaller's name:")
# lb3.grid(row=1,column=0)
# w_name = Entry(outputframe1,width=30,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
# w_name.grid(row=1,column=1)

lb4=Label(outputframe1,text="Total amount")
lb4.grid(row=1,column=2,padx=20)
stotal = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
stotal.grid(row=1,column=3)

lb5=Label(outputframe1,text="Selling price:")
lb5.grid(row=1,column=0)
sp = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
sp.grid(row=1,column=1)

lb6=Label(outputframe1,text="Expiry date:")
lb6.grid(row=2,column=0)
exd = Entry(outputframe1,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
exd.grid(row=2,column=1)
# select=Button(outputframe1,width=10,text='select',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=open_cal)
# select.grid(row=4,column=2)
add=Button(outputframe1,width=20,padx=12,pady=0,text='ADD',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=add_details)
#add.grid(row=2,column=2,padx=25)
add.place(x=300,y=52)






update=Button(mwindow,width=15,pady=7,text='UPDATE',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=update_details)
update.place(x=50,y=610)
updatequantity=Entry(mwindow,width=15,fg='black',border=2,bg="white",font=('Microsoft Yahei UI',10))
updatequantity.place(x=180,y=620)
delete=Button(mwindow,width=15,pady=7,text='delete',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=delete_details)
delete.place(x=325,y=610)



print=Button(mwindow,width=15,pady=7,text='print',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=generate_invoice)
print.place(x=1237,y=630)

billing_table=ttk.Treeview(outputframe2,columns=("name_of_product","sellingprice","quantity","discount","exdate","total"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x=ttk.Scrollbar(command=billing_table.xview)
scroll_y=ttk.Scrollbar(command=billing_table.yview)

scroll_x2.pack(side=BOTTOM,fill=X)
scroll_y2.pack(side=RIGHT,fill=Y)

scroll_x2=ttk.Scrollbar(command=billing_table.xview)
scroll_y2=ttk.Scrollbar(command=billing_table.yview)

billing_table.heading("name_of_product",text="PRODUCT")
billing_table.heading("sellingprice",text="SELLING PRICE")
billing_table.heading("quantity",text="QUANTITY") 
billing_table.heading("total",text="TOTAL") 
billing_table.heading("discount",text="DISCOUNT") 
billing_table.heading("exdate",text="EXPIRY DATE") 

billing_table["show"]="headings"
billing_table.column("name_of_product",width=100)
billing_table.column("sellingprice",width=75)
billing_table.column("quantity",width=50)
billing_table.column("total",width=75)
billing_table.column("discount",width=50)
billing_table.column("exdate",width=75)
billing_table.pack(fill=BOTH,expand=1)

billing_table.bind("<ButtonRelease-1>",get_cursor2)
fetch_data()


# grandtotal=Button(mwindow,width=15,pady=7,text='Total',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=total_sum(billing_table,column_index))
# grandtotal.place(x=1200,y=610)

sell=Button(mwindow,width=15,pady=7,text='sell',bg='#006666',activebackground='#006666',activeforeground='white',fg='white',command=sell_detail)
sell.place(x=1237,y=670)
#add new invoice button and solve the glich of entry fields

mwindow.mainloop()
