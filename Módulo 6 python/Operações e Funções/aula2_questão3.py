import random

#preencher duas listas com 20 valores aleatórios entre 0 e 50
lista1 = [random.ramdint (0, 50) for _ in range (20)]
lista2 = [random.ramdint (0, 50) for _ in range (20)]

#criar a lista de intersecção sem duplicatas
#convertendo para set, garantimos que os elementos sejam únicos
interseccao = sorted (list (set(lista1) & set(lista2)))

#contagem de vezes que cada elemento da intersecção aparece nas listas originais
contagem = {}
for num in interseccao:
    contagem [num] = (lista1.count(num), lista2.count(num))

#impressão dos resultados
print (f"Lista 1 :{lista1}")
print (f"Lista 2 :{lista2}")
print (f"Intersecção Ordenada: {interseccao}")

print ("\nContagem (Elemento: [Lista1, Lista2]):")
for num, counts in contagem.items ():
    print (f"{num}: {list(counts)}")