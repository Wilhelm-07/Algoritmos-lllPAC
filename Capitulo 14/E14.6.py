class KnightTour:
    def __init__(self, n):
        self.n = n
        self.board = [[-1 for _ in range(n)] for _ in range(n)]

    def solve(self):
        # Comienza desde la posición (0, 0)
        self.board[0][0] = 0
        if not self._solveKTUtil(0, 0, 1):
            print("No solution exists")
        else:
            self._printSolution()

    def _solveKTUtil(self, curr_x, curr_y, move_count):
        # Todos los movimientos posibles para el caballo
        move_x = [2, 1, -1, -2, -2, -1, 1, 2]
        move_y = [1, 2, 2, 1, -1, -2, -2, -1]

        # Intentar cada movimiento desde la posición actual
        for i in range(8):
            new_x = curr_x + move_x[i]
            new_y = curr_y + move_y[i]

            # Comprueba si la posición es válida
            if self._isSafe(new_x, new_y):
                self.board[new_x][new_y] = move_count
                if self._solveKTUtil(new_x, new_y, move_count + 1):
                    return True
                else:
                    # Si no es posible continuar, vuelve a borrar el movimiento
                    self.board[new_x][new_y] = -1

        return False

    def _isSafe(self, x, y):
        return 0 <= x < self.n and 0 <= y < self.n and self.board[x][y] == -1

    def _printSolution(self):
        for row in self.board:
            print(' '.join(f"{elem:02}" for elem in row))

# Tamaño del tablero, KxK
k = 5
kt = KnightTour(k)
kt.solve()
