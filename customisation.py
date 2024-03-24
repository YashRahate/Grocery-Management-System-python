# import tkinter as tk
# from tkinter import ttk

# def get_input():
#     user_input = entry.get()
#     print("User input:", user_input)

# # Create the main window
# root = tk.Tk()
# root.title("Customized Entry Field Example")

# # Customize Entry Field
# entry_style = {
#     "width": 30,
#     "font": ("Helvetica", 12),
#     "borderwidth": 3,
#     "relief": "solid",
#     "highlightbackground": "green",  # Highlight color when selected
#     "highlightcolor": "blue",  # Highlight color when active
#     "highlightthickness": 2,  # Highlight thickness
# }
# entry = ttk.Entry(root, **entry_style)
# entry.pack(pady=10)  # Add padding

# # Customize Button
# button_style = {
#     "text": "Get Input",
#     "command": get_input,
#     "style": "Custom.TButton",
# }
# style = ttk.Style()
# style.configure("Custom.TButton", foreground="#FFFFFF", background="#FF5733", font=("Helvetica", 10, "bold"), padding=(10, 8))
# button = ttk.Button(root, **button_style)
# button.pack()

# # Start the GUI event loop
# root.mainloop()

# import tkinter as tk

# def get_input():
#     user_input = entry.get()
#     print("User input:", user_input)

# # Create the main window
# root = tk.Tk()
# root.title("Customized Entry Field Example")

# # Customize Entry Field
# entry = tk.Entry(root, width=30, font=("Helvetica", 12), bd=3, relief=tk.SOLID, highlightbackground="green", highlightcolor="blue", highlightthickness=2)
# entry.pack(pady=10)  # Add padding

# # Customize Button
# button = tk.Button(root, text="Get Input", command=get_input, bg="#FF5733", fg="#FFFFFF", font=("Helvetica", 10, "bold"), bd=0, relief=tk.FLAT, activebackground="#FFC300", activeforeground="#000000", padx=20, pady=8)
# button.pack()

# # Start the GUI event loop
# root.mainloop()
import tkinter as tk
from tkinter import ttk

def get_input():
    user_input = entry.get()
    print("User input:", user_input)

# Create the main window
root = tk.Tk()
root.title("Customized Entry Field Example")

# Customize Entry Field
style = ttk.Style()
style.configure("CustomEntry.TEntry", borderwidth=3, relief="solid", font=("Helvetica", 12), highlightbackground="green", highlightcolor="blue", highlightthickness=2)
entry = ttk.Entry(root, style="CustomEntry.TEntry", width=30)
entry.pack(pady=10)  # Add padding

# Customize Button
button = tk.Button(root, text="Get Input", command=get_input, bg="#FF5733", fg="#FFFFFF", font=("Helvetica", 10, "bold"), bd=0, relief=tk.FLAT, activebackground="#FFC300", activeforeground="#000000", padx=20, pady=8)
button.pack()

# Start the GUI event loop
root.mainloop()
