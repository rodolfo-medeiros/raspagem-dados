import sqlite3
import pandas as pd
from playwright.sync_api import sync_playwright

def extracting_data():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=50)
        page = browser.new_page()
        page.goto(
            "https://pt.tradingeconomics.com/brazil/currency",
            wait_until="domcontentloaded",
            timeout=6000
                  )
        print("Carregando página..")
        #localizando a tabela usando a classe
        table = page.locator(".table-heatmap ")
        # pegando todas as linhas da tabela
        rows = table.locator("tr").all()
        table_data = []
        
        for row in rows:
            #extrair o texto dos cabeçalhos e das células (th/td) na linha
            row_text = row.locator("th,td").all_inner_texts()
            table_data.append(row_text)
        browser.close()
    return table_data
    
    

data = extracting_data()
df_currency = pd.DataFrame(data[1:],columns=data[0])

print("Tabela carregada com sucesso!")

df_currency.columns = ["currency","price","null","variation","day","year","date"]
df_currency = df_currency.drop(columns=["null","variation","day","year"])
df_currency["date"] = pd.to_datetime(df_currency["date"])
df_currency["price"] = df_currency["price"].str.replace(",","")
df_currency["price"] = df_currency["price"].astype("float64").round(2)
df_currency["id"] = df_currency["currency"] + "-" + df_currency["date"].dt.strftime("%Y%m%d")
df_currency = df_currency[["id","currency","price","date"]]
print(df_currency.head())


# Abrindo a conexão
conn = sqlite3.connect("currency.db")
#chamando o cursor ("garçom")
cursor = conn.cursor()

# IF NOT EXISTS garante que ele só vai criar a tabela a primeira vez que rodar
query ='''
CREATE TABLE IF NOT EXISTS cotacoes_historico (
    id TEXT PRIMARY KEY,
    currency TEXT NOT NULL,
    price REAL NOT NULL,
    date DATE NOT NULL
    
)   
'''

cursor.execute(query)

# Inserindo os dados 
# if_exists = "append" se a tabela ja existir coloque os dados no final dela.

# traz todos os ids que estão no banco de dados e coloca me uma lista
ids_existentes = pd.read_sql_query("SELECT* FROM cotacoes_historico",conn)["id"].tolist()

#traz apenas os ids novos ou seja, que não estão no banco de dados.
df_filter = df_currency[~df_currency["id"].isin(ids_existentes)]

df_currency.to_sql("cotacoes_historico",conn,if_exists="append",index=False)


print("Inserindo os dados..")

#salva no disco
conn.commit()
cursor.close()
conn.close()






