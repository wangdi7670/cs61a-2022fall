for i in range(3):
    print(i)

from math import sqrt

def is_prime(n):
    if n == 2:
        return True
    elif n % 2 == 0:
        return False
    i = 3
    while i <= sqrt(n):
        if n % i == 0:
            return False
        i += 2
    return True


def pigs_on_prime(player_score, opponent_score):
    """Return the points scored by the current player due to Pigs on Prime.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.
    """
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    if not is_prime(player_score):
        return 0
    else:
        i = player_score + 1
        while not is_prime(i):
            i += 1
        return i - player_score
    # END PROBLEM 4


ans = pigs_on_prime(19, 0)
print(ans)