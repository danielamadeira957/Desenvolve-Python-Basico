numero = input ("Digite o número:")

#remove hífens se o úsuario digitar
numero = numero.replace ("-", " ")

#adiciona o 9 na frente se tiver 8 dígitos
if len (numero) == 8:
    numero = "9" + numero

#formata com o hífen
numero_formatado = f"{numero[:5]}-{numero[5:]}"
print (f"Número completo: {numero_formatado}")