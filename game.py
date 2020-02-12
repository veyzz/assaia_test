import player
import board


class Game:
    def __init__(self, size, trail=4):
        self.trail = trail
        self.players = (player.Player('x'), player.Player('o'))
        self.board = board.Board(size)
        self.active_player = 0

    #TODO: refactor check with function
    # def check_axis(self, coord, axis):
    #     x, y = coord
    #     start_x, start_y = [max(0, coord[i] - el * self.trail - 1) for i, el in enumerate(axis)]
    #     temp = (len(self.board), self.board.max_height)
    #     finish_x, finish_y = [min(temp[i], coord[i] + el * self.trail - 1) for i, el in enumerate(axis)]
    #     print(start_x, start_y, finish_x, finish_y)
    #     start_x = max(0, x - self.trail - 1)
    #     finish_x = min(len(self.board), x + self.trail - 1)
    #     start_y = max(0, y - self.trail - 1)
    #     finish_y = min(self.board.max_height, y + self.trail - 1)
    #     x_iter = start_x
    #     y_iter = start_y

    #     count = 1
    #     temp = ''
    #     while x_iter != finish_x and y_iter != finish_y:
    #         try:
    #             el = self.board.matrix[x_iter][y_iter]
    #         except IndexError:
    #             count = 1
    #             continue
    #         if temp == el:
    #             count += 1
    #             if count == self.trail: return True
    #         else:
    #             count = 1
    #         temp = el
    #         x_iter += axis[0]
    #         y_iter += axis[1]

    def end_game_condition_check(self, coord):
        x, y = coord
        start_x = max(0, x - self.trail - 1)
        finish_x = min(len(self.board), x + self.trail - 1)
        count = 1
        temp = ''
        for i in range(start_x, finish_x + 1):
            try:
                el = self.board.matrix[i][y]
            except IndexError:
                count = 1
                continue
            if temp == el:
                count += 1
                if count == self.trail: return True
            else:
                count = 1
            temp = el

        start_y = max(0, y - self.trail - 1)
        finish_y = min(self.board.max_height, y + self.trail - 1)
        count = 1
        temp = ''
        for i in range(start_y, finish_y + 1):
            try:
                el = self.board.matrix[x][i]
            except IndexError:
                count = 1
                continue
            if temp == el:
                count += 1
                if count == self.trail: return True
            else:
                count = 1
            temp = el

        #TODO: add check diagonally

        # start_x = max(0, x - self.trail - 1)
        # finish_x = min(len(self.board), x + self.trail - 1)
        # start_y = max(0, y - self.trail - 1)
        # finish_y = min(self.board.max_height, y + self.trail - 1)
        # count = 1
        # temp = ''
        # y_iter = start_y
        # for i in range(start_x, finish_x + 1):
        #     try:
        #         el = self.board.matrix[i][y_iter]
        #     except IndexError:
        #         count = 1
        #         continue
        #     if temp == el:
        #         count += 1
        #         if count == self.trail: return True
        #     else:
        #         count = 1
        #     temp = el
        #     y_iter += 1

        # start_x = max(0, x - self.trail - 1)
        # finish_x = min(len(self.board), x + self.trail - 1)
        # start_y = min(self.board.max_height, y + self.trail - 1)
        # finish_y = max(0, y - self.trail - 1)
        # print(coord)
        # print(start_x, start_y, finish_x, finish_y)
        # count = 1
        # temp = ''
        # y_iter = start_y
        # for i in range(start_x, finish_x + 1):
        #     try:
        #         el = self.board.matrix[i][y_iter]
        #     except IndexError:
        #         count = 1
        #         continue
        #     if temp == el:
        #         count += 1
        #         if count == self.trail: return True
        #     else:
        #         count = 1
        #     temp = el
        #     y_iter -= 1

    def game_loop(self):
        while True:
            print(self.board)
            print(f"Now player's {self.active_player + 1} turn")
            column = int(input())
            height = self.board.push(column,
                                     self.players[self.active_player].marker)
            if height is None:
                continue
            if self.end_game_condition_check((column, height)):
                print(f"Game over. Player {self.active_player + 1} wins")
                break
            self.active_player = (self.active_player + 1) % len(self.players)
