login = str(input("Digite seu login: "))
senha = str(input("Digite a sua senha: "))
match(login, senha):
    case ("Julia", "0506"):
        print("Usuario logado com sucesso")

    case ("Artur", "2101"):
        print("Administradora logada com sucesso")

    case _:
        print("Login ou senha incorreto")