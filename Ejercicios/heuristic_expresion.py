from node import Node
from itertools import permutations

def solve_backtracking_expresion(value:int)->str:
    # Explorando las posibles soluciones se observa que el producto tiene más relevancia
    # al igual que los números más altos en las soluciones y por eso se exploran primero.
    # (el orden de exploración es inverso al de la lista por el uso de pop y append).
    OPERATIONS = ['-','/','*','+']
    NUMBERS = [i for i in range(9,0,-1)]
    inf_limit = -69
    sup_limit = 77

    def solve(value:int, node:Node):
        def solve_for_number(value:int, node:Node):
            for n in set(NUMBERS)-set(node.numbers):
                node.add_number(n)
                if solve(value, node):
                    return True
                node.substact_number()
            return False

        if len(node.operations) == 4:
            if node.eval_node()==value:
                return True
            else:
                return False
        elif not node.numbers:
            return solve_for_number(value,node)
        else:
            for o in set(OPERATIONS)-set(node.operations):
                node.add_operation(o)
                if solve_for_number(value, node):
                    return True
                node.substact_operation()
        return False

    if value < inf_limit or value > sup_limit:
        raise ValueError('Valor imposible de calcular')

    node = Node()
    if solve(value, node):
        return node.expression
    else:
        return ""
    
print(solve_backtracking_expresion(-60))

