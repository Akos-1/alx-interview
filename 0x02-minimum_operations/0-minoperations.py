#!/usr/bin/python3

"""
This script calculates the fewest number of operations needed to result
in exactly n H characters in a text file, given that the text editor
can only execute two operations: Copy All and Paste.

Prototype: def minOperations(n)
Returns an integer representing the fewest number of operations needed.
If n is impossible to achieve, returns 0.
"""


def minOperations(n):
    """
    Calculates the fewest number of operations needed to
    achieve n 'H' characters.

    Parameters:
        n (int): The desired number of 'H' characters in the file.

    Returns:
        int: The fewest number of operations needed.

    Raises:
        None
    """
    if n <= 1:
        return 0

    operations = n

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            operations = min(operations, i + minOperations(n // i))

    return operations


if __name__ == "__main__":
    # Example usage:
    n = 9
    print("Number of operations for", n, "characters:", minOperations(n))
