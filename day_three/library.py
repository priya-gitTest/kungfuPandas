import sqlite3

conn = sqlite3.connect("library.sl3")

cursor = conn.cursor()

result = cursor.execute("SELECT * FROM book")

print(result.fetchall())


title = input("Enter a book title: ")

author = input("Who wrote it? ")

cursor.execute("INSERT INTO book(title, author) VALUES (?,?)", (title, author))

conn.commit()

conn.close()