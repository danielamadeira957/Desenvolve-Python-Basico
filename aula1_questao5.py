frase = input ("Digite uma frase:")
vogais_alvo = "aeiouAEIOU"
indices = []

for i in range (len(frase)):
    if frase [i] in vogais_alvo:
        indices.append(i)

print(f"{len(indices)} vogais")
print (f"Índices {indices}")