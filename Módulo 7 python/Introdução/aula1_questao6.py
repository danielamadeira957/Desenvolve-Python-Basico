frase = input("Digite uma frase:").lower()
objetivo = input ("Digite uma palavra objetivo:").lower()

#Função para checar se é anagrama
def e_anagrama (p1, p2):
    return sorted(p1) == sorted(p2)

#limpa a frase de pontuações simples e separa as palavras
palavras = frase.replace (",", " ").replace (",", " ").split()
anagramas_encontrados = [p for p in palavras if e_anagrama (p, objetivo)]

print (f"Anagramas: {anagramas_encontrados}")