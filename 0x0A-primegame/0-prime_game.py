#!/usr/bin/python3
""" prime game module """


def isWinner(x, nums):
    """
    Determine the winner after x rounds of the game.
    Maria and Ben take turns picking numbers from 1 to n,
    and the player with the most primes wins the round.

    x: number of rounds
    nums: array of n values
    Return: name of the player that won the most rounds
    If the winner cannot be determined, return None
    """
    if not nums or x < 1:
        return None

    # Compute primes using sieve up to the maximum number in nums
    n = max(nums)
    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for i in range(2, int(n ** 0.5) + 1):
        if sieve[i]:
            for j in range(i * i, n + 1, i):
                sieve[j] = False

    # Calculate the number of primes up to each number in nums
    prime_count = [0] * (n + 1)
    for i in range(1, n + 1):
        prime_count[i] = prime_count[i - 1] + int(sieve[i])

    # Track the scores of Maria and Ben
    maria_score = 0
    ben_score = 0

    # Determine the winner of each round
    for num in nums:
        if prime_count[num] % 2 == 0:
            ben_score += 1
        else:
            maria_score += 1

    if maria_score > ben_score:
        return "Maria"
    elif ben_score > maria_score:
        return "Ben"
    else:
        return None
