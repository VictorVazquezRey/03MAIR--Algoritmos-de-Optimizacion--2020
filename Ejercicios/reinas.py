def queens (n:int) -> list:
    board = []
    def canBeSet(row:int, board: list, elem:int) -> bool:
        if row == 0:
            return True

        for i in range(row):
            if board[i] == elem:
                return False
            elif abs(board[i] - elem) == abs(i - row):
                return False

        return True

    def recursive_queen(row:int, board:list, n:int) -> bool:
        if row < n:            
            for j in range(n):
                if canBeSet(row,board,j):
                    board.append(j)
                    if recursive_queen(row+1, board, n):
                        return True
                    board.pop()
            return False
        return True
    
    if recursive_queen(0, board, n):
        return board
    else:
        return []

print(queens(4))
