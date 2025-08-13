# 📜 Descrição do Código

Este código em Python solicita informações sobre um produto (nome, preço e porcentagem de desconto), calcula o valor do desconto e o preço final, e exibe os resultados formatados.

## 🚀 Como funciona
1. O programa pede ao usuário:
   - Nome do produto (`input` como string)
   - Preço do produto (`input` convertido para `float`)
   - Porcentagem de desconto (`input` convertido para `float`)
2. Calcula:
   - Valor do desconto (`preco * (desconto / 100)`)
   - Preço final (`preco - valor_desconto`)
3. Exibe todas as informações organizadas.

## 📌 Código
```python
nome_produto = input("Digite o nome do produto: ")
preco = float(input("Digite o preço do produto: "))
desconto = float(input("Digite a porcentagem de Desconto: "))

valor_desconto = preco * (desconto / 100)
preco_final = preco - valor_desconto

print("==================================================")
print(f"Produto: {nome_produto}")
print(f"Preço: R$ {preco:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço final: R$ {preco_final:.2f}")
print("==================================================")
print("Obrigado por comprar conosco!")
```

## 🖥️ Exemplo de uso
**Entrada:**
```
Digite o nome do produto: Camiseta
Digite o preço do produto: 100
Digite a porcentagem de Desconto: 20
```

**Saída:**
```
==================================================
Produto: Camiseta
Preço: R$ 100.00
Desconto: 20.0%
Valor do desconto: R$ 20.00
Preço final: R$ 80.00
==================================================
Obrigado por comprar conosco!
```

## 🛠️ Observações
- Os valores monetários são formatados com duas casas decimais usando `:.2f`.
- A porcentagem de desconto é informada pelo usuário e pode ser decimal.
- O nome do produto permanece como texto (`string`).





