import matplotlib.pyplot as plt

from strategies import *


def gamble(strategy, money, num_bets, simulations, winp, start_amount=1, plotting=False, table_limit=float('inf')):
    if plotting:
        plt.figure(figsize=(12, 6))

    loss = 0
    last_balances = np.zeros(simulations)

    for num in range(simulations):
        result = strategy(money, start_amount, winp, num_bets, table_limit)

        if min(result) <= 0:
            loss += 1
            if plotting:
                plt.plot(result, 'r', alpha=.20)
        else:
            if plotting:
                plt.plot(result, 'b', alpha=.20)

        # Calculate expected return of investment (ROI)
        last_balances[num] = result[-1] - money

    print(f"\nRan {simulations} simulations ")
    print(f"After {num_bets} bets, {100.0 * loss / simulations}% of bettors lost all their money")
    print(f"Average money won or lost ${last_balances.mean()}")
    print(f"Closing balance ${last_balances.sum()}")
    if plotting:
        plt.title('Martingale', fontsize=15)
        plt.xlabel('Number of Bets', fontsize=15)
        plt.ylabel('Money', fontsize=15)
        plt.xlim(0, num_bets)
        plt.ylim(0, )
        #plt.savefig('outcome.pdf', bbox_inches='tight')
        plt.show()


if __name__ == "__main__":

    gamble(martingale, 50000, 2000, 2000, 18.0/37.0, start_amount=100)
    gamble(martingale, 50000, 2000, 2000, 18.0/37.0, start_amount=100, table_limit=2048)
    gamble(martingale, 50000, 2000, 2000, 18.0/37.0, start_amount=100, table_limit=1024)

    gamble(martingale, 50000, 20, 2000, 18.0/37.0, start_amount=100, table_limit=2048)
    gamble(martingale, 50000, 200, 2000, 18.0/37.0, start_amount=100, table_limit=2048)
    gamble(martingale, 50000, 2000, 2000, 18.0/37.0, start_amount=100, table_limit=2048)

    gamble(martingale, 50000, 20, 2000, 18.0 / 37.0, start_amount=100, table_limit=2048)
    gamble(martingale, 50000, 20, 2000, 18.0 / 37.0, start_amount=500, table_limit=2048)
    gamble(martingale, 50000, 20, 2000, 18.0 / 37.0, start_amount=1000, table_limit=2048)

    gamble(paroli, 5000, 200, 2000, 18.0 / 37.0, start_amount=10, table_limit=2048)
    gamble(paroli, 5000, 200, 2000, 18.0 / 37.0, start_amount=100, table_limit=2048)
    gamble(paroli, 5000, 200, 2000, 18.0 / 37.0, start_amount=1000, table_limit=1024)
