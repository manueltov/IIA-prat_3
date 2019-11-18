"""Exercicio 1 b)"""

from searchPlus import *

class Problema3Jarros(Problem):
    """Problem about pouring water between jugs to achieve some water level.
    Each state is a tuples of water levels. In the initialization, also provide a tuple of
    jug sizes, e.g. PourProblem(initial=(0, 0, 0), goal=6, sizes=(7, 8, 3)),
    which means three jugs of sizes 7, and 3, initially all empty, with the goal
    of getting a level of 6 in one of the jugs."""

    def __init__(self,initial=(0,0,0),goal=6,capacidades=(7,8,3)):
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
