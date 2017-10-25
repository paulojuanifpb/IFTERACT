import sqlite3

# CONEXÃO
conn = sqlite3.connect(' ifteract.db ')

# criação do cursor
cursor = conn.cursor()

# criação das tabelas do banco
cursor.execute("""
    CREATE TABLE tb_Usuario (
        id int auto_increment primary key,
        nome VARCHAR(70) NOT NULL,
        email VARCHAR(50) NOT NULL,
        nascimento DATE,
        profissao VARCHAR(50),
        genero VARCHAR(10),
        publico BOOLEAN default FALSE,
        senha VARCHAR(30) NOT NULL
     );

""")


conn.close()
