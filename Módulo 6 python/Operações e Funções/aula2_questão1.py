import random

#Construção da lista de valores aleatórios
lista_original = [random.randint(-100, 100)for _ in range (20)]

#A lista ordenada, sem modificar a lista original
lista_ordenada = sorted (lista_original)

#encontrando os índices do maior e menor valor
índice_maior = lista_original.index(max(lista_original))
índice_menor = lista_original.index(min(lista_original))

#impressão dos resultados na ordem estabelecida
print(f"A lista ordenada: {lista_ordenada}")
print(f"A lista original: {lista_original}")
print(f"O índice do maior valor da lista: {índice_maior}")
print(f"O índice do menor valor da lista: {índice_menor}")