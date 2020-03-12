import numpy as np
from collections import defaultdict


class ConnectGame:
    def __init__(self, board):
        self.np = np.array([list(x.replace(' ', '')) for x in board.split('\n')])
        self.moves = self.neighbours()

    def get_winner(self):
        for x in range(len(self.np)):
            if self.np[x, 0] == 'X' and self.attempt((x, 0)):
                return 'X'
        for y in range(len(self.np[0])):
            if self.np[0, y] == 'O' and self.attempt((0, y), False):
                return 'O'
        return ''

    def attempt(self, start, x=True):
        stack = [start]
        while stack:
            cur = stack.pop()
            if cur[1 if x else 0] == (len(self.np[0]) - 1 if x else len(self.np) - 1):
                return True
            while self.moves[cur]:
                hold = self.moves[cur].pop()
                if self.np[hold[0], hold[1]] == ('X' if x else 'O'):
                    stack.append(hold)
        return False

    def neighbours(self):
        lats = ((1, -1), (-1, 1), (0, 1), (0, -1), (1, 0), (-1, 0))
        d = defaultdict(list)
        for yi, st in enumerate(self.np):
            for xi, char in enumerate(st):
                for a, b in lats:
                    x, y = xi + a, yi + b
                    if min(x, y) < 0 or x > len(st) - 1 or y > len(self.np) - 1:
                        continue
                    d[(yi, xi)].append((y, x))
        return d