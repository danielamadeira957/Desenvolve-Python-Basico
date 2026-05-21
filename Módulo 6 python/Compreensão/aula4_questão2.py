frase = input ("Digite uma frase:")

#a lista de vogais da frase, ordenada alfabeticamente
vogais_lista = sorted ([char for char in frase.lower()if char in 'aeiouáéíóúâêîõûãõ'])

#a lista de consoantes da frase (removendo espaços em branco)
consoantes_lista = [char for char in frase.lower() if char.isalpha() and char not in 'aeiouáéíóúâêîõûãõ']

print (f"Vogais: {vogais_lista}")
print (f"Consoantes: {consoantes_lista}")