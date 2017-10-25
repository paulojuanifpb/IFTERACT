import sqlite3
import datetime
import Tabelas.Usuario
import Tabelas.Post
import Tabelas.Grupo
import Tabelas.Mensagem
import Tabelas.Notificação
# CONEXÃO
conn = sqlite3.connect(' ifteract.db ')

# criação do cursor
cursor = conn.cursor()
# criação das DMLs
def inserirUsuario():
    print('CADASTRANDO USUARIO')
    id = int(input('Digite o id:\n'))
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
    cursor.execute("""
    insert into tb_Usuario values(?,?,?,?,?,?,?,?)
    """,(id,nome,email,nascimento,profissao,genero,publico,senha))
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

def exibirUsuario():
    print('EXIBINDO USUARIO')

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











def main():

    #usuario
    inserirUsuario()
    exibirUsuario()
    atualizarUsuario()
    exibirUsuario()
    deletarUsuario()
    exibirUsuario()
    # post
    inserirPost()
    exibirPost()
    atualizarPost()
    exibirPost()
    deletarPost()
    exibirPost()
    # grupo
    inserirGrupo()
    exibirGrupo()
    atualizarGrupo()
    exibirGrupo()
    deletarGrupo()
    exibirGrupo()


if __name__ == '__main__':
    main()
