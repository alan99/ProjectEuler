dp = [1] * 201
coins = [2, 5, 10, 20, 50, 100, 200]

for c in coins:
	for i in range(c,201):
		dp[i] += dp[i-c]

print(dp)
