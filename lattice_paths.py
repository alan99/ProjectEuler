size = 20
path = [1] * (size+1)

for _ in range(1, size+1):
	for i in range(1, size+1):
		path[i] += path[i-1]
	print(path)
	
