import random
import os

def gerar_lista(tamanho, tipo):
    if tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'inversa':
        return list(range(tamanho - 1, -1, -1))
    elif tipo == 'aleatoria':
        lista = list(range(tamanho))
        random.shuffle(lista)
        return lista
    else:
        raise ValueError("Tipo de lista desconhecido. Use 'ordenada', 'inversa' ou 'aleatoria'.")

def salvar_lista_em_arquivo(lista, nome_arquivo):
    with open(nome_arquivo, 'w') as arquivo:
        for item in lista:
            arquivo.write(f"{item}\n")

# Exemplos de uso
lista_aleatoria_1000 = gerar_lista(1000, 'aleatoria')
lista_ordenada_10000 = gerar_lista(10000, 'ordenada')
lista_inversa_50000 = gerar_lista(50000, 'inversa')

# Salvando as listas em arquivos
salvar_lista_em_arquivo(lista_aleatoria_1000, 'lista_aleatoria_1000.txt')
salvar_lista_em_arquivo(lista_ordenada_10000, 'lista_ordenada_10000.txt')
salvar_lista_em_arquivo(lista_inversa_50000, 'lista_inversa_50000.txt')

print("Arquivos gerados com sucesso.")
