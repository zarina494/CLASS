import sqlite3

connection = sqlite3.connect('test.db')
cursor = connection.cursor()

# cursor.execute("""CREATE TABLE Students(
#                name varcha(50) NOT NULL,
#                last_name varchar(50),
#                phone int )""")

# cursor.execute("INSERT INTO Students(name,last_name,phone) VALUES ('zarina','sadykova',1234567)")
# cursor.execute("INSERT INTO Students(name,last_name,phone) VALUES ('nazira','p',1234567)")
# cursor.execute("INSERT INTO Students(name,last_name,phone) VALUES ('baizak','mol',3456789)")
# cursor.execute("INSERT INTO Students(name,last_name,phone) VALUES ('meerim','nov',22345678)")



# cursor.execute("DELETE FROM Students WHERE salary<=2000")
# cursor.execute("SELECT name,salary FROM Students WHERE salary>=1000")
# cursor.execute("SELECT * FROM Students")
# cursor.execute("ALTER TABLE Students ADD salary int")
# cursor.execute("AlTER TABLE Students ADD job int")
# cursor.execute("UPDATE Students SET job='engineer' WHERE name='baizak'")
# cursor.execute("UPDATE STUDENTS SET phone=22345678 WHERE name='baizak'")
#        cursor.execute("UPDATE Students SET salary=7000 WHERE name='baizak'")
# cursor.execute("DELETE FROM Students WHERE name='meerim'")
print(cursor.fetchall())



connection.commit()
