def get_most_common(data, index):
	set_bits = 0
	for i in range(data.__len__()):
		line = data[i]
		if (line[index] == '1'):
			set_bits += 1
	if (set_bits >= data.__len__() / 2):
		return 1
	else:
		return 0

def get_least_common(data, index):
	set_bits = 0
	for i in range(data.__len__()):
		line = data[i]
		if (line[index] == '1'):
			set_bits += 1
	if (set_bits < data.__len__() / 2):
		return 1
	else:
		return 0

def print_numbers(data):
	for i in data:
		print(i)

def binary_to_number(bin):
	num = 0
	for i in range(12):
		if (bin[i] == '1'):
			num += (1 << (11 - i))
	return num


f = open("input", "r")
if (f == None):
	print("Failed to open input file")
	exit()

data = []
while (1):
	line = f.readline()
	if (line == None or line.__len__() == 0):
		break
	line = line.rstrip("\n")
	data.append(line)

filtered = data.copy()
index = 0
while (filtered.__len__() > 1):
	most_common_bit = get_most_common(filtered, index)
	i = 0
	while (i < filtered.__len__()):
		if (str(filtered[i][index]) != str(most_common_bit)):
			filtered.remove(filtered[i])
		else:
			i += 1
	index += 1

oxygen = binary_to_number(filtered[0])

filtered = data.copy()
index = 0
while (filtered.__len__() > 1):
	least_common_bit = get_least_common(filtered, index)
	i = 0
	while (i < filtered.__len__()):
		if (str(filtered[i][index]) != str(least_common_bit)):
			filtered.remove(filtered[i])
		else:
			i += 1
	index += 1

scrubber = binary_to_number(filtered[0])

print("Results:")
print(oxygen)
print(scrubber)
print(oxygen * scrubber)