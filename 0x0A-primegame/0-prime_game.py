#!/usr/bin/python3


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True


def simulate_game(n):
    primes = [i for i in range(2, n + 1) if is_prime(i)]
    remaining = set(range(1, n + 1))
    maria_turn = True

    while True:
        if maria_turn:
            possible_moves = [p for p in primes if p in remaining]
            if not possible_moves:
                return "Ben"
            for p in possible_moves:
                for i in range(p, n + 1, p):
                    remaining.discard(i)
            maria_turn = False
        else:
            possible_moves = [p for p in range(2, n + 1) if p in remaining and is_prime(p)]
            if not possible_moves:
                return "Maria"
            for p in possible_moves:
                for i in range(p, n + 1, p):
                    remaining.discard(i)
            maria_turn = True


def isWinner(x, nums):
    maria_wins = 0
    ben_wins = 0

    for n in nums:
        winner = simulate_game(n)
        if winner == "Maria":
            maria_wins += 1
        elif winner == "Ben":
            ben_wins += 1

    if maria_wins > ben_wins:
        return "Maria"
    elif maria_wins < ben_wins:
        return "Ben"
    else:
        return None


if __name__ == "__main__":
    x = 3
    nums = [4, 5, 1]
    print(isWinner(x, nums))  # Output: Ben
