registro = {}
status = ''


def salvar_login():
    with open('registro.txt', 'w') as r:
        print(registro, file=r)


def menu():
    status = input(
        "Você já está cadastrado? Responda com 1 para sim e 2 para não. Pressione 0 para sair. >>")
    if status == '1':
        usuarioCadastrado()
    elif status == '2':
        usuarioNovo()
    elif status == '0':
        print("Obrigado por utilizar nossa plataforma.")
        quit()
    else:
        print("Comando inválido. Tente novamente.")


def usuarioCadastrado():
    login = input('Informe seu login: ')
    senha = input('Informe sua senha: ')

    if login in registro and registro[login] == senha:
        print('\nAcesso permitido!\n')
    else:
        print('\nLogin ou senha incorretos. Tente novamente.')


def usuarioNovo():
    criarLogin = input("Informe o login que quer usar para criar a conta: ")

    if criarLogin in registro:
        print("\nLogin ja existente\n")
    else:
        criarSenha = input("Informe a senha: ")
        registro[criarLogin] = criarSenha
        print("Usuário registrado!")
    salvar_login()


while True:
    menu()
