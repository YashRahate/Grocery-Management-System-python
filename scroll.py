import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.title("Treeview with Scrollbar")

# Create a Treeview widget with a scrollbar
tree = ttk.Treeview(root)
tree['columns'] = ('Name', 'Age')

# Define column headings
tree.heading('#0', text='ID')
tree.heading('Name', text='Name')
tree.heading('Age', text='Age')

# Insert some dummy data
for i in range(50):
    tree.insert('', 'end', text=str(i), values=('Person '+str(i), i+20))

# Create a vertical scrollbar
vsb = ttk.Scrollbar(root, orient="vertical", command=tree.yview)
vsb.pack(side="right", fill="y")
tree.configure(yscrollcommand=vsb.set)

# Pack the treeview widget
tree.pack(expand=True, fill='both')

root.mainloop()
