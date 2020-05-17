def num_ways(n, dp):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    if dp[n] == -1:
        take_one_step = num_ways(n - 1, dp)
        take_2steps = num_ways(n - 2, dp)
        dp[n] = take_one_step + take_2steps
    return dp[n]
