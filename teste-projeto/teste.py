import sqlite3

def conexao():
    global cursor
    global banco
    
    banco = sqlite3.connect('teste.db')
    cursor = banco.cursor()

    cursor.execute("CREATE TABLE IF NOT EXISTS users (nome text, senha text)")

def cadastrar():
    conexao()

    nome = input("Digite um nome de usuario...: ")
    senha = input("Digite uma senha............: ")

    if nome and senha :
        try :
            try :
                cursor.execute("SELECT nome FROM users WHERE nome = '{}'".format(nome))

                if cursor.fetchall()[0][0] == nome :
                    return False
                        
            except :
                cursor.execute("INSERT INTO users VALUES ('{}', '{}')".format(nome, senha))

                banco.commit()
                banco.close()

                return True

        except sqlite3.Error as erro :
            print(erro)
            return False
    
    else :
        return False

def entrar():
    conexao()
    
    nome = input("User...: ")
    senha = input("Senha..: ")

    if nome and senha :
        try :
            cursor.execute("SELECT senha FROM users WHERE nome = '{}'".format(nome))
            senha_cap = cursor.fetchall()

            try :
                if senha == senha_cap[0][0] :
                    return True
            
            except :
                return False
        
        except sqlite3.Error as erro :
            print(erro)
            return False
    
    else :
        return False


while True :
    print("(c) para cadastrar\n(e) para entrar\n(s) para sair")
    le = input(": ").lower()

    if le == "c" :
        if cadastrar() == True :
            print("Cadastro realizado com sucesso!\n")

        else :
            print("não foi possivel realizar seu cadastro!\n")
    
    elif le == "e" :
        if entrar() == True :
            print("parabéns você entrou!\n")
            break

        else :
            print("nome ou senha invalido, não foi possivel logar!\n")
    
    elif le == "s" :
        print("Até a mais.\n")
        break

    else :
        print("argumento invalido.. tente de novo!\n")
