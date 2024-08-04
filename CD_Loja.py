import conn 
import pandas as pd


#Importação de bases excel
tabela = pd.read_excel("Cadastro_Lojas.xlsx", "Plan1")


for index, row in tabela.iterrows():
    sql = "INSERT INTO cadastroloja (idLoja,nomeLoja,qtdColaborador,tipo,idLocalidade,gerenteLoja,docGerente) VALUES (%s,%s,%s,%s,%s,%s,%s)"
    val = (row['ID Loja'],row['Nome da Loja'],row['Quantidade Colaboradores'],row['Tipo'],row['id Localidade'],row['Gerente Loja'],row['Documento Gerente'])
    conn.cursor.execute(sql,val)
    conn.conexao.commit()


print("Dados inseridos com sucesso")

conn.cursor.execute('select * from cadastroloja')
for x in conn.cursor:
    print(x)

conn.fechar()