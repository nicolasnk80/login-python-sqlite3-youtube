import sqlite3

banco = sqlite3.connect("banco_de_dados_teste.db")

cursor = banco.cursor()

cursor.execute("SELECT * FROM pessoas WHERE nome = 'Nicolas'")

values = cursor.fetchall()

print(values[0][0])
