import sys

def solve1(path):
	with open(path) as file:
		data = file.read().strip()
	floor = data.count('(') - data.count(')')
	print(floor)	

def solve2(path):
	with open(path) as file:
		data = file.read().strip()
	floor = 0
	for i, c in enumerate(data):
		if c == ')':
			floor -= 1
		elif c == '(':
			floor += 1

		if floor == -1:
			print(i + 1)
			break

if __name__ == "__main__":
	n = int(sys.argv[1])
	path = sys.argv[2]
	if n == 1:
		solve1(path)
	elif n == 2:
		solve2(path)