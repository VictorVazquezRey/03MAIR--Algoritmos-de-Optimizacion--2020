from node import Node
from itertools import permutations

def solve_expresion(value:int)->str:
    OPERATIONS = ['*', '+', '/', '-']
    for n in permutations([i+1 for i in range(9)], len(OPERATIONS) + 1):
        for e in permutations(OPERATIONS):
            node = Node(n,e)
            if node.eval_node()==value:
                return node.expression
        

# inf_limit = -69
# sup_limit = 77
#
# not_reachable = []
# for v in range(inf_limit,sup_limit+1):
#     if not solve_expresion(v):
#         not_reachable.append(v)
# print(not_reachable)


# inf_limit = 0
# sup_limit = 77
# 
# solutions = []
# for v in range(inf_limit,sup_limit+1):
#     solution = solve_expresion(v)
#     solutions.append("{}={}".format(v, solution))
# print(solutions)

print(solve_expresion(4))