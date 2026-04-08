#Leia n (quantidade de números a serem comparados)
n = int(input("Digite a quantidade de números(n):"))

#Inicializa a variavel 'maior' com 0
maior = 0

#Enquanto n > 0 (Estrutura de repetição/decisão)
while n > 0:

#Leia x
x = int(input("Digite um número (x):"))

#Se x > maior (decisão interna)
if x > maior :

#Sim: maior recebe o valor de x 
maior = x

#n = n - 1 (Decrementa o contador para evitar loop infinito)
n = n - 1

#Quando n não for mais > 0, imprima maior
print (f"O maior valor digitado foi:{maior}")