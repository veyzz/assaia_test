class Board:
    def __init__(self, size):
        self.max_height = size[1]
        self.matrix = [[] for _ in range(size[0])]
        self.filled = 0

    def push(self, n, el):
        '''Returns y coordinate of added element
        or None if not succesfull

        '''
        if n not in range(len(self.matrix)):
            return None
        if len(self.matrix[n]) < self.max_height:
            self.matrix[n].append(el)
            if len(self.matrix[n]) == self.max_height:
                self.filled += 1
            return len(self.matrix[n]) - 1
        return None

    def __len__(self):
        return len(self.matrix)

    def __str__(self):
        s = ''
        for i in reversed(range(self.max_height)):
            for j in range(len(self.matrix)):
                try:
                    s += self.matrix[j][i]
                except IndexError:
                    s += '.'
            s += '\n'
        s += ''.join(str(i) for i in range(len(self.matrix)))
        return s
