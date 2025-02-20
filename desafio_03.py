# 3 - Escreva um programa que leia números positivos do teclado, até que o número zero seja digitado. Após, o programa deverá exibir um relatório na tela descrevendo os seguintes itens:
# a) Quantos números foram lidos.
# b) O maior numero lido.
# c) A média dos números lidos.
# d) O menor número ímpar lido (caso algum número ímpar tenha sido digitado).
# e) A quantidade de vezes que cada número ocorreu. Exemplo: "O número 7 ocorreu 2 vezes." "O número 13 ocorreu 8 vezes".
# DICA: Use vetores.


def coletar_numeros():
    numeros = []
    while True:
        try:
            num = int(input("Digite um número (0 para sair): "))
            if num == 0:
                break
            if num > 0:
                numeros.append(num)
            else:
                print("Por favor, digite apenas números positivos.")
        except ValueError:
            print("Entrada inválida. Digite um número inteiro positivo.")
    return numeros

def analisar_numeros(numeros):
    if not numeros:
        print("Nenhum número foi digitado.")
        return
    
    qtd_numeros = len(numeros)
    maior_numero = max(numeros)
    media = sum(numeros) / qtd_numeros
    
    impares = [num for num in numeros if num % 2 != 0]
    menor_impar = min(impares) if impares else "Nenhum número ímpar foi digitado."
    
    ocorrencias = {}
    for num in numeros:
        ocorrencias[num] = ocorrencias.get(num, 0) + 1
    
    print("\nRelatório:")
    print(f"a) Quantos números foram lidos: {qtd_numeros}")
    print(f"b) O maior número lido: {maior_numero}")
    print(f"c) A média dos números lidos: {media:.2f}")
    print(f"d) O menor número ímpar lido: {menor_impar}")
    print("e) Quantidade de vezes que cada número ocorreu:")
    for num, qtd in ocorrencias.items():
        print(f"   - O número {num} ocorreu {qtd} vezes.")

numeros_lidos = coletar_numeros()
analisar_numeros(numeros_lidos)
