# 2 - Escreva uma função que receba um parâmetro do tipo string e retorne uma string como resultado. 
# A função deverá "compactar" a string recebida como parâmetro de entrada. A compactação funcionará 
# escrevendo o caractere encontrado seguido da quantidade de vezes que ele ocorre em sequência.
# Ex.:
# Parâmetro de entrada: jjjjooaoo
# Resultado da função: j4o2ao2

palavra = input("Escreva uma mensagem: ")

if not palavra:
    print("Mensagem vazia, escreva uma palavra!")
else:
    def compactar_string(s):
        if not s:
            return ""
        
        resultado = ""
        contador = 1
        
        for i in range(len(s) - 1):
            if s[i] == s[i + 1]:
                contador += 1
            else:
                resultado += s[i] + (str(contador) if contador > 1 else "")
                contador = 1
        
        resultado += s[-1] + (str(contador) if contador > 1 else "")
        
        return resultado

    print(compactar_string(palavra))