from pacotes import *
import sqlite3

#criando conexão

try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com Banco de Dados!")
    
# Crinado  Tabela do Banco de dados
#CRiar tabela de login
try:
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS login(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                usuario TEXT,
                senha TEXT
            )""")
        print("Tabela de Login criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela de Login:", e)
#Tabela Rota Mercado lIvre
try:
    with con:
        cur = con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Rota_Mercado_Livre(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                dia_semana TEXT,
                valor_rota TEXT,
                km TEXT,
                valor_bomba TEXT,
                lucro TEXT,
                entregas TEXT,
                devolvidas TEXT,
                total TEXT
            )
        """)
        print("Tabela Rota Mercado Livre criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Rota Mercado Livre:", e)
    
#Tabela Rota Mercado lIvre
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Rota_Shoppee(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                dia_semana TEXT,
                valor_rota TEXT,
                km TEXT,
                valor_bomba TEXT,
                lucro TEXT,
                entregas TEXT,
                devolvidas TEXT,
                total TEXT
            )""")
        print("Tabela Rota Shoppee criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Rota Shoppee!")    
 
#Tabela Rota Mercado lIvre
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Rota_Eu_Entrego(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                dia_semana TEXT,
                valor_rota TEXT,
                km TEXT,
                valor_bomba TEXT,
                lucro TEXT,
                entregas TEXT,
                devolvidas TEXT,
                total TEXT
            )""")
        print("Tabela Rota Eu Entrego criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Rota Eu Entrego!")      