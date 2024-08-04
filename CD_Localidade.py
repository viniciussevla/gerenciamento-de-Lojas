import conn 
import pandas as pd


#Importação de bases excel
tabela = pd.read_excel("Cadastro_Localidades.xlsx", "Plan1")


for index, row in tabela.iterrows():
    sql = "INSERT INTO cadastrolocalidade (idLocalidade,pais,continente) VALUES (%s,%s,%s)"
    val = (row['ID Localidade'],row['País'],row['Continente'])
    conn.cursor.execute(sql,val)
    conn.conexao.commit()


print("Dados inseridos com sucesso")

conn.cursor.execute('select * from cadastrolocalidade')
for x in conn.cursor:
    print(x)

conn.fechar()