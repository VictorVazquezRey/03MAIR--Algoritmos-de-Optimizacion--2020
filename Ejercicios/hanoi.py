def hanoi(n:int,origin:list, helper:list, target:list, game: list):
    if n > 0:
        hanoi(n-1, origin, target, helper, game)
        target.append(origin.pop())
        print(game)
        hanoi(n-1, helper, origin, target, game)

# These are like stacks. More to the rigth more up
origin = [5, 4, 3, 2, 1]
helper = []
target = []

# This is used to print, because origin, helper and target are changed
# across calls. 
game = [origin, helper, target]

hanoi(5, origin, helper, target, game)