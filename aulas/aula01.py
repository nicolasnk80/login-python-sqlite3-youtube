import sqlite3

banco = sqlite3.connect("banco_de_dados_teste.db")

cursor = banco.cursor()

#cursor.execute("CREATE TABLE pessoas (nome text, idade number, telefone number)")
cursor.execute("INSERT INTO pessoas VALUES ('João', 60, 976575754)")

banco.commit()
banco.close()
