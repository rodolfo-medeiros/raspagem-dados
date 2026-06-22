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



# Conectando ao banco de dados
conn = sqlite3.connect("database.db")
cursor = conn.cursor()




