a, b, res = 1, 1, 0

while a < 4e6:
	if a % 2 == 0:
		res += a
	a, b = b, a+b

print(res)
