from Game_logika import Game

e = '0'
w = '1'
b = '2'
p = '3'
k = '4'
f = '5'


class lvl_1:
    def __init__(self):
        self.pole = [[w, w, w, w, w, w, w, w, w, w],
                     [w, e, e, e, e, e, b, e, k, w],
                     [w, e, p, e, e, e, b, e, k, w],
                     [w, e, e, e, w, b, e, e, e, w],
                     [w, e, e, e, w, k, e, e, e, w],
                     [w, e, b, k, w, w, w, w, w, w],
                     [w, w, w, w, w, w, w, w, w, w]]
        self.pole_size = [10, 7]
        self.pole_str = '1 1 1 1 1 1 1 1 1 1 1 0 0 0 0 0 2 0 4 1 1 0 3 0 0 0 2 0 4 1 1 ' \
                        '0 0 0 1 2 0 0 0 1 1 0 0 0 1 4 0 0 0 1 1 0 2 4 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 '



class lvl_2:
    def __init__(self):
        self.pole = [[w, w, w, w, w, w, w, w],
                     [w, e, e, e, e, e, w, w],
                     [w, p, e, e, e, e, w, w],
                     [w, e, b, w, e, e, e, k],
                     [w, e, b, w, e, e, w, w],
                     [w, e, e, w, e, w, w, w],
                     [w, w, k, w, w, w, w, w]]
        self.pole_size = [8, 7]
        self.pole_str = '1 1 1 1 1 1 1 1 1 0 0 0 0 0 1 1 1 3 0 0 0 0 1 1 1 0 2 1 0 0 0 4 1 0' \
                        ' 2 1 0 0 1 1 1 0 0 1 0 1 1 1 1 1 4 1 1 1 1 1 '



pole_str = ''


def transform_lvl(lvl):
    global pole_str
    for t in lvl.pole:
        for s in t:
           pole_str += s + ' '
    print(pole_str)


#transform_lvl(lvl_2())