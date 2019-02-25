primes = [2]
i = 3

while len(primes) < 10001:
	for p in primes:
		if i % p == 0:
			break
	else:
		primes.append(i)

	i += 1

print(primes[-1])