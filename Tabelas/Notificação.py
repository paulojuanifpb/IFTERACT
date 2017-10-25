import sqlite3

# CONEXÃO
conn = sqlite3.connect(' ifteract.db ')

# criação do cursor
cursor = conn.cursor()

# criação das tabelas do banco
cursor.execute("""
    CREATE TABLE tb_Notificacao(
    id int auto_increment primary key,
    texto VARCHAR(100),
    confirmar boolean default false,
    visualizado boolean default false,
    emissor int not null,
    receptor int not null,
    foreign key (emissor) references tb_Usuario('id'),
    foreign key (receptor) references tb_Usuario('id')

     );






""")

conn.close()
