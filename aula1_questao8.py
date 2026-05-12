cpf = input ("Digite o CPF (xxx.xxx.xxx-xx):").replace('.', '').replace('-', '')

#validação do primeiro dígito
soma = 0
multiplicador = 10
for i in range (9):
    soma += int(cpf[i]) * multiplicador
    multiplicador -= 1

    resto =  soma % 11
    digito1 = 0 if resto < 2 else 11 - resto

    #Para o segundo dígito, repete-se a l´gica com peso de 11 a 2,
    #incluindo o primeiro dígito calculado.