#!/usr/bin/python3
"""a pile of coins of different values"""


def makeChange(coins, total):
    if total <= 0:
        return 0

    # Create a list to store the fewest number of coins needed for each total
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    # Iterate over each coin value
    for coin in coins:
        # Update the fewest number of coins needed for each total
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    if dp[total] == float('inf'):
        return -1
    else:
        return dp[total]
