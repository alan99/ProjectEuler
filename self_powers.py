result = 0
module = 1e10

for i in range(1,1001):
	x = i
	for j in range(1,i):
		x *= i
		x %= module

	result += x
	result %= module

print(result)