#faça um programa que se o usuario inserir 1 ele escolhe a classe barbaro, se 2 escolhe a classe mago, se 3 escolhe a classe arqueiro.


c = input("Qual será a sua classe escolhida?\n 1 = Bárbaro\n 2 = Mago\n 3 = Arqueiro\n > ")

if (c == "1"):
    classe = "Bárbaro"

elif (c == "2"):
    classe = "Mago"

elif (c == "3"):
    classe = "Arqueiro"

else: 
    print("Comando não reconhecido.")

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

print(f"Você é um {classe} com a arma {arma}!")