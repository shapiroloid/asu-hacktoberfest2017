def bubble(numbers):
	n = len(numbers)
	continuar = 1
	for j in range(0,n):
		continuar = 0
		for i in range(1,n):
			if (numbers[i-1] > numbers[i]):
				temp = numbers[i-1]
				numbers[i-1] = numbers[i]
				numbers[i] = temp
				continuar = 1
		#for the loop if you have already ordered
		if (continuar == 0):
			break

	return numbers;
