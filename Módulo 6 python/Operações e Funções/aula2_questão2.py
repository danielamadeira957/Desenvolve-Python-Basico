import random

#gera aleatoriamente um valor entre 5 e 20
num_elementos = random.randint(5, 20)

#gera valores aleatorios entre 1 e 10 e armazena na lista 'elementos'
elementos = [random.randint(1, 10)for _ in range (num_elementos)]

#cálculos
soma = sum(elementos)
media = soma / num_elementos

#impressão dos resultados
print (f"Lista elementos: {elementos}")
print (f"Soma dos valores: {soma}")
print (f"Média dos valores: {media:.2f}")