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
    
#Tabela Abastecimento
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS Abastecimento(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                dia_semana TEXT,
                valor_abastecimento TEXT,
                litros TEXT
            )""")
        print("Tabela Abastecimento criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar Abastecimento!")     
    


 #Tabela Mercado Livre
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS mercado_livre(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes TEXT,
                total_entregas TEXT,
                total_devolvidas TEXT,
                total_km TEXT,
                total_abastecimento TEXT,
                total_lucro TEXT,
                total_valor_rota TEXT
            )""")
        print("Tabela Mercado Livre criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela Mercado Livre!", e)
 #Tabela Shoppee
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS shoppee(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes TEXT,
                total_entregas TEXT,
                total_devolvidas TEXT,
                total_km TEXT,
                total_abastecimento TEXT,
                total_lucro TEXT,
                total_valor_rota TEXT
            )""")
        print("Tabela Shoppee criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela Shoppee!", e)
 #Tabela Eu Entrego
try:
    with con:
        cur= con.cursor()
        cur.execute("""
            CREATE TABLE IF NOT EXISTS eu_entrego(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                mes TEXT,
                total_entregas TEXT,
                total_devolvidas TEXT,
                total_km TEXT,
                total_abastecimento TEXT,
                total_lucro TEXT,
                total_valor_rota TEXT
            )""")
        print("Tabela Eu Entrego criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar tabela Eu Entrego!", e)