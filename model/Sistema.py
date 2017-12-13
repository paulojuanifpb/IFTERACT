import sqlite3
import datetime


conn = sqlite3.connect("sistema.db")

cursor = conn.cursor()
try:
    cursor.execute("""
        Create Table tb_redes(
            id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
            nome varchar(50),
            data date
        
        );
        """)

except:
    print("Sistema Ja foi Criado")

def adicionarRede(nome,conn):
    data = datetime.date.today()
    cursor.execute("""
    Insert into tb_redes(nome,data) Values(?, ?)
    """,(nome, data))

    conn.commit()

    listarRedes()
def listarRedes():

    cursor.execute("""
    Select * From tb_redes;
    
    """)
    for linha in cursor.fetchall():
        print(linha)

