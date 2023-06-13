

memo = {
    0: 0,
    1: 1
}


def fibonacci(n: int) -> int:
    # Searching for a precalculated value in the memoization table
    if memo.get(n) is not None:
        return memo[n]
    # Couldn't find the corresponding value
    else:
        # Calculating fibonacci(n) and storing the value in the memoization table before returning
        memo[n] = fibonacci(n-1) + \
        fibonacci(n-2)
        return memo[n]


def main():
    # Testing with user input
    n = int(input())
    print(fibonacci(n))


if __name__ == "__main__":
    main()
