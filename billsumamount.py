# # import tkinter as tk
# # from tkinter import ttk

# # def sum_column_data(tree, column):
# #     total = 0
# #     for item in tree.get_children():
# #         # Retrieve data from the desired column
# #         item_data = tree.item(item, 'values')[column]
# #         # Convert the data to a numeric type and add it to the total
# #         total += int(item_data)
# #     return total

# # # Create Tkinter window
# # root = tk.Tk()
# # root.title("Treeview Column Sum Example")

# # # Create a Treeview widget
# # tree = ttk.Treeview(root, columns=("Name", "Quantity"))

# # # Insert some sample data
# # tree.insert("", "end", values=("Item 1", 10))
# # tree.insert("", "end", values=("Item 2", 15))
# # tree.insert("", "end", values=("Item 3", 20))

# # # Pack the Treeview widget
# # tree.pack()

# # # Define the index of the column you want to sum
# # column_index = 1  # Assuming the Quantity column is the second column (index 1)

# # # Button to calculate column sum
# # button = tk.Button(root, text="Calculate Column Sum",
# #                    command=lambda: print("Sum of Quantity column:", sum_column_data(tree, column_index)))
# # button.pack()

# # root.mainloop()
# import tkinter as tk
# from tkinter import ttk

# def total_sum(tree, column):
#     total = 0.0  # Initialize total as a float
#     for item in tree.get_children():
#         item_data = tree.item(item, 'values')[column]
#         try:
#             total += float(item_data)
#         except ValueError:
#             print(f"Warning: Invalid value '{item_data}' in column {column + 1}. Skipping.")
#     return total

# # Create Tkinter window
# root = tk.Tk()
# root.title("Billing Table")

# # Create a frame for the Treeview and scrollbars
# outputframe2 = tk.Frame(root)
# outputframe2.pack(fill=tk.BOTH, expand=True)

# # Create Treeview widget
# billing_table = ttk.Treeview(outputframe2, columns=("NameofProduct", "sellingprice", "quantity", "discount", "exdate", "total"))

# # Create scrollbars
# scroll_x = ttk.Scrollbar(outputframe2, orient=tk.HORIZONTAL, command=billing_table.xview)
# scroll_y = ttk.Scrollbar(outputframe2, orient=tk.VERTICAL, command=billing_table.yview)
# scroll_x.pack(side=tk.BOTTOM, fill=tk.X)
# scroll_y.pack(side=tk.RIGHT, fill=tk.Y)

# # Set scrollbar commands for the Treeview
# billing_table.configure(xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

# # Define headings and column widths
# billing_table.heading("NameofProduct", text="PRODUCT")
# billing_table.heading("sellingprice", text="SELLING PRICE")
# billing_table.heading("quantity", text="QUANTITY")
# billing_table.heading("total", text="TOTAL")
# billing_table.heading("discount", text="DISCOUNT")
# billing_table.heading("exdate", text="EXPIRY DATE")
# billing_table["show"] = "headings"
# billing_table.column("NameofProduct", width=100)
# billing_table.column("sellingprice", width=75)
# billing_table.column("quantity", width=50)
# billing_table.column("total", width=75)
# billing_table.column("discount", width=50)
# billing_table.column("exdate", width=75)

# billing_table.pack(fill=tk.BOTH, expand=True)

# # Function to calculate and display the total sum as a float
# def calculate_total():
#     total = total_sum(billing_table, 5)  # Assuming "total" column is at index 5
#     print("Sum of Total column:", total)

# # Create a button to calculate the total sum
# calculate_button = tk.Button(root, text="Calculate Total", command=calculate_total)
# calculate_button.pack()

# root.mainloop()
# import tkinter as tk
# from tkinter import ttk

# def get_tree_data(tree):
#     data = []
#     for item in tree.get_children():
#         values = tree.item(item, 'values')
#         data.append(values)
#     return data

# def main():
#     root = tk.Tk()
#     tree = ttk.Treeview(root)
#     tree['columns'] = ('name', 'age')

#     tree.heading('#0', text='ID')
#     tree.heading('name', text='Name')
#     tree.heading('age', text='Age')

#     # Insert some dummy data
#     for i in range(1, 6):
#         tree.insert('', 'end', text=str(i), values=('Person ' + str(i), 20 + i))

#     tree.pack()

#     def print_tree_data():
#         data = get_tree_data(tree)
#         print("Data in tree:", data)

#     button = tk.Button(root, text="Print Tree Data", command=print_tree_data)
#     button.pack()

#     root.mainloop()

# if __name__ == "__main__":
#     main()

import tkinter as tk
from tkinter import ttk

def get_tree_data(tree):
    data = []
    for item in tree.get_children():
        values = tree.item(item, 'values')
        data.append(values)
    return data

def print_tree_data():
    data = get_tree_data(tree)
    print("Data in tree:", data)

root = tk.Tk()
tree = ttk.Treeview(root)
tree['columns'] = ('name', 'age')

tree.heading('#0', text='ID')
tree.heading('name', text='Name')
tree.heading('age', text='Age')

# Insert some dummy data
for i in range(1, 6):
    tree.insert('', 'end', text=str(i), values=('Person ' + str(i), 20 + i))

tree.pack()

button = tk.Button(root, text="Print Tree Data", command=print_tree_data)
button.pack()

root.mainloop()

import tkinter as tk
from tkinter import ttk

def get_tree_data(tree):
    data = []
    for item in tree.get_children():
        values = tree.item(item, 'values')
        data.append(list(values))
    return data

def print_tree_data():
    data = get_tree_data(tree)
    print("Data in tree:", data)

root = tk.Tk()
tree = ttk.Treeview(root)
tree['columns'] = ('name', 'age')

tree.heading('#0', text='ID')
tree.heading('name', text='Name')
tree.heading('age', text='Age')

# Insert some dummy data
for i in range(1, 6):
    tree.insert('', 'end', text=str(i), values=('Person ' + str(i), 20 + i))

tree.pack()

button = tk.Button(root, text="Print Tree Data", command=print_tree_data)
button.pack()

root.mainloop()