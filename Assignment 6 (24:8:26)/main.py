def knapsack_top_down(weights, values, capacity):
    memo = {}

    def solve(i, remaining):
        if i == 0 or remaining == 0:
            return 0

        if (i, remaining) in memo:
            return memo[(i, remaining)]

        if weights[i - 1] > remaining:
            result = solve(i - 1, remaining)
        else:
            include = values[i - 1] + solve(
                i - 1, remaining - weights[i - 1]
            )
            exclude = solve(i - 1, remaining)
            result = max(include, exclude)

        memo[(i, remaining)] = result
        return result

    return solve(len(weights), capacity)


def knapsack_bottom_up(weights, values, capacity):
    n = len(weights)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] > w:
                dp[i][w] = dp[i - 1][w]
            else:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                dp[i][w] = max(include, exclude)

    return dp[n][capacity]


weights = [2, 3, 4, 5]
values = [3, 4, 5, 6]
capacity = 5

print("Top-Down:", knapsack_top_down(weights, values, capacity))
print("Bottom-Up:", knapsack_bottom_up(weights, values, capacity))