# 4 - Escreva um programa que leia um arquivo texto (.txt) escolhido pelo usuário. Após 
# a leitura do arquivo, o programa deverá exibir qual linha possui mais vogais e qual linha possui 
# mais consoantes. Por simplicidade admita que o arquivo conterá apenas letras (sem acentos ou ç) e 
# espaços em branco. Caso ocorra empate, qualquer uma das linhas poderá ser exibida.

import tkinter as tk
from tkinter import filedialog

def contar_vogais_consoantes(linha):
    vogais = "aeiouAEIOU"
    consoantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
    
    qtd_vogais = sum(1 for letra in linha if letra in vogais)
    qtd_consoantes = sum(1 for letra in linha if letra in consoantes)
    
    return qtd_vogais, qtd_consoantes

root = tk.Tk()
root.withdraw()

caminho_arquivo = filedialog.askopenfilename(title="Selecione um arquivo TXT", filetypes=[("Arquivos de Texto", "*.txt")])

if caminho_arquivo:
    try:
        with open(caminho_arquivo, "r", encoding="utf-8") as arquivo:
            linhas = arquivo.readlines()

        if not linhas:
            print("O arquivo está vazio.")
        else:
            max_vogais = max_consoantes = 0
            linha_mais_vogais = linha_mais_consoantes = ""

            for linha in linhas:
                linha = linha.strip() 
                qtd_vogais, qtd_consoantes = contar_vogais_consoantes(linha)


                if qtd_vogais > max_vogais:
                    max_vogais = qtd_vogais
                    linha_mais_vogais = linha
                
                if qtd_consoantes > max_consoantes:
                    max_consoantes = qtd_consoantes
                    linha_mais_consoantes = linha

            print("\n📜 Relatório 📜")
            print(f" Linha com mais vogais ({max_vogais} vogais):\n {linha_mais_vogais}")
            print(f" Linha com mais consoantes ({max_consoantes} consoantes):\n {linha_mais_consoantes}")

    except Exception as e:
        print(f"Erro ao abrir o arquivo: {e}")
else:
    print("Nenhum arquivo selecionado.")
