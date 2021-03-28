from StudentClass import *

estudante = None

while True:
    print("\n\nMENU\n")
    print("1. MATRICULAR UM ALUNO")
    print("2. MODIFICAR OS DADOS")
    print("3. VER DADOS DO ALUNO")
    print("4. SAIR")
    option = input("Selecione uma opção: ")

    if (option=='1'):
        print("Dados básicos do Aluno (Defiitivos): ")
        matricula = input("Matrícula: ")
        nome = input("Nome do Aluno:")
        estudante = StudentClass(matricula, nome)

    elif (option=='2'):
        while True:
            print("\n\nMENU DE EDIÇÃO\n")
            print("1. ATUALIZAR TELEFONE")
            print("2. ATUALIZAR IDADE")
            print("3. ATUALIZAR PESO")
            print("4. VOLTAR AO MENU ANTERIOR")
            option2 = input("Selecione uma opção: ")
            
            if (option2=='1'):
                telefone = input("Telefone: ")
                estudante.setTelefone(telefone)

            elif (option2=='2'):
                idade = input("Idade: ")
                estudante.setIdade(idade)

            elif (option2=='3'):
                peso = input("Peso: ")
                estudante.setPeso(peso)

            elif (option2=='4'):
                break

    elif (option=='3'):
        print("\n\nDADOS DO ESTUDANTE:\n")
        print("Matrícula: "+estudante.getMatricula())
        print("Nome: "+estudante.getNome())
        print("Telefone: "+estudante.getTelefone())
        print("Idade: "+estudante.getIdade())
        print("Peso: "+estudante.getPeso())

    elif (option=='4'):
        print("FINALIZANDO O APLICATIVO.")
        break

    else:
        print("OPÇÃO INVÁLIDA, Digite uma opção do Menu.")
