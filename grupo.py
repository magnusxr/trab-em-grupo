print("Qual arma você gostaria de equipar?")
print("1 - Adaga")
print("2 - Espada Longa")
print("3 - Arco e Flecha")
print("4 - Cajado")
print("")
x = input("> ")


if x == "1":
    arma = "Adaga"

elif x == "2":
    arma = "Espada Longa"

elif x == "3":
    arma = "Arco e Flecha"

elif x == "4":
    arma = "Cajado"

else:
    print("Comando não reconhecido.")
    print(x)

print(f"Você escolheu {arma}!")
