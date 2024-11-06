def knapsack(values, weights, capacity):
    n = len(values)
    # Create a 2D array to store the maximum value at each n and capacity
    dp = [[0 for x in range(capacity + 1)] for y in range(n + 1)]

    # Build the table dp[][] in bottom-up manner
    for i in range(1, n + 1):  # Loop through items
        for w in range(1, capacity + 1):  # Loop through capacities
            if weights[i - 1] <= w:
                # Max of including the item or excluding it
                dp[i][w] = max(values[i - 1] + dp[i - 1][w - weights[i - 1]], dp[i - 1][w])
            elif i == 0 or w == 0:
                dp[i][w] = 0
            else:
                # Item cannot be included
                dp[i][w] = dp[i - 1][w]

    # The maximum value that can be stored in the knapsack
    return dp[n][capacity]


# Example usage
if __name__ == "__main__":
    # Input: list of values and weights, and knapsack capacity
    values = [30, 40, 45, 77, 90]
    weights = [5, 10, 15, 22, 25]
    capacity = 60

    max_value = knapsack(values, weights, capacity)
    print(f"Maximum value in knapsack: {max_value}")
