from tkinter import W


l = list()
l = [1, 2, 3, 5]
l.append(7)
l.pop(2)
t = tuple()
t = (1, 2, 3, 3, 5, 'abc')
t[2]
# HASHABLE ( HASHEÁVEIS )
# HASH MAP -> 1 ->(HASHING)-> djnsaid2913672e9 
s = set()
s = {1, 2, 4, 5}
d = dict()
d = {1: 'um', 2: 'dois'}
d[1]
d = dict(a=1, b=2, c=3)
# filas, pilhas, deques, OrderedDict, DefaultDict ...
# args, kwargs (key word arguments)
def minha_funcao(a, b, c):
    return a + b + c
args = [1, 2, 3]
print(minha_funcao(1, 2, 3))
print(minha_funcao(*args))

# loop ( while , for )
i = 0
while i < 10:
    print(i)
    i += 1

for i in range(10):
    print(i)

# 4 PERGUNTAS A, B, C, D
a, b = [0, 1]

alterantivas = ['A', 'B', 'C', 'D']
for idx, elem in enumerate(alterantivas):
    print(alterantivas[idx])

while True:
    print('oi')
    break

for i in range(10):
    if i == 3:
        break
    print(i)

a = 3

d = {'amor': 'amar', 'abacate': 'banana'}
for valor in d.values():
    print(f'Chave é: {valor}')


# tudo é um objeto (é uma instância de uma classe)
# método é uma função de uma classe

class Veiculo:
    def __init__(self, num_rodas, som_da_buzina):
        self.rodas = num_rodas
        self.som = som_da_buzina

    def buzinar(self):
        print(self.som)


class Carro(Veiculo):
    def __init__(self, marca, ano, som_da_buzina='honk honk'): # construtor
        super().__init__(4, som_da_buzina)
        self.marca = marca
        self.ano = ano

    # sobrescrita de método
    def buzinar(self):
        print('vrau')

    def __str__(self):
        return f'Meu carro é um {self.marca} do ano {self.ano}'

hb20 = Carro('HB20S', 2013)
pegout = Carro('Pegout 207', 2009)
print(hb20)
print(pegout)


class CarrinhoDeCompras():
    def __init__(self):
        self.lista = []

    def ja_ta_no_carrinho(self, item):
        for compra in self.lista:
            if compra == item:
                return True
        return False
    
    def coloca_no_carrinho(self, item):
        self.lista.append(item)


meu_carrinho = CarrinhoDeCompras()


