class Entrevista():

    nome = ""
    ano_informado = 0
    idade = 0

    def pergunta_nome(self):
        self.nome = input("Nome do candidato: ")
        print("O nome é '" + self.nome + "'")
        return self.nome

    def pergunta_idade(self, ano_atual=2021):
        self.ano_informado = int(input("Ano de nascimento de " + self.nome + ":"))
        self.idade = ano_atual - self.ano_informado
        print(self.nome,"tem",self.idade,"anos.")
        #return (self.ano_informado, self.idade)

# Funçoes restritas já estão imbutidas na liguagem py, a primeira recebe os valores e retorna
    def __str__(self):
        return "{}/{}".format(self.nome, self.idade)
    def __repr__(self):
        return"Nome: {} - Idade: {}\n".format(self.nome, self.idade)