import pandas as pd

class Emprestimo():
    
    nome = ""
    valor = 0
    quant = 0
    perc = 0
    perc_recebido = 0
    pago = 0
    mont = 0
    perc_atual = 0
    
    def nome_devedor(self):
        self.nome = input('Nome de quem pegou emprestado: ')
        return self.nome

    def situacao_emprestimo(self):
        self.valor = float(input('\nValor total emprestado: R$'))
        self.quant = float(input('Quantia recebida no mês: R$'))
        self.perc = float(input('Percentual pago anteriormente: '))
        self.perc_recebido = (100*self.quant/self.valor)
        self.pago = float(self.valor/(100/self.perc))
        self.mont = self.pago + self.quant
        self.perc_atual = self.perc + self.perc_recebido

        print('\nA quantia recebida corresponde a ', str(self.perc_recebido)+'% do tatal bruto.')
        print('O percentual pago anteriormente totaliza R$'+str(self.pago))
        print('O montante recebido atualizado é de: R$'+str(self.mont))
        print('O percentual recebido atualizado é:', str(self.perc_atual)+'%\n')


    def __str__(self):
            return "{}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}".format(self.nome, self.valor, self.quant, self.perc, self.perc_recebido, self.pago, self.mont, self.perc_atual)
    def __repr__(self):
            return "{}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}/{:0.2f}".format(self.nome, self.valor, self.quant, self.perc, self.perc_recebido, self.pago, self.mont, self.perc_atual)
    

#parar_rotina = False
#lista_emprestimos = []

#while parar_rotina == False:
#    devedor = Emprestimo() #Instância da Classe

#    if devedor.nome_devedor() == "fim":
#        parar_rotina = True

#    else:
#        devedor.situacao_emprestimo()
#        lista_emprestimos.append(devedor)
    
#resultado.to_csv("AppDesenvolvimento\Estudos\Exemplos\Emprestimo\lista_emprestimos.csv")
#resultado = pd.DataFrame(lista_emprestimos)
#print(resultado)