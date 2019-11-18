from pee2_e1 import *

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
