f = open("infile")
if (f == None):
	print("Failed to open infile")
	exit


aim = 0
forward = 0
depth = 0
data = []
while (1):
	line = f.readline()
	if (line == None or line.__len__() == 0):
		break
	tmp = line.split(" ")
	if (tmp[0] == "forward"):
		forward += int(tmp[1])
		depth += aim * int(tmp[1])
	elif (tmp[0] == "down"):
		aim += int(tmp[1])
	elif (tmp[0] == "up"):
		aim -= int(tmp[1])
	else:
		print("Unsupported action encountered: " + line)

print(forward.__str__() + " : " + depth.__str__())
print(forward * depth)