n, r = 102, 102
dp = [[1]]
# dp[n][r] = C(n,r)
# C(n,r) = C(n-1,r-1) + C(n-1,r)
count = 0

for i in range(1,n):
	row = [1]
	for j in range(1,i-1):
		k = dp[-1][j-1] + dp[-1][j]
		row += [k]
	
		if k > 1e6:
			count += 1

	row += [1]
	dp += [row]
	#print(row)
	

print(count)

