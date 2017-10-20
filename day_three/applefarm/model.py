import sqlite3


class Model:

	def __init__(self):
		self.conn = sqlite3.connect("applefarm.sl3")
		self.cursor = self.conn.cursor()

	def createTables(self):
		self.cursor.execute('''CREATE TABLE employees(id INTEGER PRIMARY KEY,
			name VARCHAR(256),
			hours INTEGER,
			payperhour REAL)''')

		self.cursor.execute('''CREATE TABLE trees(id INTEGER PRIMARY KEY,
			ripeapples INTEGER,
			rottenapples INTEGER,
			costperapple REAL,
			type VARCHAR(256))''')

		self.conn.commit()
		
	def selectAllEmployees(self):
		result = self.cursor.execute("SELECT * FROM employees")

		return result.fetchall()

	def selectAllTrees(self):
		result = self.cursor.execute("SELECT * FROM trees")

		return result.fetchall()

	#Takes in a list[name,hours,payperhour] and inserts it into the database
	def insertEmployee(self, employee_info):
		self.cursor.execute("INSERT INTO employees(name,hours,payperhour) VALUES (?,?,?)", employee_info)
		self.conn.commit()

	def deleteEmployee(self, employee_id):
		self.cursor.execute("DELETE FROM employees WHERE id=?",(employee_id,) )
		self.conn.commit()

	def insertTree(self, tree_info):
		self.cursor.execute("INSERT INTO trees(ripeapples, rottenapples, costperapple, type) VALUES (?,?,?,?)",tree_info)
		self.conn.commit()

	#update tree takes in a list[ripeapples,rottenapples,costperapple,typeofapple,id] in that order
	def updateTree(self, tree_info):
		self.cursor.execute("UPDATE trees SET ripeapples=?, rottenapples=?, costperapple=?, type=? WHERE id=?",tree_info)
		self.conn.commit()

	def selectOneTree(self, tree_id):
		result = self.cursor.execute("SELECT * FROM trees WHERE id=?", (tree_id,) )

		return result.fetchone()

	def closeConnection(self):
		self.conn.close()