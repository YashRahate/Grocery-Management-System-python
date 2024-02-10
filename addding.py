import tkinter as tk
from tkinter import ttk

# Create the main application window
root = tk.Tk()
root.title("Treeview Example")

# Create a Treeview widget
tree = ttk.Treeview(root)

# Define columns
tree["columns"] = ("Name", "Age", "Gender")

# Format column headings
tree.heading("#0", text="ID")
tree.heading("Name", text="Name")
tree.heading("Age", text="Age")
tree.heading("Gender", text="Gender")

# Inserting data into the Treeview
tree.insert("", "end", text="1", values=("John Doe", 30, "Male"))
tree.insert("", "end", text="2", values=("Jane Smith", 25, "Female"))

# Pack the Treeview widget
tree.pack(expand=True, fill="both")

# Run the Tkinter event loop
root.mainloop()
