from pacotes import *
import sqlite3

#criando conexão

try:
    con = sqlite3.connect('database.db')
    print("Conexão com Banco de Dados efetuado com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com Banco de Dados!")
    
# Criando a tabela de Login    
def criar_login(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO login (usuario, senha) values(?,?)"
        cur.execute(query, i) 
def atualizar_login(i):
    with con:
        cur = con.cursor()
        query = "UPDATE login SET usuario=?, senha=? WHERE id=?"
        cur.execute(query, i)
def ver_login():
    try:
        with con:  # Certifique-se de que `con` (conexão) está definida globalmente
            cur = con.cursor()
            cur.execute('SELECT * FROM login')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
def excluir_login(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM login WHERE id = ?"
        cur.execute(query, (i,))
        print(f"Login com ID {i} foi excluído com sucesso.")
        
def verificar_usuario(usuario):
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM login WHERE usuario=?', (usuario,))
            return cur.fetchone() is not None
    except Exception as e:
        print(f"Erro ao verificar usuário: {e}")
        return False
 
# Tabela Mercado Livre
def criar_dados_ml(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Rota_Mercado_Livre(data,dia_semana,valor_rota,valor_bomba,km,lucro,entregas,devolvidas,total) values(?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
        con.commit()  # Commit para salvar as alterações no banco de dados
#-----------------------------------------------------------------------------------------------------------------
def ver_dados_ml():
    try:
        with con:  # Certifique-se de que `con` (conexão) está definida globalmente
            cur = con.cursor()
            cur.execute('SELECT * FROM Rota_Mercado_Livre')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
#-----------------------------------------------------------------------------------------------------------------
def calcular_total_lucro_ml():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT SUM(lucro) FROM Rota_Mercado_Livre')
            resultado = cur.fetchone()[0]
            return resultado if resultado is not None else 0
    except Exception as e:
        print(f"Erro ao calcular total de lucro: {e}")
        return 0
#-----------------------------------------------------------------------------------------------------------------
def atualizar_dados_ml(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Rota_Mercado_Livre SET data=?,dia_semana=?,valor_rota=?,valor_bomba=?,km=?,lucro=?,entregas=?,devolvidas=?,total=? WHERE id=?"
        cur.execute(query, i)
#-----------------------------------------------------------------------------------------------------------------
def excluir_dados_ml(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Rota_Mercado_Livre WHERE id=?"
        cur.execute(query, (i))
        
##############################################################################################################################################################

# Tabela Shoppee
def criar_dados_s(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Rota_Shoppee(data,dia_semana,valor_rota,valor_bomba,km,lucro,entregas,devolvidas,total) values(?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
        con.commit()  # Commit para salvar as alterações no banco de dados
#-----------------------------------------------------------------------------------------------------------------
def ver_dados_s():
    try:
        with con:  # Certifique-se de que `con` (conexão) está definida globalmente
            cur = con.cursor()
            cur.execute('SELECT * FROM Rota_Shoppee')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []

#-----------------------------------------------------------------------------------------------------------------
def atualizar_dados_s(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Rota_Shoppee SET data=?,dia_semana=?,valor_rota=?,valor_bomba=?,km=?,lucro=?,entregas=?,devolvidas=?,total=? WHERE id=?"
        cur.execute(query, i)
#-----------------------------------------------------------------------------------------------------------------  
def excluir_dados_s(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Rota_Shoppee WHERE id=?"
        cur.execute(query, (i))

# Tabela Eu Entrego
def criar_dados_ee(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Rota_Eu_Entrego(data,dia_semana,valor_rota,valor_bomba,km,lucro,entregas,devolvidas,total) values(?,?,?,?,?,?,?,?,?)"
        cur.execute(query, i)
        con.commit()  # Commit para salvar as alterações no banco de dados
#-----------------------------------------------------------------------------------------------------------------
def ver_dados_ee():
    try:
        with con:  # Certifique-se de que `con` (conexão) está definida globalmente
            cur = con.cursor()
            cur.execute('SELECT * FROM Rota_Eu_Entrego')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
#-----------------------------------------------------------------------------------------------------------------
def calcular_total_lucro_ee():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT SUM(lucro) FROM Rota_Eu_Entrego')
            resultado = cur.fetchone()[0]
            return resultado if resultado is not None else 0
    except Exception as e:
        print(f"Erro ao calcular total de lucro: {e}")
        return 0
#-----------------------------------------------------------------------------------------------------------------
def atualizar_dados_ee(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Rota_Eu_Entrego SET data=?,dia_semana=?,valor_rota=?,valor_bomba=?,km=?,lucro=?,entregas=?,devolvidas=?,total=? WHERE id=?"
        cur.execute(query, i)
#-----------------------------------------------------------------------------------------------------------------
def excluir_dados_ee(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Rota_Eu_Entrego WHERE id=?"
        cur.execute(query, (i))


# Tabela Abastecimento
def criar_dados_abastecimento(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Abastecimento(data,dia_semana,valor_abastecimento,litros) values(?,?,?,?)"
        cur.execute(query, i)
        con.commit()  # Commit para salvar as alterações no banco de dado

def ver_dados_abastecimento():
    try:
        with con:  # Certifique-se de que `con` (conexão) está definida globalmente
            cur = con.cursor()
            cur.execute('SELECT * FROM Abastecimento')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []

def calcular_total_abastecimento():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT SUM(valor) FROM Abastecimento')
            resultado = cur.fetchone()[0]
            return resultado if resultado is not None else 0
    except Exception as e:
        print(f"Erro ao calcular total de abastecimento: {e}")
        return 0

def atualizar_dados_abastecimento(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Abastecimento SET data=?,dia_semana=?,valor_abastecimento=?,litros=?,total=? WHERE id=?"
        cur.execute(query, i)

def excluir_dados_abastecimento(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Abastecimento WHERE id=?"
        cur.execute(query, (i,))

# Tabela de dados anuais
def criar_dados_anuais(i):
    with con:
        cur = con.cursor()
        query = "INSERT INTO Dados_Anuais(mes,valor_total_rota,valor_total_abastecimento,valor_total_lucro,total_valor_rota) values(?,?,?,?,?)"
        cur.execute(query, i)
        con.commit()  # Commit para salvar as alterações no banco de dados
def ver_dados_anuais():
    try:
        with con:
            cur = con.cursor()
            cur.execute('SELECT * FROM Dados_Anuais')
            return cur.fetchall()
    except Exception as e:
        print(f"Erro ao buscar dados: {e}")
        return []
def atualizar_dados_anuais(i):
    with con:
        cur = con.cursor()
        query = "UPDATE Dados_Anuais SET mes=?,valor_total_rota=?,valor_total_abastecimento=?,valor_total_lucro=?,total_valor_rota=? WHERE id=?"
        cur.execute(query, i)
def excluir_dados_anuais(i):
    with con:
        cur = con.cursor()
        query = "DELETE FROM Dados_Anuais WHERE id=?"
        cur.execute(query, (i,))

    
    
    
    
    
    
    
    
    