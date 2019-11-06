from searchPlus import *

class ProblemaJarros(Problem):
    """Problem about pouring water between jugs to achieve some water level.
    Each state is a tuples of water levels. In the initialization, also provide a tuple of
    jug sizes, e.g. PourProblem(initial=(0, 0), goal=3, sizes=(7, 5)),
    which means two jugs of sizes 7 and 5, initially both empty, with the goal
    of getting a level of 3 in either jug."""

    def __init__(self,initial=(0,0),goal=3,capacidades=(7,5)):
        super().__init__(initial,goal)
        self.capacidades = capacidades

    def actions(self, estado):
        """As acções executáveis neste estado."""
        jarros = range(len(estado))
        return ([('Enche', i+1)    for i in jarros if estado[i] < self.capacidades[i]] +
                [('Esvazia', i+1)    for i in jarros if estado[i]] +
                [('Verte', i+1, j+1) for i in jarros if estado[i] for j in jarros if i != j])

    def result(self, estado, accao):
        """O estado sofre accao e passa a ser:."""
        resultado = list(estado)  # converte tuplo em lista
        a, i, *_ = accao
        i = i-1  # O jarro i correspoinde à posição i - 1
        if a == 'Enche':   # Enche jarro i até capacidade
            resultado[i] = self.capacidades[i]
        elif a == 'Esvazia': # Esvazia i
            resultado[i] = 0
        elif a == 'Verte': # Verte i em j
            j = accao[2]-1  # o jarro j corresponde à posição j - 1
            quantidade = min(estado[i], self.capacidades[j] - estado[j])
            resultado[i] -= quantidade
            resultado[j] += quantidade
        return tuple(resultado)

    def is_goal(self, estado):
        """True if the goal level is in any one of the jugs."""
        return self.goal in estado

    def exec(self):
        prob_jarros = ProblemaJarros()
        print("Estado Inicial:",prob_jarros.initial)
        print('Capacidades dos jarros:',prob_jarros.capacidades)
        print("O objectivo é medir ",prob_jarros.goal, "litros")
        prob_jarros.actions(prob_jarros.initial)
        e1 = prob_jarros.result(prob_jarros.initial,('Enche', 1))
        print(e1)
        prob_jarros.actions(e1)
        e2 = prob_jarros.result(e1,('Verte',1,2))
        print(e2)
        e3 = prob_jarros.result(e2,('Enche',1))
        print(e3)
        custo = 0
        e0 = prob_jarros.initial
        print("Comecemos:",e0,", com custo =",custo)
        e1 = prob_jarros.result(e0,('Enche',2))
        custo = prob_jarros.path_cost(custo,prob_jarros.initial,('Enche',2),e1)
        print("Vamos encher o segundo jarro:",e1, ", com custo =",custo)
        e2 = prob_jarros.result(e1,('Verte',2,1))
        custo = prob_jarros.path_cost(custo,prob_jarros.initial,('Verte',2,1),e1)
        print("Vamos verter o jarro 2 em jarro 1:",e2, ", com custo =",custo)
