class MeuLutador:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo

    def atacar(self):
        if self.tipo == "guerreiro":
            print(f"O {self.tipo} atacou usando espada!")
        elif self.tipo == "mago":
            print(f"O {self.tipo} atacou usando magia!")
        elif self.tipo == "monge":
            print(f"O {self.tipo} atacou usando artes marciais!")
        elif self.tipo == "ninja":
            print(f"O {self.tipo} atacou usando shuriken!")
        else:
            print("Escolha novamente o tipo do seu lutador: guerreiro, mago, monge ou ninja.")
            self.tipo = input("Seu lutador será guerreiro, mago, monge ou ninja?: ")


print("Seja bem-vindo à arena da Terrargucci!")
nome_lutador = input("Digite seu nome: ")
idade_lutador = input("Digite a sua idade: ")
tipo_lutador = input("Seu lutador será guerreiro, mago, monge ou ninja?: ")

heroi_escolhido = MeuLutador(nome_lutador, idade_lutador, tipo_lutador)

heroi_escolhido.atacar()