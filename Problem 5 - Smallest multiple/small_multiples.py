import math

k = 20
N = 1
i = 0
check = True
limit = k**.5

p = [2,3,5,7,11,13,17,19]
a = []

for n in p:
	a.append(1)
	if check:
		if n <= limit:
			a[-1] = int(math.log(k) / math.log(n))
		else:
			check = False

	N = N * n ** a[-1]
	print(a)


print(N)