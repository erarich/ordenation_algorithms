import random

def gerar_lista(tamanho, tipo):
    if tipo == 'ordenada':
        return list(range(tamanho))
    elif tipo == 'inversa':
        return list(range(tamanho, 0, -1))
    elif tipo == 'aleatoria':
        lista = list(range(tamanho))
        random.shuffle(lista)
        return lista
    else:
        raise ValueError("Tipo de lista desconhecido. Use 'ordenada', 'inversa' ou 'aleatoria'.")

# Exemplo de uso
lista_aleatoria_1000 = gerar_lista(1000, 'aleatoria')
lista_ordenada_10000 = gerar_lista(10000, 'ordenada')
lista_inversa_50000 = gerar_lista(50000, 'inversa')
