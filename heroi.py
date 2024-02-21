class Heroi:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
    def atacar(self):
        if self.tipo == 'mago':
            ataque = 'magia'
        elif self.tipo == 'guerreiro':
            ataque = 'espada'
        elif self.tipo == 'monge':
            ataque = 'artes marciais'
        elif self.tipo == 'ninja':
            ataque = 'shuriken'
        else:
            ataque = 'um ataque desconhecido'


        mensagem = f'O {self.tipo} {self.nome} atacou usando {ataque}.'
        return(mensagem)
    
heroi1 = Heroi('Gabriel', 19, 'mago')
heroi2 = Heroi('Alan', 30, 'guerreiro')
heroi3 = Heroi('Lucas', 40, 'monge')
heroi4 = Heroi('David', 25, 'ninja')

print(heroi1.atacar())
print(heroi2.atacar())
print(heroi3.atacar())
print(heroi4.atacar())
