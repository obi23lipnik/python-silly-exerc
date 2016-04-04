import random

def cointoss():
	return random.randint(1,2)

def tossnum():
	i = 0
	j = 1
	b = 0
	while 1:
		i+=1
		a = cointoss()
		if b != a:
			b = a
			j+=1
			if j == 10:
				break
		else:
			j = 1
			
			
	return i
	
sum = 0
for a in xrange(1000):
	sum += tossnum()

print sum/1000