import sqlite3
import csv

def createTables():
	conn = sqlite3.connect("employee.sl3")

	cursor = conn.cursor()

	cursor.execute('''CREATE TABLE employees(id INTEGER PRIMARY KEY,
		name VARCHAR(256),
		email VARCHAR(256),
		country VARCHAR(45)
		)''')

	cursor.execute('''CREATE TABLE phonenumber(id INTEGER PRIMARY KEY,
		phonenum VARCHAR(12),
		type VARCHAR(20),
		employeesid INTEGER,
		FOREIGN KEY (employeesid) REFERENCES employees(id)
		)''')

	conn.commit()

	conn.close()

# createTables()

conn = sqlite3.connect("employee.sl3")

cursor = conn.cursor()

with open("employees.csv", newline='') as csvfile:
	reader = csv.reader(csvfile)
	next(reader)
	for row in reader:
		cursor.execute('''INSERT INTO employees(name, email, country)
			VALUES (?,?,?)''', ( row[0] , row[4] , row[5] ) )
		foreign = cursor.lastrowid

		#home phone numbers
		cursor.execute('''INSERT INTO phonenumber(phonenum,type,employeesid)
			VALUES (?,?,?)''', ( row[2] , "home" , foreign ) )

		#cell phone numbers
		cursor.execute('''INSERT INTO phonenumber(phonenum, type, employeesid)
			VALUES (?,?,?)''', ( row[1] , "cell" , foreign ) )

		#work phone numbers
		cursor.execute('''INSERT INTO phonenumber(phonenum, type, employeesid)
			VALUES (?,?,?)''', ( row[3] , "work" , foreign ) )

		conn.commit()

conn.close()