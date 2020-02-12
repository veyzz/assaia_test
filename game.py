import board
import player


class Game:
    def __init__(self, size, trail=4):
        self.trail = trail
        self.players = (player.Player('x'), player.Player('o'))
        self.board = board.Board(size)
        self.active_player = 0

    def check_axis(self, coord, axis):
        x, y = coord
        count = 1
        temp = ''
        step = 0
        while step < self.trail:
            step += 1
            try:
                if x < 0 or y < 0:
                    raise IndexError
                el = self.board.matrix[x][y]
            except IndexError:
                count = 1
                return False
            if temp == el:
                count += 1
                if count == self.trail: return True
            else:
                count = 1
            temp = el
            x += axis[0]
            y += axis[1]
        return False

    def check_from_cell(self, coord):
        return any(
            (self.check_axis(coord, (1, 0)), self.check_axis(coord, (1, 1)),
             self.check_axis(coord, (0, 1)), self.check_axis(coord, (-1, 1)),
             self.check_axis(coord, (-1, 0)), self.check_axis(coord, (-1, -1)),
             self.check_axis(coord, (0, -1)), self.check_axis(coord, (1, -1))))

    def win_condition_check(self):
        for i in range(len(self.board)):
            for j in range(len(self.board.matrix[i])):
                if self.check_from_cell((i, j)):
                    return True
        return False

    def draw_condition_check(self):
        if self.board.filled == len(self.board):
            return True

    def game_loop(self):
        while True:
            print(self.board)
            print(f"Now player's {self.active_player + 1} turn")
            try:
                column = int(input())
            except ValueError:
                continue
            height = self.board.push(column,
                                     self.players[self.active_player].marker)
            if height is None:
                continue
            if self.win_condition_check():
                print(self.board)
                print(f"Game over. Player {self.active_player + 1} wins.")
                break
            if self.draw_condition_check():
                print(self.board)
                print("Game over. Draw.")
                break
            self.active_player = (self.active_player + 1) % len(self.players)
