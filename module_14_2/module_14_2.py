import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor()
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute('CREATE INDEX IF NOT EXISTS idx_email ON Users (email)')

cursor.execute('DELETE FROM Users WHERE id = ?', (6, ))


cursor.execute('SELECT COUNT (*) FROM Users')
total_users = cursor.fetchone()[0]
print(total_users)

cursor.execute('SELECT SUM (balance) FROM Users')
sum_balance = cursor.fetchone()[0]
print(sum_balance)

cursor.execute('SELECT AVG (balance) FROM Users')
avg_balance = cursor.fetchone()[0]
print(avg_balance)

connection.commit()
connection.close()