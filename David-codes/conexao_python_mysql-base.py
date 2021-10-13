#INSTALAÇÃO DE BIBLIOTECAS (CASO NECESSÁRIO)
#pip install mysql-connector-python

#Importação de bibliotecas
import mysql.connector
import sys

#Início do programa

def abre_conexao_bd():
    try:
      con = mysql.connector.connect(host="200.128.9.67", port=33006, database="ei32teste", user="ei32teste", password="tes12345")
      #con = mysql.connector.connect(host="localhost", port=3306, database="danilo", user="root", password="")

      return con

    except mysql.connector.Error as e:
      print("Falha na matrix")

    return 0    

#----- Modulo que executa uma alteração no banco (insert, update, delete...) e não retorna resultado
def manipula_dados(sql):
    con = abre_conexao_bd()
    if con != 0:        
        cursor = con.cursor()     
        cursor.execute(sql)
        con.commit() #este comando salva as alterações realizadas durante a conexão (con). Note que sem ele, as alterações não aparecem após uma nova execução.

        cursor.close()
        con.close()
        print("Operação realizada com sucesso.\n")
    else:
        print("A operação não foi realizada.\n")

#----- Módulo que executa uma consulta e imprime os resultados
def executa_conculta(sql):
    con = abre_conexao_bd()
    if con != 0:        
        cursor = con.cursor()     
        cursor.execute(sql)              
        for linha in cursor.fetchall():
            print(linha)

        cursor.close()
        con.close()
        print("\nfim da impressão.\n\n")
    else:
        print("O select não foi executado.\n")     


#----- PROGRAMA PRINCIPAL -------------------

executa_conculta("select * from aluno")
manipula_dados("insert into aluno (nome, turma_id, status) values ('sebastiao', 1, 'A');")
manipula_dados("update aluno set status = 'A' where id = 2")
executa_conculta("select * from aluno")

# SUGESTÃO: escreva em python o seguinte algoritmo
# digite 1 para consultar dados, 2 para manipular dados e 3 para sair
# enquanto opcao igual a 1 ou 2, faça
#     digite o comando a ser executado
#     se opcao igual a 1
#         executa_consulta(comando)
#     se opcao igual a 2
#         manipula_dados(comando)
#     digite 1 para consultar dados, 2 para manipular dados e 3 para sair

