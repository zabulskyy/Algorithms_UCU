class AdjacencyMatrix:
    def __init__(self, size):
        self.table = [[None for _ in range(size)] for _ in range(size)]
