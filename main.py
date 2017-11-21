import sqlite3
import datetime
from Model import Usuario
from Model import Post
from Model import Grupo
from Model import Mensagem
from Model import Notificacao
from Model import RedeSocial
from Model import Sistema


# CONEXÃO
conn = sqlite3.connect("NADA")

# criação do cursor
cursor = conn.cursor()
# criação das DMLs
def cadastrar(conn):
    print('CADASTRANDO USUARIO')
    nome = input('Digite o Nome:\n')
    email = input('Digite o Email:\n')
    try:
        dia = int(input('Digite o Dia:\n'))
        mes = int(input('Digite o Mes:\n'))
        ano = int(input('Digite o Ano:\n'))
        nascimento =  datetime.date(ano,mes,dia)
        profissao = input('Digite a profissao:\n')

    except ValueError:
        print("Valor para data inválido")
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

#Funcao de Logar
def logar(conn):
    #Criacao do cursor da conexao(Banco de Dados - SQLite3)
    cursor = conn.cursor()

    #Pedindo Dados
    email = input("Digite o seu email:\n ")
    senha = input("Digite sua senha:\n ")

    #Comando Sql de Consulta(Select
    cursor.execute("""
        Select * From tb_Usuario where email = ? and senha = ?;
    """, (email, senha))
    user = cursor.fetchone()
    print(user)

    if (user == None):
        return (False, "NADA")
    else:
        return (True, user)

#Funcao de BUscar Notificacoes no BD
def BuscarNotificacoes(idUser,conn):

    #Criacao do cursor pra manipulcao apartir de conn(BD da rede)
    cursor = conn.cursor()

    #Contador de Notificacoes
    contador = 0

    #Comando Sql de consulta(Select)
    cursor.execute("""
        Select texto,confirmar,emissor,tb_Usuario.email from tb_Notificacao, tb_Usuario
         where receptor = ? and tb_Usuario.id = tb_Notificacao.emissor ;
    """,(idUser,))

    #TEsxo a ser reotornado
    texto = ""
    for linha in cursor.fetchall():
        texto = texto + "\n"+ str(linha)
        contador +=1

    #Se não houver Notificacoes enviar ess mensagem de return
    if (texto == ""):
        texto = "Não há nenhuma notificacao:"

    return (contador, texto)


#Funcao de Buscar todas As Mensagens
def buscarMensagem(idUser,conn):

     #Criacao do cursor pra manipulcao apartir de conn(BD da rede)
    cursor = conn.cursor()

    contador = 0
    cursor.execute("""
        Select texto,emissor,tb_Usuario.email from tb_Mensagem, tb_Usuario
         where receptor = ? and tb_Usuario.id = tb_Mensagem.emissor;
    """,(idUser,))

    texto = ""
    for linha in cursor.fetchall():
        texto = texto + "\n"+ str(linha)
        contador +=1

    if (texto == ""):
        texto = "Não há nenhuma mensgem"

    return (contador, texto)

def enviarMensagem(usuario,idUsuario, conn):
    try:
        email = input("Digite o email do outro usuario\n")


        cursor = conn.cursor()
        cursor.execute("""
            select id from tb_Usuario where email = ?
        """,(email,))

        idR = cursor.fetchone()[0]

        cursor.execute("""
            Select confirmar from tb_Notificacao where emissor = ? and receptor = ?;
        """,(idR, idUsuario))

        confirmacao = cursor.fetchone()[0]

        if (confirmacao == "true"):
            texto = input("Digite a sua mensagem\n")
            usuario.enviarMensagem(texto,idUsuario, idR, conn)

        else:
            print("Amigo Nao encontrado")
    except TypeError:
        print("Email não encontrado")





def main():

    sair = False
    conn = sqlite3.connect("sistema.db")
    cursor = conn.cursor()

    while (True):
        try:
            escolha  = int(input("Digite:\n 1 - Criar Rede Social\n 2 - Entrar na Sua rede Social\n"))

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
        except ValueError:
            print("Digite um NUMERO que correspond a sua vontade:\n")


    logou = False
    while(logou != True and sair == False):
        try:
            escolha = int(input("Digite o numero correspondente a opção:\n 1-Cadastrar-se\n 2-Logar\n 3-Sair"))

            if(escolha == 1):
                cadastrar(conn)
                exibirUsuario(conn)

            elif(escolha == 2):
                respostas = logar(conn)
                logou = respostas[0]


            elif(escolha == 3):
                print("Bye")
                sair = True


            if(logou):
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
                while(logou and sair == False):
                    try:

                    #Verificando se a Notificaoes(Solicitacoes)

                        quantidadeNotificacoes = BuscarNotificacoes(idUsuario, conn)[0]
                        if(quantidadeNotificacoes > 0):
                            print("\n---VocÊ tem %s solicitacoes" %quantidadeNotificacoes)

                    #Verificando se a mensagens

                        quantidadeMensagem = buscarMensagem(idUsuario, conn)[0]
                        if(buscarMensagem(idUsuario, conn)):
                            print("\n---VocÊ tem %s Mensagens" %quantidadeMensagem)

                    #Selecionando a opcao deseja e verificando a resposta
                        escolha = int(input("\nDigite o numero correspondente a opção:\n 1-Solicitar Amizade\n 2-Enviar Mensagem \n 3-Listar Usuarios\n 5-Mostrar Mensagens\n 6-notificacoes\n 7-aceitar Solicitacao\n 8-Sair\n"))

                    #Solicitar Amizade
                        if(escolha == 1):
                            email = input("Digite o email do outro usuario")
                            usuario.solicitarAmizade(idUsuario, email,conn)

                    #Enviar Mensagem
                        elif(escolha == 2):
                            enviarMensagem(usuario,idUsuario,conn)

                    #Listar Usuarios
                        elif(escolha == 3):
                            usuarios = usuario.listar(conn)

                            for usuario in usuarios:
                                print("Nome: " + usuario.nome + " Email: " + usuario.email)

                    #Mostrar Mensagens
                        elif(escolha == 5):
                            print(buscarMensagem(idUsuario, conn)[1])

                    #Mostrar Notificacoes
                        elif(escolha == 6):
                            print(BuscarNotificacoes(idUsuario,conn)[1])



                    #Aceitar Solicitacao de Amizade
                        elif(escolha == 7):
                            usuario.aceitarSolicitacao(idUsuario,conn)

                    #Sair - LogOut
                        if(escolha == 8):
                            logou = False

                    except ValueError:
                        print("\n!!!!!Digite um NUMERO correspondente com a opcao!!!!!\n")


        except ValueError:
            print("\n!!!!Digit um NUMERO correspondente!!!!\n")


if __name__ == '__main__':
    main()
