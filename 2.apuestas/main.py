from roulette import *

if __name__ == "__main__":
    '''
    strategy
    initial bank roll
    target winning
    trials
    table limit
    '''

game = AmRoulette()
for i in range(1000):
    game.spin()
    print(game.ball)
