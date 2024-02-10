import tkinter as tk

def on_vertical_scroll(*args):
    canvas.yview(*args)

def on_horizontal_scroll(*args):
    canvas.xview(*args)

root = tk.Tk()
root.title("Scrollbars Example")

# Create a frame to contain the scrollable area
frame = tk.Frame(root)
frame.pack(fill="both", expand=True)

# Create a canvas widget inside the frame for scrollable content
canvas = tk.Canvas(frame)
canvas.pack(side="left", fill="both", expand=True)

# Add vertical scrollbar to the canvas
vertical_scrollbar = tk.Scrollbar(frame, orient="vertical", command=on_vertical_scroll)
vertical_scrollbar.pack(side="right", fill="y")

# Link the scrollbar to the canvas
canvas.configure(yscrollcommand=vertical_scrollbar.set)

# Add horizontal scrollbar to the canvas
horizontal_scrollbar = tk.Scrollbar(frame, orient="horizontal", command=on_horizontal_scroll)
horizontal_scrollbar.pack(side="bottom", fill="x")

# Link the scrollbar to the canvas
canvas.configure(xscrollcommand=horizontal_scrollbar.set)

# Create a frame inside the canvas for the scrollable content
scrollable_frame = tk.Frame(canvas)
canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")

# Add some widgets to the scrollable frame (just for demonstration)
for i in range(50):
    tk.Label(scrollable_frame, text=f"Label {i}").pack()

# Configure the canvas to update scroll region when the frame size changes
scrollable_frame.bind("<Configure>", lambda event: canvas.configure(scrollregion=canvas.bbox("all")))

root.mainloop()

