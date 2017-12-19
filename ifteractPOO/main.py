import mysql.connector
from database.configDB import config
import datetime
from model.Usuario import Usuario, criarTabelaUsuario
from model.Post import Post, criarTabelaPost
from model.Grupo import Grupo, criarTabelaGrupo
from model.Mensagem import Mensagem, criarTabelaMensagem
from model.Notificacao import Notificacao,criarTabelaNotificacao
from model.RedeSocial import RedeSocial
from database.TabelasDAO import criarTabelas
from database.RedeSocialDAO import RedeSocialDAO
from database.UsuarioDAO import UsuarioDAO
from database.NotificacaoDAO import NotificacaoDAO

from model import Sistema


# CONEXÃO

# criação do cursor
# criação das DMLs

def exibirMenuHome(usuario):

    print('''
                    %s
            ==      HOME        ==
             1-Solicitar Amizade
             2-Enviar Mensagem
             3-Listar Usuarios
             4-Mostrar Mensagens
             5-notificacoes
             6-aceitar Solicitacao
             7-Desfazer Amizade
             0-Sair"

          ''' %usuario.nome)


def exibirMenuInicio():


    redesocialDAO = RedeSocialDAO()
    retornoSetRede = redesocialDAO.listar()
    idRedeSocial = retornoSetRede[0]
    redeSocial = retornoSetRede[1]

    if(idRedeSocial == 0):

        print('''
            
            SEJA BEM VINDO A REDE SOCIAL               
                                                       
            1-Dar nome a Rede                               
            2-Cadastrar                                  
            3-Logar                                        
            0-Sair                                            
                                                                        
                                                            
        ''')

    else:
        print('''

            SEJA BEM VINDO A %s  
                
            1-Dar nome a Rede                               
            2-Cadastrar                                  
            3-Logar                                        
            0-Sair                                            


                ''' %redeSocial.nome)




'''
    Cadastrar Usuario
'''
def cadastrar():
    #Iniciando Cadastro
    print('CADASTRANDO USUARIO')
    print("CASO QUEIRA Cancelar o Cadastro a Qualquer momento digite %&AA")

    nome = input('Digite o Nome:\n')

    #Verificando se é desejado cancelar Cadastro
    if (nome == "%&AA"):
        return "Cadastro Cancelado"

    email = input('Digite o Email:\n')
    if (email == "%&AA"):
        return "Cadastro Cancelado"


    while(True):
        try:
            print("DATA DE NASCIMENTO")

            #DIA
            dia = int(input('\nDigite o Dia:\n'))
            # Verificando se é desejado cancelar Cadastro
            if (dia < 0):
                return "Cadastro Cancelado"

            #MES
            mes = int(input('Digite o Mes:\n'))
            # Verificando se é desejado cancelar Cadastro
            if (mes < 0):
                return "Cadastro Cancelado"

            #ANO
            ano = int(input('Digite o Ano:\n'))
            # Verificando se é desejado cancelar Cadastro
            if (ano < 0):
                return "Cadastro Cancelado"

            nascimento =  datetime.date(ano,mes,dia)


            break

        except ValueError:
         print("Valor para data inválido")

    #PROFISSAO
    profissao = input('Digite a profissao:\n')
    # Verificando se é desejado cancelar Cadastro
    if (nome == "%&AA"):
        return "Cadastro Cancelado"

    #GENERO
    genero = input('Digite o Genero:\n')
    # Verificando se é desejado cancelar Cadastro
    if (nome == "%&AA"):
        return "Cadastro Cancelado"
    publico = False

    #SENHA
    senha = input('Digite a Senha:\n')
    # Verificando se é desejado cancelar Cadastro
    if (nome == "%&AA"):
        return "Cadastro Cancelado"

    usuario = Usuario(nome,email,nascimento, profissao, genero, publico, senha)
    usuarioDAO =  UsuarioDAO()
    usuarioDAO.inserir(usuario)
    print("CADASTRO REALIZADO COM SUCESSO")

def exibirMenu():


    print('''
            1-Solicitar Amizade
             2-Enviar Mensagem
             3-Listar Usuarios
             4-Mostrar Mensagens
             5-notificacoes
             6-aceitar Solicitacao
             0-Sair"
             
             '''
          )

'''
    Criação da Rede Social
'''

def criarRedeSocial():
    nome = str(input('Digite um nome para a Rede Social:\n'))
    descricao = str(input('Descreva sua Rede Social:\n'))

    redeSocial = RedeSocial(nome,descricao)
    redeSocialDAO = RedeSocialDAO()
    idRedeSocial = redeSocialDAO.inserirRedeSocial(redeSocial)
    return idRedeSocial

#Funcao de Logar
def logar():
    #Criacao do cursor da conexao(Banco de Dados - SQLite3)

    conn = mysql.connector.connect(**config)
    cursor = conn.cursor()

    #Pedindo Dados
    email = input("Digite o seu email:\n ")
    senha = input("Digite sua senha:\n ")

    #Comando Sql de Consulta(Select
    cursor.execute("""
        Select * From tb_Usuario where email = %s and senha = %s;
    """, (email, senha))
    user = cursor.fetchone()
    print(user)

    cursor.close()
    conn.close()

    if (user == None):
        return (False, "NADA")
    else:
        return (True, user)



#Funcao de BUscar Notificacoes no BD
def BuscarNotificacoes(idUser):

    conn = mysql.connector.connect(**config)

    #Criacao do cursor pra manipulcao apartir de conn(BD da rede)
    cursor = conn.cursor()

    #Contador de Notificacoes
    contador = 0

    #Comando Sql de consulta(Select)
    cursor.execute("""
        Select texto,confirmar,emissor,tb_Usuario.email from tb_Notificacao, tb_Usuario
         where receptor = %s and tb_Usuario.id = tb_Notificacao.emissor ;
    """,(idUser,))

    #TEsxo a ser reotornado
    texto = ""
    for linha in cursor.fetchall():
        texto = texto + "\n"+ str(linha)
        contador +=1

    #Se não houver Notificacoes enviar ess mensagem de return
    if (texto == ""):
        texto = "Não há nenhuma notificacao:"

    cursor.close()
    conn.close()
    return (contador, texto)


'''
    Buscar Mensagens
'''
#Funcao de Buscar todas As Mensagens
def buscarMensagem(idUser):

    conn = mysql.connector.connect(**config)

     #Criacao do cursor pra manipulcao apartir de conn(BD da rede)
    cursor = conn.cursor()

    contador = 0
    cursor.execute("""
        Select texto,emissor,tb_Usuario.email from tb_Mensagem, tb_Usuario
         where receptor = %s and tb_Usuario.id = tb_Mensagem.emissor;
    """,(idUser,))

    texto = ""
    for linha in cursor.fetchall():
        texto = texto + "\n"+ str(linha)
        contador +=1

    if (texto == ""):
        texto = "Não há nenhuma mensgem"


    cursor.close()
    conn.close()

    return (contador, texto)

"""
    Enviar Mensagem
"""



def quadroAvisos(notificacaoDAO, idUsuario):

    notificacoes = notificacaoDAO.listar(idUsuario)
    notificacoesEnviadas = notificacoes[0]
    notificacoesRecebidas = notificacoes[1]



    quantidadeEnviadas = len(notificacoesEnviadas)
    for notificacaoE in notificacoesEnviadas[quantidadeEnviadas - 3:]:
        print("""
                        Ultimas Notificacoes Enviadas
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
    
        %s
        
        
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        
        """ %notificacaoE)

    for notificacaoR in notificacoesRecebidas:
        if(notificacaoR.vizualizado == False):
            print("""
                                    Notificacoes Recebidas
                    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

                    %s


                    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

                    """ %notificacaoR)



'''
    Main - Funcao Principal
'''
def main():

    sair = False
    criarTabelas()

    while (True):

        logou = False
        while(logou != True and sair == False):
            try:

                exibirMenuInicio()
                escolha = int(input("Digite o numero correspondente a opção"))

                if(escolha == 1):
                    criarRedeSocial()

                if(escolha == 2):
                    print(cadastrar())

                elif(escolha == 3):
                    respostas = logar()
                    logou = respostas[0]


                elif(escolha == 0):
                    print("Bye")
                    sair = True


                '''
                    home
                '''
                if(logou):

                    """
                        Criando OBJETO USUARIO E DAO
                    """
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
                    usuarioDAO = UsuarioDAO()
                    notificacaoDAO =NotificacaoDAO()

                    while(logou and sair == False):

                        try:
                            quadroAvisos(notificacaoDAO,idUsuario)

                        #Selecionando a opcao deseja e verificando a resposta

                            exibirMenuHome(usuario)
                            escolha = int(input("\nDigite o numero correspondente a opção:"))

                        #Solicitar Amizade
                            if(escolha == 1):
                                email = input("Digite o email do outro usuario:")
                                usuarioDAO.solicitarAmizade(idUsuario, email)

                        #Enviar Mensagem
                            elif(escolha == 2):
                                email = input("Digite o email do outro usuario:")
                                usuarioDAO.enviarMensagem(usuario,idUsuario,email)

                        #Listar Usuarios
                            elif(escolha == 3):
                                usuarios = usuarioDAO.listar()

                                for user in usuarios:
                                    print("Nome: " + user.nome + " Email: " + user.email)

                        #Mostrar Mensagens
                            elif(escolha == 4):
                                print(buscarMensagem(idUsuario)[1])

                        #Mostrar Notificacoes
                            elif(escolha == 5):
                                print(BuscarNotificacoes(idUsuario)[1])



                        #Aceitar Solicitacao de Amizade
                            elif(escolha == 6):
                                usuarioDAO.aceitarSolicitacao(idUsuario)

                        #Desfazer Amizade
                            elif(escolha == 7):
                                usuarioDAO.desfazerAmizade(idUsuario)

                        #Sair - LogOut
                            if(escolha == 0):
                                logou = False

                        except ValueError:
                            print("\n!!!!!Digite um NUMERO correspondente com a opcao!!!!!\n")


            except ValueError:
                print("\n!!!!Digit um NUMERO correspondente!!!!\n")


if __name__ == '__main__':
    main()
