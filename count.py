

sum = 0

for counter in range(999,0,-1):
	if(counter % 3 == 0 or counter % 5 == 0):
		sum = sum + counter
print (sum)