

e = '0'
w = '1'
b = '2'
p = '3'
k = '4'
f = '5'

tg_change = {'0': '⬜',
             '1': '🟫',
             '2': '🟧',
             '3': '🟥',
             '4': '🟦',
             '5': '🟩'}


class Game:
    def __init__(self, pole_s, pole_size=None):
        if pole_size is None:
            self.pole_size = [10, 7]
        else:
            self.pole_size = pole_size
        self.player_pos_x = -1
        self.player_pos_y = -1
        self.pole_l = pole_s.split(' ')
        self.pole_l.pop(len(self.pole_l)-1)
        self.pole = []
        self.list_ = []
        self.lenght = 0
        for m in self.pole_l:
            self.lenght += 1
            self.list_.append(m)
            if self.lenght == self.pole_size[0]:
                self.lenght = 0
                self.pole.append(self.list_)
                self.list_ = []
        self.pole_return = ''

    def move(self, move):
        for u in self.pole:
            self.player_pos_y += 1
            for uu in u:
                if uu == p:
                    self.player_pos_x = u.index(p)
                    break
            if u[self.player_pos_x] == p:
                break
        cof_of_pos = 0
        while True:

            cof_of_pos += 1
            if self.pole[self.player_pos_y + move[1]*cof_of_pos][self.player_pos_x + move[0]*cof_of_pos] == w:
                break
            if self.pole[self.player_pos_y + move[1] * cof_of_pos][self.player_pos_x + move[0] * cof_of_pos] == f:
                break
            if self.pole[self.player_pos_y + move[1]*cof_of_pos][self.player_pos_x + move[0]*cof_of_pos] == k:
                if cof_of_pos == 1:
                    break
                else:
                    self.pole[self.player_pos_y + move[1] * cof_of_pos][
                         self.player_pos_x + move[0] * cof_of_pos] = f
                    self.pole[self.player_pos_y + move[1] * (cof_of_pos-1)][
                        self.player_pos_x + move[0] * (cof_of_pos-1)] = e
                    cof_of_pos = 0

            if self.pole[self.player_pos_y + move[1]*cof_of_pos][self.player_pos_x + move[0]*cof_of_pos] == b:
                pass
            if self.pole[self.player_pos_y + move[1]*cof_of_pos][self.player_pos_x + move[0]*cof_of_pos] == e:
                while cof_of_pos != 0:
                    if cof_of_pos != 1:
                        self.pole[self.player_pos_y + move[1] * cof_of_pos][
                            self.player_pos_x + move[0] * cof_of_pos] = b
                    else:
                        self.pole[self.player_pos_y][self.player_pos_x] = e
                        self.pole[self.player_pos_y + move[1] * cof_of_pos][self.player_pos_x + move[0] * cof_of_pos] = p
                    cof_of_pos -= 1
                break



        return self.change_format()

    def print_(self):
        for g in self.pole:
            print(g)

    def change_format(self):
        for t in self.pole:
            for s in t:
                self.pole_return += s + ' '
        return self.pole_return

    def print_tg(self):
        pole_result = ''
        y = 0
        for i in self.pole:
            y += 1
            for j in i:
                pole_result += tg_change[j]
            pole_result += '\n'
        return pole_result

    def lvl_complited(self):
        for i in self.pole:
            for j in i:
                if j == k:
                    return False
        return True