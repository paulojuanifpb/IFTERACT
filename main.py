import sqlite3
import datetime
from Tabelas import Usuario
from Tabelas import Post
from Tabelas import Grupo
from Tabelas import Mensagem
from Tabelas import Notificação
from Tabelas import RedeSocial
from Tabelas import Sistema


# CONEXÃO
conn = sqlite3.connect("NADA")

# criação do cursor
cursor = conn.cursor()
# criação das DMLs
def cadastrar(conn):
    print('CADASTRANDO USUARIO')
    nome = input('Digite o Nome:\n')
    email = input('Digite o Email:\n')
    dia = int(input('Digite o Dia:\n'))
    mes = int(input('Digite o Mes:\n'))
    ano = int(input('Digite o Ano:\n'))
    nascimento =  datetime.date(ano,mes,dia)
    profissao = input('Digite a profissao:\n')
    genero = input('Digite o Genero:\n')
    publico = False
    senha = input('Digite a Senha:\n')

    usuario = Usuario.Usuario(nome,email,nascimento, profissao, genero, publico, senha)
    usuario.inserir(usuario,conn)
    conn.commit()

def atualizarUsuario():
    print('ATUALIZANDO USUARIO')
    novo_nome = input('Digite o Nome:\n')
    nova_profissao = input('Digite a profissao:\n')
    cursor.execute("""
    update tb_Usuario
    set nome = ?, profissao = ?
    where id = 1
    """, (novo_nome, nova_profissao))
    conn.commit()

def deletarUsuario():
     print('DELETANDO USUARIO')
     id = int(input('Digite o id:\n'))
     cursor.execute("""
     delete from tb_Usuario
     where id = ?
     """,(id,))

def exibirUsuario(conn):
    print('EXIBINDO USUARIO')
    cursor = conn.cursor()

    cursor.execute("""
    Select * From tb_Usuario;
    """)

    for linha in cursor.fetchall():
        print(linha)





def inserirPost():
    print('INSERINDO POST')
    id = int(input('Digite o id'))
    texto = input('Digite o texto do post:\n')
    publico = False

    cursor.execute("""
    insert into tb_Post values(?,?,?)
    """,(id, texto, publico))
    conn.commit()

def atualizarPost():
    print('ATUALIZANDO POST')
    novo_texto = input('Digite o Novo texto do post:\n')

    cursor.execute("""
    update tb_Post
    set texto = ?
    where id = 1
    """, (novo_texto,))
    conn.commit()

def deletarPost():
     print('DELETANDO POST')
     id = int(input('Digite o id:\n'))
     cursor.execute("""
     delete from tb_Post
     where id = ?
     """,(id,))

def exibirPost():
    print('EXIBINDO POST')

    cursor.execute("""
    Select * From tb_Post;
    """)

    for linha in cursor.fetchall():
        print(linha)





def inserirGrupo():
    print('INSERINDO GRUPO')
    id = int(input('Digite o id'))
    nome = input('Digite o nome dom grupo:\n')
    dia = int(input('Digite o Dia:\n'))
    mes = int(input('Digite o Mes:\n'))
    ano = int(input('Digite o Ano:\n'))
    data =  datetime.date(ano,mes,dia)
    id_adimin = int(input('Digite o id do administrador do grupo:'))

    cursor.execute("""
    insert into tb_Grupo values(?,?,?,?)
    """,(id, nome, data, id_adimin))
    conn.commit()

def atualizarGrupo():
    print('ATUALIZANDO GRUPO')
    novo_nome = input('Digite o Novo nome do grupo:\n')

    cursor.execute("""
    update tb_Grupo
    set nome = ?
    where id = 1
    """, (novo_nome,))
    conn.commit()

def deletarGrupo():
     print('DELETANDO GRUPO')
     id = int(input('Digite o id:\n'))
     cursor.execute("""
     delete from tb_Grupo
     where id = ?
     """,(id,))

def exibirGrupo():
    print('EXIBINDO GRUPO')

    cursor.execute("""
    Select * From tb_Grupo;
    """)

    for linha in cursor.fetchall():
        print(linha)


def logar(conn):
    cursor = conn.cursor()
    email = input("Digite o seu email:\n ")
    senha = input("Digite sua senha:\n ")

    cursor.execute("""
        Select * From tb_Usuario where email = ? and senha = ?;
    """, (email, senha))
    user = cursor.fetchone()
    print(user)

    if (user == None):
        return (False, "NADA")
    else:
        return (True, user)

def BuscarNotificacoes(idUser,conn):

    cursor = conn.cursor()



    cursor.execute("""
        Select * from tb_Notificacao where receptor = ?;
    """,(idUser,))

    for linha in cursor.fetchall():
        print(linha)





def main():

    conn = sqlite3.connect("sistema.db")
    cursor = conn.cursor()

    while (True):
        escolha  = int(input("Digite:\n 1 - Criar Rede Social\n 2 - Entrar na Sua rede Social"))

        if(escolha == 1):
            nome = input("\n\nDigite o nome da sua Rede Social:\n")

            #ADICIONANDO AO BD SISTEMA TB REDES
            Sistema.adicionarRede(nome,conn)

            #INSTANCIANDO O OBJETO DA REDE SOCIAL
            rede = RedeSocial.RedeSocial(nome,datetime.date.today())

            #CRIANDO BANCO DE DADOS DA REDE
            conn = rede.CriarBanco(nome)

            #CRIANDO ALGUMA TABELAS DA REDE SOCIAL
            Grupo.criarTabela(conn)
            Notificação.criarTabela(conn)
            Mensagem.criarTabela(conn)
            Post.criarTabela(conn)
            Usuario.criarTabela(conn)
            conn.commit()
            break

        elif(escolha == 2):
            nome = input("Digite o Nome da Sua Rede Social:\n")

            cursor.execute("""
            Select * From tb_redes; 
            """)

            for linha in cursor.fetchall():
                print(linha)

            nomeDB = nome + ".db"
            conn = sqlite3.connect(nomeDB)
            break

        else:
            print("OPCAO INVALID")


    logou = False
    while(logou != True):

        escolha = int(input("Digite o numero correspondente a opção:\n 1-Cadastrar-se\n 2-Logar"))

        if(escolha == 1):
            cadastrar(conn)
            exibirUsuario(conn)

        elif(escolha == 2):
            respostas = logar(conn)
            logou = respostas[0]

    print("!--HOME--!")
    usuario = respostas[1]
    idUsuario = usuario[0]
    nome = usuario[1]
    email = usuario[2]
    nascimento = usuario[3]
    profissao = usuario[4]
    genero = usuario[5]
    publico = usuario[6]
    senha = usuario[7]

    usuario = Usuario.Usuario(nome, email, nascimento, profissao, genero, publico, senha)
    while(logou):

        escolha = int(input("Digite o numero correspondente a opção:\n 1-Solicitar Amizade\n 6-notificacoes\n 7-aceitarSolicitacao"))

        if(escolha == 1):
            nome = input("Digite o nome do outro usuario")
            usuario.solicitarAmizade(idUsuario, nome,conn)

        elif(escolha == 2):

            nome = input("Digite o nome do outro usuario")


            cursor = conn.cursor()
            cursor.execute("""
            select id from tb_Usuario where nome = ?
            """,(nome,))

            idR = cursor.fetchone()[0]

            cursor.execute("""
            Select confirmar from tb_Notificacao where emissor = ? and receptor = ?;
            """,(idR, idUsuario))

            confirmacao = cursor.fetchone()[0]

            if (confirmacao == "true"):
                input("TEXTO DA MENSAGEM")

            else:
                print("Amigo Nao encontrado")

        elif(escolha == 6):
            BuscarNotificacoes(idUsuario,conn)

        elif(escolha == 7):
            idSolic = int(input("DIgite o id da solicitacao"))
            cursor = conn.cursor()

            cursor.execute("""
                update tb_Notificacao
                set confirmar = 'true', visualizado = 'true'
                where id = ?;
            """,(idSolic,))

            conn.commit()


if __name__ == '__main__':
    main()
