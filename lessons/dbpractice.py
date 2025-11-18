# Database Practice 
import sqlite3

# Connection allows us to conntect 
# python to a SQL database
connection = sqlite3.connect("./database.db") # period says from my location, / target (relative pathways)
# cursor allows us to interact with the SQL DB
cursor = connection.cursor()

query = """
SELECT product_name, price FROM Products;
"""

result = cursor.execute(query).fetchall()
print(f"Our SQL Results: {result}")

# BOTTOM/END OF OUR CODE
connection.commit() # commits our changes 
connection.close() # this disconnect our connection