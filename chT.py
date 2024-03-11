import tkinter as tk
from tkinter import ttk

def sum_column_data():
    total_sum = 0
    # Iterate over all items in the tree
    for item_id in tree.get_children():
        # Get the values of each column for the current item
        values = tree.item(item_id, 'values')
        if values:
            # Iterate over the values
            for value in values:
                # Check if the value is an integer
                try:
                    total_sum += int(value)
                except ValueError:
                    pass  # Ignore if value is not an integer
    # Display the total sum
    result_label.config(text=f"Total Sum: {total_sum}")

# Create the main window
root = tk.Tk()
root.title("Sum of Integer Column Data")

# Create a Treeview widget
tree = ttk.Treeview(root, columns=("Column 1", "Column 2", "Column 3"), show="headings")
tree.pack()

# Insert some sample data (some integers and some non-integers)
tree.insert("", "end", values=("10", "20", "30"))
tree.insert("", "end", values=("40", "50", "60"))
tree.insert("", "end", values=("70", "80", "non-integer"))
tree.insert("", "end", values=("non-integer", "100", "110"))

# Button to calculate the sum of integer column data
sum_button = tk.Button(root, text="Sum Integer Column Data", command=sum_column_data)
sum_button.pack()

# Label to display the result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
