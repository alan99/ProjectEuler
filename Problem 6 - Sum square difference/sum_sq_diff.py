A = list(range(1,101))
print(A[0],A[-1])
M = sum(map(lambda x: x**2, A))
N = (sum(A))**2

print(N-M)