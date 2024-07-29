print("Bem vindo ao conversor de milhas, para quilometros!")

print("Escreva um valor me milhas:")
milhas = input()
print("Milhas inseridas:", milhas)
# 1 milha = 1.609 kms
km = float(milhas) * 1.609
print(f"{milhas} milhas é igual a {km} quilometros")
