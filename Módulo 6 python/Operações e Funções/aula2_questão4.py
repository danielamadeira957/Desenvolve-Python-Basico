#Solicita o tamanho e os elementos da primeira lista
n1 = int(input("Digite a quantidade de elementos da lista 1:"))
lista1 = []
print (f"Digite os {n1} elementos da lista 1:")
for _ in range (n1):
    lista1.append (int(inpunt()))

    #solicita o tamanho e os elemenos da segunda lista
    n2 = int(input("Digite a quantidade de elementos da lista 2:"))
    lista2 = []
    print (f"Digite os {n2} elementos da lista 2:")
for _ in range (n2):
    lista2.append (int(input()))

#lógica de intercalação
lista_intercalada = []
i = 0

#intercalada enquanto houver elementos em ambas as listas
while i < len (lista1) and i < len (lista2):
    lista_intercalada.append(lista1[i])
    lista_intercalada.append(lista2[i])
    i += 1

    #adiciona o restante da lista que for maior
    lista_intercalada.extend(lista1[i:])
    lista_intercalada.extend(lista2[i:])

    #exibe o resultado formatado
    print("Lista Intercalada:", *lista_intercalada)