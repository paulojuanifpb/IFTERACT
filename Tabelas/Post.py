import sqlite3

# CONEXÃO
conn = sqlite3.connect(' ifteract.db ')

# criação do cursor
cursor = conn.cursor()

# criação das tabelas do banco
cursor.execute("""
    CREATE TABLE tb_Post (
    id int auto_increment primary key,
    texto text not null,
    publico boolean default true
     );






""")

conn.close()
