import random

NUM_SAMPLES = 10000000

i = 0
count = 0
total = 0

while i < NUM_SAMPLES:
	i = i + 1
	
	#see if we choose cup A or not
	A = (random.random() < 0.9)

	#prob we choose a quarter	
	Q = 0
	if A == True:
		Q = (random.random() < 0.666666666666)
	if A == False:
		Q = (random.random() < 0.333333333333)


	# if we get the conditions we care about, count it
	if A == True and Q == False:
		count = count + 1

	# if our observed variable was false, count it as a sample, otherwise throw away
	if Q == False:
		total = total + 1

print count
print total
print (float(count) / float(total))