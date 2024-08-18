import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    password="zoey_464852",
    database="web_vocabulary"
)

mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE idk_name (en VARCHAR(255), az VARCHAR(255))")
# mycursor.execute("ALTER TABLE idk_name ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
# mycursor.execute("SHOW TABLES")

# for i in mycursor:
#     print(i)

# sql="INSERT INTO idk_name (en, az) VALUES (%s, %s)"
# val=[
#     ('Marriage', 'Toy'),
#     ('Entrance', 'Giriş'),
#     ('Existence', 'Mövcud_olma'),
#     ('Accountant', 'Mühasib')
# ]

# mycursor.executemany(sql, val)

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
# print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("SELECT * FROM idk_name")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# sql = "DELETE FROM idk_name WHERE id>4"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")