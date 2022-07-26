import pyautogui as pg, pyperclip as pc 
import time, pandas as pd

# time.sleep(3)
# a = pg.position()
# print(a)

pg.PAUSE = 1

pg.press('win')
pg.write('chrome')
pg.press("enter")
time.sleep(2)


pc.copy('https://drive.google.com/drive/folders/149xknr9JvrlEnhNWO49zPcw0PW5icxga?usp=sharing')

pg.hotkey('ctrl', 'v')
pg.press("enter")
time.sleep(4)

pg.click(x=474, y=328, clicks=3)

time.sleep(2)

pg.click(x=380, y=375, clicks=1)

pg.click(x=1753, y=185, clicks=1)

pg.click(x=1513, y=639, clicks=1)

time.sleep(6)
#
pg.click(x=1895, y=991, clicks=1)
#
tabela = pd.read_excel(r"C:\Users\Gustavo\Downloads\Vendas - Dez.xlsx")
print(tabela)

quantidade = tabela['Quantidade'].sum()
print(quantidade)
faturamento = tabela['Valor Final'].sum()
print(faturamento)

pg.hotkey('ctrl', 't')  

pg.click(x=1817, y=164, clicks=1)
time.sleep(1.5)

pg.click(x=1587, y=509, clicks=1)
time.sleep(2)

pg.click(x=51, y=229, clicks=1)
time.sleep(2)

pg.write('Gustavo Novais')

pg.press('tab')
pg.press('tab')

pc.copy('Relação de vedas e faturamento')
pg.hotkey('ctrl', 'v')

pg.press('tab')
pc.copy(f'''Prezados, bom dia.

Segue a relação de vendas e faturamento do dia anterior

Vendas: {quantidade}
Faturamento: {faturamento} ''')

pg.hotkey('ctrl', 'v')

pg.hotkey('ctrl', 'enter')