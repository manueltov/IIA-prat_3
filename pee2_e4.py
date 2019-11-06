from searchPlus import *

class PuzzleN(Problem):
    """ O problema das N=dxd-1 peças deslizantes, num tabuleiro quadrado de dimensão dxd
    onde um dos quadrados está vazio, tentando atingir uma configuração particular
    Um estado é representado por um tuplo de dimensão dxd.
    As peças são representadas pelos próprios números e a peça vazia por 0.
    O objectivo por omissão no caso de 3x3:
        1 2 3
        4 5 6 ==> (1, 2, 3, 4, 5, 6, 7, 8, 0)
        7 8 _
    Existe um atributo d que representa a dimensão do quadrado, 3 no caso do puzzle de 8
    """


    def __init__(self, initial=(0, 1, 2, 3, 4, 5, 6, 7, 8), goal=(1, 2, 3, 4, 5, 6, 7, 8, 0)):
        self.initial, self.goal = initial, goal
        self.d = int(math.sqrt(len(initial)))

    def display(self, state):
        """ print the state please"""
        output=""
        for i in range(self.d * self.d):
            ch = str(state[i])
            if ch == "0":
                ch = '_'
            output += ch + " "
            i = i+1
            if i % self.d == 0:
                output += "\n"
        print(output)

    def actions (self, estado) :
        """As acções executáveis neste estado."""
        """ver indice do zero e se eles estiver nos conjuntos de d elementos
        ate ao conjunto d-1 entao ele pode descer, se estiver do d ao 1 ele
        pode subir, e equivalente com posicao no conjunto para saber se
        direita ou esquerda"""
        return ()

    def result(self, state, action) :
        """resultado de fazer tal accao, devolve a nova lista"""
        """chama metodo swap"""
