"""
1 - Entrar no sistema da empresa https://dlp.hashtagtreinamentos.com/python/intensivao/login
2 - Fazer Login
3 - Importar Base de Dados
4 - Cadastrar um produto
5 - repetir para mais produtos
"""
import pyautogui
import time
import pandas as pd

# Ajuste global de pausa entre ações do PyAutoGUI
pyautogui.PAUSE = 0.5

# Abrir o navegador (Edge) via menu iniciar
pyautogui.press("win")
pyautogui.write("edge")
pyautogui.press("enter")
pyautogui.sleep(1)

# Acessar a página de login do sistema
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(3)

# Preencher e enviar o formulário de login
pyautogui.click(x=610, y=370)
pyautogui.write("DevOps@gmail.com")
pyautogui.press("tab")
pyautogui.write("123456")
pyautogui.press("enter")

# Entrar na área de cadastro
pyautogui.press("tab")
pyautogui.press("enter")

time.sleep(3)

# Ler a base de produtos
tabela = pd.read_csv("produtos.csv")

print(tabela)

# Para cada linha da tabela, preencher o formulário e enviar
for linha in tabela.index:
    # Focar no primeiro campo do formulário
    pyautogui.click(x=497, y=245)

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

    # Preencher observações apenas quando houver valor (evita escrever 'nan')
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")

    # Enviar cadastro do produto
    pyautogui.press("enter")

    # Rolar a página para garantir visibilidade do próximo formulário
    pyautogui.scroll(10000)