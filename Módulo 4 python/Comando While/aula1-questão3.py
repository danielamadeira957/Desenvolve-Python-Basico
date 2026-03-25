#Entrada de dados: leia n1, n2, n3
n1 = float (input("Digite a nota 1:"))
n2 = float (input("Digite a nota 2:"))
n3 = float (input("Digite a nota 3:"))

#Processamento:  m = (n1+n2+n3)/3
m = (n1 + n2 + n3) /3

#Estrutura de decisão
if m >= 60:
#Se m >= 60 for Sim
    print ("Aprovado")
elif m>= 40:
    #Se m>= 60 for Não e m>=40 for Sim
    print("Recuperação")
else:
    #Se ambas forem Não
    print("Reprovado")

    #Finalização: Imprima "Fim"
    print ("Fim")