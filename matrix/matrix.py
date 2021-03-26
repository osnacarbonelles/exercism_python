class Matrix:
    def __init__(self, matrix_string):
        self.mat = [[int(i) for i in row.split()]
                    for row in matrix_string.splitlines()]

    def row(self, index):
        return self.mat[index - 1]

    def column(self, index):
        return [row[index - 1] for row in self.mat]
