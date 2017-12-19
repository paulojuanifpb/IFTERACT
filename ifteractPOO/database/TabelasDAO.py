import mysql.connector
from database.configDB import config

def criarTabelas():
    try:
        conn = mysql.connector.connect(**config)
        cursor = conn.cursor()
        cursor.execute("""

            CREATE TABLE tb_Usuario (
                            id INTEGER NOT NULL PRIMARY KEY auto_increment,
                            nome VARCHAR(70) NOT NULL,
                            email VARCHAR(50) NOT NULL UNIQUE,
                            nascimento DATE,
                            profissao VARCHAR(50),
                            genero VARCHAR(10),
                            publico BOOLEAN default FALSE,
                            senha VARCHAR(30) NOT NULL
                         );
                         
            create table tb_RedeSocial(
                        
                id int primary key auto_increment,
                nome varchar(100),
                descricao varchar(250),
                data_criacao date
            );
            
            CREATE TABLE tb_Notificacao(
                        id INTEGER NOT NULL PRIMARY KEY auto_increment,
                        texto VARCHAR(100),
                        confirmar boolean default false,
                        data date,
                        visualizado boolean default false,
                        emissor int not null,
                        receptor int not null,
                        foreign key (emissor) references tb_Usuario(id),
                        foreign key (receptor) references tb_Usuario(id)
                    
                         );
                         
            CREATE TABLE tb_Mensagem(
                    id INTEGER NOT NULL PRIMARY KEY auto_increment,
                    texto text not null,
                    data date,
                    visualizado boolean default false,
                    emissor int not null,
                    receptor int not null,
                    foreign key (emissor) references tb_Usuario(id),
                    foreign key (receptor) references tb_Usuario(id)
                     );     
                        
                        
        """)

    except:
        pass