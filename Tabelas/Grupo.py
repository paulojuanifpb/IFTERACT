import sqlite3

# CONEXÃO
conn = sqlite3.connect(' ifteract.db ')

# criação do cursor
cursor = conn.cursor()

# criação das tabelas do banco
cursor.execute("""
    CREATE TABLE tb_Grupo(
    id int auto_increment primary key,
    nome VARCHAR(70) not null,
    data date,
    administrador int not null,
    foreign key (administrador) references tb_Usuario('id')

     );






""")

conn.close()
