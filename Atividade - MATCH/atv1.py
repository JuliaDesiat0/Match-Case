num = int(input("Digite um número: "))

match num:
    case 1:
        print("Você digitou o número 1.")
    case 2:
        print("Você digitou o número 2.")
    case 3:
        print("Você digitou o número 3.")
    case _:
        print("Outro número")