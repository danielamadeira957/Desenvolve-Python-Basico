n = int (input())

#inicializar as variaveis
soma = 0 #resultado -> somo
cont = 0 #variavel de controle do laço

while cont < n :
    idade  = int (input())
    soma += idade #soma = soma + idade

    #atualizando a variavel de controle do laço
    cont += 1 # cont =  cont + 1

    #imprimir a media
    print (f"A média das idades é{soma/n:.0f}anos")
    