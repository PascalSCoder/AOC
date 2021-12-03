f = open("input", "r")
if (f == None):
	print("Failed to open input file")
	exit()

data = [0] * 12
total_input = 0
while (1):
	line = f.readline()
	if (line == None or line.__len__() == 0):
		break
	for i in range(12):
		if (line[i] == '1'):
			data[i] += 1
	total_input += 1

gamma = 0
epsilon = 0
for i in range(12):
	if (data[i] > total_input / 2):
		gamma += (1 << (11 - i))
	else:
		epsilon += (1 << (11 - i))

print("gamma: " + gamma.__str__())
print("epsilon: " + epsilon.__str__())
print("sum: " + (gamma * epsilon).__str__())