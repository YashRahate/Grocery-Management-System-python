import tkinter as tk
from tkinter import ttk

def get_row_data_by_value(tree, column, value):
    for item in tree.get_children():
        # Retrieve data from the specified column
        item_data = tree.item(item, 'values')[column]
        if item_data == value:
            # If the value matches, return the data of that row
            return tree.item(item, 'values')

    # Return None if the value is not found
    return None

# Create Tkinter window
root = tk.Tk()
root.title("Treeview Row Data by Value Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("ID", "Name", "Age"))

# Insert some sample data
tree.insert("", "end", values=("1", "John", 30))
tree.insert("", "end", values=("2", "Alice", 25))
tree.insert("", "end", values=("3", "Bob", 35))

# Pack the Treeview widget
tree.pack()

# Define the value you want to search for
search_value = "Alice"

# Get the row data containing the search value
row_data = get_row_data_by_value(tree, 1, search_value)

# Print only the value "Alice"
if row_data:
    print(row_data[1])  # Index 1 corresponds to the "Name" column

root.mainloop()

