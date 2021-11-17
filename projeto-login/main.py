import sqlite3
import subprocess as s

def criar_banco():
    global banco
    global cursor

    banco = sqlite3.connect("data_user.db")
    cursor = banco.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS users (nome text, senha text)")

def cadastrar_usuario():
    criar_banco()

    acesso = False

    nome = input("Digite o nome de usuario: ")
    senha = input("Digite uma senha: ")

    if nome and senha :
        try :
            cursor.execute("INSERT INTO users VALUES ('{}', '{}')".format(nome, senha))
            banco.commit()
            banco.close()
            acesso = True
        
        except :
            acesso = False

    return acesso

def entrar_com_usuario():
    criar_banco()

    acesso = False

    nome = input("Nome: ")
    senha = input("Senha: ")

    if nome and senha :
        try :
            cursor.execute("SELECT senha FROM users WHERE nome = '{}'".format(nome))
            senha_cap = cursor.fetchall()
            
            if senha == senha_cap[0][0] :
                acesso = True
            else :
                acesso = False
        
        except :
            acesso = False
    
    return acesso

def abrir_google():
    print("Abriu google")

def analizar_usuario():
    print("(c) para cadastrar\n(e) para entrar\n(s) para sair")
    digitou = input(": ")

    if digitou == "c" :
        if cadastrar_usuario() :
            print("Cadastro realizado com sucesso!\n")

        else :
            print("Não foi possivel realizar seu cadastro!\n")
    
    elif digitou == "e" :
        if entrar_com_usuario() :
            print("Parabens voce entrou!\n")
            abrir_google()

        else :
            print("Login invalido, tente novamente!\n")
    
    elif digitou == "s" :
        print("até logo!")
        exit()

while True :
    analizar_usuario()
