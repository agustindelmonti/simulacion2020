import numpy as np
import random as rn


def martingale(start_money, start_amount, winp, num_bets, table_limit=float('inf')):
    bet_size = min(start_amount, start_amount, table_limit)
    money = start_money
    output = np.zeros(num_bets + 1)

    output[0] = start_money
    for i in range(1, num_bets + 1):
        if money <= 0:
            pass
        elif rn.random() < winp:
            money += bet_size
            bet_size = start_amount
        else:
            money -= bet_size
            bet_size = min(2 * bet_size, table_limit)
            if bet_size > money:
                bet_size = money

        output[i] = money

    return output


def paroli(start_money, start_amount, winp, num_bets, table_limit=float('inf')):
    bet_size = min(start_amount, start_money, table_limit)
    money = start_money
    output = np.zeros(num_bets + 1)

    output[0] = start_money
    for i in range(1, num_bets + 1):
        if money <= 0:
            return output
        elif rn.random() < winp:
            money += bet_size
            bet_size = min(2 * bet_size, table_limit)
            if i % 3 == 0:
                bet_size = start_amount
        else:
            money -= bet_size
            bet_size = start_amount

        output[i] = money

    return output
