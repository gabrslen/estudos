class ClasseExemplo:
    def __init__(self, atributo_1, atributo_2):
        self.atributo_1 = atributo_1
        self.atributo_2 = atributo_2

    def MetodoExemplo(self):
        print(self.atributo_1, self.atributo_2)

instancia = ClasseExemplo('Hello', 'World')
instancia.MetodoExemplo()

