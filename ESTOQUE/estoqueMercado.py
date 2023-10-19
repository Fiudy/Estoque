import biblioteca.funcoes as f


while True:
    print("1- Inclusão de Equipamentos")
    print("2- Alteração de Equipamentos")
    print("3- Exclusão de Equipamentos")
    print("4- Relatório Geral de Equipamentos")
    print("5- Relatório Específico de Equipamentos")
    print("6- SAIR")

    opcao = input("")

    match (opcao):
        case '1':
            f.incluir()
        case '2':
            f.alterar()
        case '3':
            f.excluir()
        case '4':
            f.relGeral()
        case '5':
            f.relEsp()
        case '6':
            exit()