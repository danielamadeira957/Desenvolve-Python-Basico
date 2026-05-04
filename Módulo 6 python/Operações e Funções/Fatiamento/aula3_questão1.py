numeros = []

print ("Digite pelo menos 4 números (ou 'sair' para finalizar):")
while True:
    entrada = input ("> ")
    if entrada.lower () == 'sair':
        if len (numeros) < 4:
            print ("Por favor, insira pelo menos 4 números.")
            continue
        break
    try:
        numeros.append (int(entrada))
    except ValueError:
        print ("Entrada inválida. Digite um número inteiro.")

        #impressões utilizando fatiamento
        print(f"A lista original: {numeros}")
        print(f"Os 3 primeiros elementos: {numeros [:3]}")
        print(f"Os 2 últimos elementos: {numeros [-2:]}")
        print(f"A lista invertida: {numeros [::-1]}")
        print(f"Os elementos de índice par: {numeros [::2]}")
        print(f"Os elementos de índice ímpar: {numeros [1::2]}")