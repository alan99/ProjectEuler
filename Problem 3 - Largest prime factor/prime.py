n = 600851475143
# sn = int(n**.5)

# Initialize the maximum prime factor 
# variable with the lowest one 
maxPrime = -1
  
# Print the number of 2s that divide n 
while n % 2 == 0: 
    maxPrime = 2
    n >>= 1     # equivalent to n /= 2 
      
# n must be odd at this point,  
# thus skip the even numbers and  
# iterate only for odd integers 
for i in range(3, int(n**.5) + 1, 2): 
    while n % i == 0: 
        maxPrime = i 
        n = n / i 
  
# This condition is to handle the  
# case when n is a prime number  
# greater than 2 
if n > 2: 
    maxPrime = n 

print(maxPrime) 

# res = [2]
# for i in range(3,sn+1):
# 	for c in res:
# 		if i % c == 0:
# 			break
# 	else:
# 		res.append(i)
# 		print(i)

# while res:
# 	r = res.pop()
# 	if n % r == 0:
# 		print(r)
# 		break
