hello = str(input("Insira a primeira string: "))
world = str(input("Insira a segunda string: "))

match hello, world:
    case ("hello", _):
        print("A primeira string é 'hello' e a segunda é qualquer outra coisa.")
    case (_, "world"):
        print("A segunda string é 'world' e a primeira é qualquer outra coisa.")
    case (hello, world):
        print("Ambas as strings são iguais.")
    case _:
        print("Nenhuma das condições é satisfeita.")