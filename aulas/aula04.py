import sqlite3

banco = sqlite3.connect("banco_de_dados_teste.db")

cursor = banco.cursor()

cursor.execute("DELETE from pessoas WHERE nome = 'Maria'")

banco.commit()

banco.close()
