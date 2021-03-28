class Computador:

    def __init__(self, a, m, p):
        self.a = a
        self.m = m
        self.p = p

#    def Ligar(self):
#        print('Ligando')

#    def Desligar(self):
#        print('Desligando')  

    def ExibirInfo(self):
        print(self.a, self.m, self.p)

c1 = Computador('Asus','8gb','NVidia')
c2 = Computador('Dell','8gb','GeForce')
c3 = Computador('Positivo','16gb','Nao identificada')

c1.ExibirInfo()
#c1.Ligar()
#c1.Desligar()

c2.ExibirInfo()
#c2.Desligar()

c3.ExibirInfo()
#c3.Ligar()