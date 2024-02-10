
billing_table=ttk.Treeview(outputframe,columns=("NameofProduct","sellingprice","quantity","sellingpricetotal","discount","exdate"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)

scroll_x.pack(side=BOTTOM,fill=X)
scroll_y.pack(side=RIGHT,fill=Y)

scroll_x=ttk.Scrollbar(command=billing_table.xview)
scroll_y=ttk.Scrollbar(command=billing_table.yview)
billing_table.heading("NameofProduct",text="PRODUCT")
billing_table.heading("sellingprice",text="SELLING PRICE")
billing_table.heading("quantity",text="QUANTITY") 
billing_table.heading("sellingpricetotal",text="SELLING PRICE TOTAL") 
billing_table.heading("discount",text="DISCOUNT") 
billing_table.heading("exdate",text="EXPIRY DATE") 

billing_table["show"]="headings"
billing_table.column("NameofProduct",width=100)
billing_table.column("sellingprice",width=75)
billing_table.column("quantity",width=50)
billing_table.column("sellingpricetotal",width=75)
billing_table.column("discount",width=50)
billing_table.column("exdate",width=75)
billing_table.pack(fill=BOTH,expand=1)

billing_table.bind("<ButtonRelease-1>",get_cursor)
fetch_data()