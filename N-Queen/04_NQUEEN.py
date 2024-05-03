
class Game:
    def __init__(self, n):
        self.n = n
        self.board = b = [[0 for _ in range(n)] for _ in range(n)]

    def is_safe(self, row, col):
        # diagonal check 1
        i, j = row, col
        while i >= 0 and j >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j -= 1

        # diagonal check 2
        i, j = row, col
        while i >= 0 and j < self.n:
            if self.board[i][j] == 1:
                return False
            i -= 1
            j += 1

        # check up
        i, j = row, col
        while i >= 0:
            if self.board[i][j] == 1:
                return False
            i -= 1

        # If not reached False
        return True

    def solution(self, row):
        if row >= self.n:
            self.queen_table()
            return

        for i in range(self.n):
            if self.is_safe(row, i):
                self.board[row][i] = 1
                self.solution(row + 1)
                self.board[row][i] = 0

    def queen_table(self):
        print("Solution:")
        for i in range(self.n):
            for j in range(self.n):
                if self.board[i][j] == 1:
                    print('Q', end="")
                if self.board[i][j] == 0:
                    print('.', end="")
            print("")


n = 4
g = Game(n)
g.solution(0)

