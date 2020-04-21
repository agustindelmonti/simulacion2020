import random

class FairRoulette:
    def __init__(self):
        self.pockets = []
        self.gen_board()
        self.ball = None

        self.history = []
        self.pocketOdds = len(self.pockets) - 1

    def spin(self):
        self.ball = random.choice(self.pockets)

    def gen_board(self):
        """ Generate the roulette wheel pockets
        RED    1 3 5 7 9 12 14 16 18 19 21 23 25 27 30 32 34 36
        BLACK 2 4 6 8 10 11 13 15 17 20 22 24 26 28 29 31 33 35
        """
        colors = ['b', 'r']
        b = [10, 8]
        k, m = 0, 0
        for i in range(1, 37):
            if k == b[m]:
                k = 0
                m = (m + 1) % 2
            c = colors[(i + m) % 2]
            k += 1
            self.pockets.append([i, c])


class EuRoulette(FairRoulette):
    def __init__(self):
        FairRoulette.__init__(self)
        self.pockets.append(['0', 'g'])


class AmRoulette(EuRoulette):
    def __init__(self):
        EuRoulette.__init__(self)
        self.pockets.append(['00', 'g'])
