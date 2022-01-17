input_number = input("Введите число: ")

number_length = len(input_number)
max_element = 0
i = 0
while i < number_length:
	current_element = int(input_number[i])
	if current_element > max_element:
		max_element = current_element
	i += 1
print(max_element)

input("")