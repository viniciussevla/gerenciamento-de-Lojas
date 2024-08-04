import mysql.connector

conexao = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='vendas',
)
cursor = conexao.cursor()

def inserir(sql,val):
    cursor.execute(sql,val)
    
def fechar():
    cursor.close()
    conexao.close()
    
def exibirTabelas():
    cursor.execute("SHOW TABLES")
    for x in cursor:
        print(x)
