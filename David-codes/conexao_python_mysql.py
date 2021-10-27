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
        print("A consulta não foi executada.\n")     


#----- PROGRAMA PRINCIPAL -------------------
# dici = executa_conculta("select * from assunto")
# dicio = {}
# for item in dici:
#     dicio[item[1]] = item[0]
# print(dicio)

#manipula_dados("insert into aluno (nome, turma_id, status) values ('sebastiao', 1, 'A');")
#manipula_dados("update aluno set status = 'A' where id = 2")
#executa_conculta("select * from aluno")

#SUGESTÃO: escreva em python o seguinte algoritmo
#digite 1 para consultar dados, 2 para manipular dados e 3 para sair
#enquanto opcao igual a 1 ou 2, faça
 #   digite o comando a ser executado
  #  se opcao igual a 1
   #     executa_consulta(comando)
    #se opcao igual a 2
    #    manipula_dados(comando)
    #digite 1 para consultar dados, 2 para manipular dados e 3 para sair

