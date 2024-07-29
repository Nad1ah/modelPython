print("*********************************")
print("***         BEM-VINDOS        ***")
print("****    A LOJA DE ANIMAIS    ****")
print("*********************************")

num_dogs = 10
num_cats = 15
num_birds = 27

soma_amimais = num_cats + num_birds + num_dogs

print("Por favor escreva seu nome:")
name = input()
print("Por favor escreva seu sobrenome:")
sobrenome = input()

nome_completo = name + " " + sobrenome

print("Obrigada por visitarnos,", nome_completo)
print("Atualmente contamos com:")
print("Cachorros:", num_dogs, "Gatos:", num_cats, "Passaros:", num_birds)
print("Em total temos", soma_amimais, "animais.")
