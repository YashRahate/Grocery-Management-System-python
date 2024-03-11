# from docxtpl import DocxTemplate

# doc = DocxTemplate("invoice_template.docx")


# invoice_list =[[2,"pen",0.5,1],
#                [4,"book",12,3]]

# doc.render({"name":"john","invoice_list":invoice_list})
# doc.save("new_invoice.docx")
import tkinter as tk
from tkinter import ttk

def merge_data(tree, new_data):
    for item in new_data:
        name_of_product = item['name_of_product']
        existing_item = None
        for child in tree.get_children():
            if tree.item(child, 'values')[0] == name_of_product:
                existing_item = child
                break
        if existing_item:
            # Update existing row by summing quantity
            current_quantity = int(tree.item(existing_item, 'values')[1])
            new_quantity = int(item['quantity'])
            total_quantity = current_quantity + new_quantity
            tree.item(existing_item, values=(name_of_product, total_quantity, item['unit_value']))
        else:
            # Insert new row
            tree.insert('', 'end', values=(item['name_of_product'], item['quantity'], item['unit_value']))

# Sample data
new_data = [
    {'name_of_product': 'Apple', 'quantity': 10, 'unit_value': 2},
    {'name_of_product': 'Banana', 'quantity': 5, 'unit_value': 1},
    {'name_of_product': 'Apple', 'quantity': 15, 'unit_value': 2}
]

root = tk.Tk()
tree = ttk.Treeview(root, columns=('name_of_product', 'quantity', 'unit_value'), show='headings')

tree.heading('name_of_product', text='Name of Product')
tree.heading('quantity', text='Quantity')
tree.heading('unit_value', text='Unit Value')

tree.pack()

# Merge new data
merge_data(tree, new_data)

root.mainloop()

