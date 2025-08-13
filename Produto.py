nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de Desconto: "))

valor_desconto = preco *(desconto / 100)
preco_final = preco - valor_desconto

print("==================================================")
print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print("==================================================")
print("Obrigado por comprar conosco!")