cor = str(input("Digite uma cor: "))

match cor:
    case "vermelho":
        print("Vermelho")
    case "azul":
        print("Azul")
    case "verde":
        print("Verde")
    case _:
        print("Cor desconhecida")

