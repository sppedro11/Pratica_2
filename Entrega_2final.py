import hashlib
import re

class User:
    def __init__(self, nome, senha, role):
        #  Validação se o nome do usuário contém caracteres especiais
        if self.verificar_caracter_especial(nome):
            self.nome = nome
        else:
            raise ValueError("Presença de caracteres especiais no nome do usuário !")
        self.senha_hash = self.hash_senha(senha)
        self.role = role

    # Função que recebe o nome do usuário e verifica se existe caracteres especiais. Retorna True se não houver e False caso contrário.

    def verificar_caracter_especial(self, nome):
        return re.match("^[a-zA-Z0-9_]+$", nome) is not None

    # Função que recebe a senha e a esconde utilizando comandos da biblioteca Hash
    def hash_senha(self, senha):
        return hashlib.sha256(senha.encode()).hexdigest()

# Declaração da lista contendo o cadastro dos usuário e seus dados.
users = [User("dragon1", "1234","common user"),User("sppedro11", "010608","main user"),
            User("got_for", "abc_1234", "common user"),User("xx_max", "abf157", "Admin")]

# Função que realiza o login. Essa recebe o nome e senha digitadas pela pessoa e verifica se estão corretos. Caso esteja, realiza o login.
def login(nome_entrada, senha_entrada):
    for c,perfil in enumerate(users):
        if perfil.nome == nome_entrada:
            senha_entrada_hash = perfil.hash_senha(senha_entrada)
            if senha_entrada_hash == perfil.senha_hash:
                print(f"O usuário de nome '{perfil.nome}' acabou de realizar o login como '{perfil.role}'.")
                break
            else:
                print(f"A senha digitada para o usuário '{nome_entrada}' está incorreta")
                break
        if c == len(users) - 1:
            print(f"O Nome do usuário '{nome_entrada}' está incorreto")

# Teste com entrada de dados
login("dragon1", "1234")
login("sppedro11", "010608")
login("got_fo", "abc_1234")
login("xx_max", "abf157")
login("xx_max", "abf")
