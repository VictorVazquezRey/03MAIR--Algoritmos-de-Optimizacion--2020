import numpy as np
from math import inf 

def cruiser(T:'nparray', origin_pier: int, target_pier: int) -> list:
    C = [[0,[target_pier]]]
    for i in range(target_pier - 1, origin_pier - 1, -1):
        pier = i
        cost = T[pier][target_pier]
        for j in range (i+1, target_pier):
            actual_cost = T[i][j] + C[i-j][0]
            if actual_cost < cost:
                cost = actual_cost
                pier = j

        to_insert = [cost,[i] + C[i-pier][1]]
        C.append(to_insert)
        # print(C)
    return C.pop()
    



T = np.array(
            [
                [0  , 5  , 4  , 3  , inf, inf, inf],
                [inf, 0  , inf, 2  , 3  , inf, 11],
                [inf, inf, 0  , 1  , inf, 4  , 10],
                [inf, inf, inf, 0  , 5  , 6  , 9],
                [inf, inf, inf, inf, 0  , inf, 4 ],
                [inf, inf, inf, inf, inf, 0  , 3],
                [inf, inf, inf, inf, inf, inf, 0, ]
            ])

print(cruiser(T, 0, 6))