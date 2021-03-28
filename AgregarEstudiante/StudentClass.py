class StudentClass:
    matricula=''
    nome=''
    telefone=''
    idade=0
    peso=0.0

    def __init__(self, matricula, nome):
        self.matricula = matricula
        self.nome = nome

    def getMatricula(self):
        return self.matricula

    def getNome(self):
        return self.nome
        
    def getTelefone(self):
        return self.telefone

    def getIdade(self):
        return self.idade

    def getPeso(self):
        return self.peso

    def setNome(self, novo_nome):
        self.nome = novo_nome

    def setTelefone(self, novo_telefone):
        self.telefone = novo_telefone

    def setIdade(self, novo_idade):
        self.idade = novo_idade

    def setPeso(self, novo_peso):
        self.peso = novo_peso