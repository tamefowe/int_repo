import numpy as np
from fractions import Fraction


def test():
    num_of_games = 3
    num_of_outcomes = 3+2*(num_of_games-1)
    cutoff = num_of_outcomes / 2
    print(f"num_of_games: {num_of_games}\nnum_of_outcomes: {num_of_outcomes}\ncutoff: {cutoff}")

    payoffs = np.zeros(num_of_outcomes)

    for i in range(0, num_of_outcomes):
        payoffs[i] = 1 if i < cutoff else 0

    print(f"payoffs: {payoffs}")


def trinomial_backward_induction(prob_of_win, prob_of_loss, prob_of_draw, num_of_games):
    # initialize payoffs
    num_of_outcomes = 3+2*(num_of_games-1)
    cutoff = num_of_outcomes / 2
    payoffs = np.zeros(num_of_outcomes)

    for i in range(0, num_of_outcomes):
        payoffs[i] = 1 if i < cutoff else 0

    # backward  recursion through tree
    for i in np.arange(num_of_games-1, -1, -1):
        for j in range(0, 2*i+1):
            payoffs[j] = (prob_of_win*payoffs[j+1] + prob_of_draw*payoffs[j] + prob_of_loss*payoffs[j-1])

    return payoffs[0]


def main():
    prob_of_win, prob_of_loss, prob_of_draw, num_of_games = 0.2, 0.2, 0.6, 24
    payoff = trinomial_backward_induction(prob_of_win, prob_of_loss, prob_of_draw, num_of_games)
    print(payoff)


if __name__ == '__main__':
    main()
    #test()
