import mysql.connector
import matplotlib.pyplot as plt
from collections import defaultdict

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
mycursor.execute("SELECT date, profit FROM graph")

# Fetch all rows from the result set
result = mycursor.fetchall()

# Create a dictionary to store the sum of 'profit' for each date
date_profit_sum = defaultdict(float)

# Iterate through the result set and calculate the sum of 'profit' for each date
for date, profit in result:
    date_profit_sum[date] += profit

# Convert the dictionary to lists of dates and corresponding sums of 'profit'
dates = list(date_profit_sum.keys())
profit_sums = list(date_profit_sum.values())

# Plot the data
plt.figure(figsize=(10, 6))
plt.plot(dates, profit_sums, marker='o', linestyle='-')
plt.title('Total Profit over Time')
plt.xlabel('Date')
plt.ylabel('Total Profit')
plt.xticks(rotation=45)  # Rotate x-axis labels for better readability
plt.tight_layout()
plt.show()
