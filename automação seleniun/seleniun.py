
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import pandas as pd

abrir = webdriver.Chrome()

abrir.get('https://www.google.com.br/')

abrir.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys('Cotação do dolar')
abrir.find_element(By.XPATH, '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)
dolar_valor = abrir.find_element(By.XPATH, '//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute('data-value')

abrir.get("https://www.google.com/")

abrir.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys("cotação euro")
abrir.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input').send_keys(Keys.ENTER)

euro_valor = abrir.find_element(By.XPATH,'//*[@id="knowledge-currency__updatable-data-column"]/div[1]/div[2]/span[1]').get_attribute("data-value")

abrir.get('https://www.melhorcambio.com/ouro-hoje#:~:text=O%20valor%20do%20grama%20do,%C3%A9%20de%20car%C3%A1ter%20exclusivamente%20informativo.')

ouro_valor = abrir.find_element(By.XPATH, '//*[@id="comercial"]').get_attribute('value')

ouro_valor = ouro_valor.replace(',', '.')

print(dolar_valor)
print(euro_valor)
print(ouro_valor)

abrir.quit()

tabela = pd.read_excel('Produtos.xlsx')

print(tabela)

tabela.loc[tabela['Moeda'] == 'Dólar', 'Cotação'] = float(dolar_valor)
tabela.loc[tabela['Moeda'] == 'Euro', 'Cotação'] = float(euro_valor)
tabela.loc[tabela['Moeda'] == 'Ouro', 'Cotação'] = float(ouro_valor)

tabela["Preço de Compra"] = tabela["Preço Original"] * tabela["Cotação"]
tabela["Preço de Venda"] = tabela["Preço de Compra"] * tabela["Margem"]

tabela.to_excel('Produtos_novo.xlsx', index=False)