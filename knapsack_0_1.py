def knapsack_bottom_up(n: int, weights: list[int], values: list[int], capacity: int) -> tuple[int, list[int]]:
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(1, capacity + 1):
            if weights[i - 1] <= w:
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            else:
                dp[i][w] = dp[i - 1][w]

    selected_items = []
    i, w = n, capacity
    while i > 0 and w > 0:
        if dp[i][w] != dp[i - 1][w]:
            selected_items.append(i - 1)
            w -= weights[i - 1]
        i -= 1

    return dp[n][capacity], selected_items[::-1]


def main():
    # Example usage
    weights = [2, 3, 4, 5]
    values = [3, 4, 5, 6]
    capacity = 7
    print(knapsack_bottom_up(
        n=4,
        weights=weights,
        values=values,
        capacity=capacity
    ))


if __name__ == "__main__":
    main()
