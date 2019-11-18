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
        """ print the state"""
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

    def actions(self, state):
        rows = list(state)
        element = 0
        row_empty = int(rows.index(element)/self.d)
        col_empty = rows.index(element)%self.d #isto vai dar o numero da coluna 0, 1, 2 ...
        actions = []
        if col_empty > 0:
            actions.append('LEFT')
        if col_empty < self.d-1:
            actions.append('RIGHT')
        if row_empty > 0:
            actions.append('UP')
        if row_empty < self.d:
            actions.append('DOWN')
        return actions

    def result(self, state, action):
        rows = list(state)
        element = 0
        row_empty = int(rows.index(element)/self.d)
        col_empty = rows.index(element)%self.d
        print("row: ", row_empty)
        print("col: ", col_empty)
        new_state = state
        if action == 'UP':
            new_row_empty = ((row_empty-1) * self.d)
            new_state = swap(new_state, row_empty, new_row_empty)
        if action == 'DOWN':
            new_row_empty = ((row_empty+1) * self.d)
            new_state = swap(new_state, row_empty, new_row_empty)
        if action == 'LEFT':
            new_col_empty = ((col_empty-1) * self.d)
            new_state = swap(new_state, col_empty, new_col_empty)
        if action == 'RIGHT':
            new_col_empty = ((col_empty+1) * self.d)
            new_state = swap(new_state, col_empty, new_col_empty)
        return new_state

def swap(array, a, b):
    lst = list(array)
    aux = lst[a]
    #print(lst)
    lst[a] = lst[b]
    lst[b] = aux
    return tuple(lst)
