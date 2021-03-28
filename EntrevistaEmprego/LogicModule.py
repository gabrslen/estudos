import DataModule

ano_corrente = int(input("O ano corrente é: "))
parar_repeticao = False
lista_entrevistados = []

while parar_repeticao == False:
    entrevistado = DataModule.Entrevista() #Instancia da classe

    if entrevistado.pergunta_nome() == "fim":
        parar_repeticao = True
    else:
        entrevistado.pergunta_idade(ano_atual=ano_corrente)
        lista_entrevistados.append(entrevistado)

print(lista_entrevistados)