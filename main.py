import sqlite3
import datetime
from model.Usuario import Usuario, criarTabelaUsuario
from model.Post import Post, criarTabelaPost
from model.Grupo import Grupo, criarTabelaGrupo
from model.Mensagem import Mensagem, criarTabelaMensagem
from model.Notificacao import Notificacao,criarTabelaNotificacao
from model.RedeSocial import RedeSocial
from database.RedeSocialDAO import RedeSocialDAO
from model import Sistema


# CONEXÃO
conn = sqlite3.connect("NADA")

# criação do cursor
cursor = conn.cursor()
# criação das DMLs
def cadastrar(conn):
    print('CADASTRANDO USUARIO')
    nome = input('Digite o Nome:\n')
    email = input('Digite o Email:\n')
    print("DATA DE NASCIMENTO")
    while(True):
        try:
            dia = int(input('Digite o Dia:\n'))
            mes = int(input('Digite o Mes:\n'))
            ano = int(input('Digite o Ano:\n'))

            nascimento =  datetime.date(ano,mes,dia)
            break

        except ValueError:
         print("Valor para data inválido")

    profissao = input('Digite a profissao:\n')
    genero = input('Digite o Genero:\n')
    publico = False
    senha = input('Digite a Senha:\n')

    usuario = Usuario(nome,email,nascimento, profissao, genero, publico, senha)
    usuario.inserir(usuario,conn)
    conn.commit()

def exibirMenu():
    print('''1-Solicitar Amizade
             2-Enviar Mensagem
             3-Listar Usuarios
             4-Mostrar Mensagens
             5-notificacoes
             6-aceitar Solicitacao
             0-Sair"

          ''')

'''
    Criação da Rede Social
'''

def criarRedeSocial():
    nome = str(input('Digite um nome para a Rede Social:\n'))
    descricao = str(input('Descreva sua Rede Social:\n'))

    redeSocial = RedeSocial(nome,descricao)
    redeSocialDAO = RedeSocialDAO()
    idRedeSocial = redeSocialDAO.inserirRedeSocial()
    return idRedeSocial

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

        logou = False
        while(logou != True and sair == False):
            try:
                escolha = int(input("Digite o numero correspondente a opção:\n 1-Cadastrar-se\n 2-Logar\n 3-Sair"))

                if(escolha == 1):
                    criarRedeSocial()

                if(escolha == 1):
                    cadastrar(conn)

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

                    usuario = Usuario(nome, email, nascimento, profissao, genero, publico, senha)
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
                            escolha = int(input("\nDigite o numero correspondente a opção"))

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
                            elif(escolha == 4):
                                print(buscarMensagem(idUsuario, conn)[1])

                        #Mostrar Notificacoes
                            elif(escolha == 5):
                                print(BuscarNotificacoes(idUsuario,conn)[1])



                        #Aceitar Solicitacao de Amizade
                            elif(escolha == 6):
                                usuario.aceitarSolicitacao(idUsuario,conn)

                        #Sair - LogOut
                            if(escolha == 0):
                                logou = False

                        except ValueError:
                            print("\n!!!!!Digite um NUMERO correspondente com a opcao!!!!!\n")


            except ValueError:
                print("\n!!!!Digit um NUMERO correspondente!!!!\n")


if __name__ == '__main__':
    main()
