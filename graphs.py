import tkinter as tk
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import mysql.connector
import matplotlib.pyplot as plt

# Connect to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="travelmanagement",
    database="crud"
)

# Create a cursor object to execute SQL queries
mycursor = mydb.cursor()

# Execute a query to fetch data from the 'graph' table
mycursor.execute("SELECT date, nos FROM graph")

# Fetch all rows from the result set
result = mycursor.fetchall()

# Extract dates and corresponding numbers from the result
dates = [row[0] for row in result]
nos = [row[1] for row in result]

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(dates, nos, marker='o', linestyle='-')
plt.title('Number of NOS over Time')
plt.xlabel('Date')
plt.ylabel('Number of NOS')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
