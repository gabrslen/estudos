import TaxaPercentual

parar_rotina = False
lista_emprestimos = []

while parar_rotina == False:
    devedor = TaxaPercentual.Emprestimo() #Instância da Classe

    if devedor.nome_devedor() == "fim":
        parar_rotina = True

    else:
        devedor.situacao_emprestimo()
        lista_emprestimos.append(devedor)

print(lista_emprestimos)