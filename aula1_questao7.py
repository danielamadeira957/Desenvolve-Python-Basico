import random

def encrypt(lista_nomes):
    #gera uma chave aleatória entre 1 e 10
    n = random.randint (1, 10)
    nomes_criptografados = []

    for nome in lista_nomes:
        nome_cripto = ""
        for c in nome:
            #Transforma o caractere em código Unicode, soma n
            codigo = ord(c) + n

            #garante que o caractere esteja no intervalo visível (33 a 126)
            #se passar de 126, volta para o início do íntervalo (wrap-around)
            if codigo > 126:
                codigo = 33 + (codigo - 127)

                nomes_criptografados.append (nome_cripto)

                return nomes_criptografados, n
            
            #exemplo
            nomes = ["Luana", "JU", "Davi", "Vivi", "Pri", "Luiz"]
            nomes_cript, chave_aleatoria = encrypt (nomes)

            print (f"Nomes: {nomes}")
            print (f"Chave aleatória = {chave_aleatoria}")
            print (f"nomes_cript = {nomes_cript}")