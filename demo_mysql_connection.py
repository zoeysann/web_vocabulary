import mysql.connector
import csv

def import_words():
        vocabulary=[]
        with open(r"vocabulary_notes.csv", encoding='UTF-8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            for row in csv_reader:
                vocabulary.append([row[0], row[1]])
            return vocabulary

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
# val=import_words()

# for i in val:
#      # i = list[en, az] 
#      mycursor.execute(sql, (i[0], i[1]))

# mydb.commit()

# print(mycursor.rowcount, "was inserted.")
# print("1 record inserted, ID:", mycursor.lastrowid)

mycursor.execute("SELECT * FROM idk_name")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

# sql = "DELETE FROM idk_name WHERE id<5"

# mycursor.execute(sql)

# mydb.commit()

# print(mycursor.rowcount, "record(s) deleted")