from tkinter import Tk, ttk

def deselect(event=None):
    selected_item = product_table.selection()
    if selected_item:
        product_table.selection_remove(selected_item)

def on_select(event):
    deselect_button.config(state="normal")

def on_click_outside(event):
    # Check if the click occurred outside of the treeview
    if event.widget != product_table:
        deselect()

mwindow = Tk()
mwindow.title('Grocery Management System')
mwindow.geometry('600x400')

product_table = ttk.Treeview(mwindow)
product_table.pack(pady=10, padx=10)

# Insert some sample data into the treeview
for i in range(10):
    product_table.insert("", "end", text=f"Item {i}")

deselect_button = ttk.Button(mwindow, text="Deselect", command=deselect, state="disabled")
deselect_button.pack()

# Bind the select event to call on_select function
product_table.bind("<<TreeviewSelect>>", on_select)

# Bind the click event to call on_click_outside function
mwindow.bind("<Button-1>", on_click_outside)

mwindow.mainloop()
