comprimento = int(input("digite o comprimento em metros:"))
largura = int(input("digite a largura em metros:"))
preco_m2 = float(input("preço do metroquadrado R$:"))

area_m2 = comprimento * largura
preco_total = preco_m2 * area_m2

print(f"O terreno possui {area_m2} e custa R${preco_total:,.2f}")