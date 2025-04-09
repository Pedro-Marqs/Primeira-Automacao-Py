import pyautogui
import time

pyautogui.PAUSE = 0.5

# Abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
time.sleep(1)

# Abrir o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Fazer o Login
pyautogui.click(x=1120, y=483)
pyautogui.write("emailteste@gmail.com")
pyautogui.press("tab")
pyautogui.write("teste!#123")
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)

# Importar a base de dados
import pandas

tabela = pandas.read_csv("produtos.csv")

# Cadastar os produtos

for linha in tabela.index:
    pyautogui.click(x=722, y=319)

    
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)
    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)
    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)
    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)
    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.scroll(1000)