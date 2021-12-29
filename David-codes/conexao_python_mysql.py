#Importação de bibliotecas
import mysql.connector
# import sys
import PySimpleGUI as ui

def abre_conexao_bd():
    try:
        #con = mysql.connector.connect(host="200.128.9.67", port=33004, database="mon_davidson", user="mon_davidson", password="dav00004")
        con = mysql.connector.connect(host="localhost", port=3306, database="mydb", user="root", password="")
        return con

    except mysql.connector.Error as e:
        print("Erro de conexão: ", e)

    return 0    

#----- Modulo que executa uma alteração no banco (insert, update, delete...) e não retorna resultado
def manipula_dados(sql):
    con = abre_conexao_bd()
    if con != 0:        
        cursor = con.cursor()     
        try:
            cursor.execute(sql)
            con.commit() #este comando salva as alterações realizadas durante a conexão (con). Note que sem ele, as alterações não aparecem após uma nova execução.
            ui.popup("Operação realizada com sucesso.\n")
        except:
            ui.popup("Alteração não efetuada")
        cursor.close()
        con.close()
    else:
        print("A operação não foi realizada.\n")

#----- Módulo que executa uma consulta e imprime os resultados
def executa_conculta(sql):
    con = abre_conexao_bd()
    if con != 0:
        resultado = []
        cursor = con.cursor()
        try:     
            cursor.execute(sql)              
            for linha in cursor.fetchall():
                resultado.append(linha)
            print("\nfim da impressão.\n\n")
        except mysql.connector.Error as e:
            ui.popup("A requisição não foi executada.\n") 
        cursor.close()
        con.close()
        return resultado
    else:
        print("O select não foi executado.\n")     


