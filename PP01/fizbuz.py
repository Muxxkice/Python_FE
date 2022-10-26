import sys

max = int(sys.argv[1]) + 1
for i in range(1, int(max)):
	if i % 15 == 0:
		print('Fizzbuzz')
	elif i % 3 == 0:
		print('fizz')
	elif i % 5 == 0:
		print('buzz')
	else:
		print(i)
