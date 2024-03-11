import tkinter as tk
from tkinter import ttk

def get_row_data(tree, unique_key):
    for item in tree.get_children():
        # Retrieve data from the first column (assuming it contains the unique key)
        item_data = tree.item(item, 'values')[0]
        if item_data == unique_key:
            # If the unique key matches, return the data of that row
            return tree.item(item, 'values')

    # Return None if the unique key is not found
    return None

# Create Tkinter window
root = tk.Tk()
root.title("Treeview Row Data Example")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("ID", "Name", "Age"))

# Insert some sample data
tree.insert("", "end", values=("1", "John", 30))
tree.insert("", "end", values=("2", "Alice", 25))
tree.insert("", "end", values=("3", "Bob", 35))

# Pack the Treeview widget
tree.pack()

# Define the unique key you want to search for
unique_key = "2"  # Change this to the desired unique key

# Button to get row data based on the unique key
button = tk.Button(root, text="Get Row Data",
                   command=lambda: print(get_row_data(tree, unique_key)))
button.pack()

root.mainloop()
