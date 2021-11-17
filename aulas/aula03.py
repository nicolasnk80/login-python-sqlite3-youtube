import sqlite3

banco = sqlite3.connect("banco_de_dados_teste.db")

cursor = banco.cursor()

cursor.execute("UPDATE pessoas SET nome = 'Fernando' WHERE nome = 'Nicolas'")

banco.commit()

banco.close()
