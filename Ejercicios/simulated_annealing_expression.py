from node import Node
import numpy as np

def simulated_annealing_expresion(value:int)->str:
    # Explorando las posibles soluciones se observa que el producto tiene más relevancia
    # al igual que los números más altos en las soluciones y por eso se exploran primero.
    # (el orden de exploración es inverso al de la lista por el uso de pop y append).
    OPERATIONS = ['/','+','-','*']
    NUMBERS = [i+1 for i in range(9)]
    inf_limit = -69
    sup_limit = 77

    def generate_solution():
        while(True):
            POS_SPLIT = 5
            numbers = np.array([i for i in range(9,0,-1)])
            np.random.shuffle(numbers)
            numbers = list(numbers[:POS_SPLIT])
            operations = np.array(OPERATIONS)
            np.random.shuffle(operations)
            node = Node(numbers,list(operations))
            if isinstance(node.eval_node(), int):
                return node

    node = generate_solution()
    print(node.expression)
    
simulated_annealing_expresion(4)