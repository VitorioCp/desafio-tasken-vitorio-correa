# 1 - Escreva uma função que receba um valor inteiro como parâmetro de entrada e imprima 
# na tela n linhas conforme estrutura apresentada abaixo. Por exemplo, as seguintes linhas devem 
# ser apresentadas ser o parâmetro de entrada for 10.
# NOTA: Caso seja inserido um valor menor ou igual a zero, uma crítica deverá ser exibida e o processo 
# deverá ser abortado.

valor = int(input("Informe um valor inteiro: "))

if valor <= 0:
    print("Valor inválido")
else:
    for i in range(valor, 0, -1):
        linha = ' '.join(str(j) for j in range(i, 0, -1))
        print(linha)
