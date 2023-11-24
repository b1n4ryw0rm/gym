import sys


def solve1(path: str) -> None:
	with open(path) as f:
		data = [line.strip() for line in f.readlines()]

	total = 0
	for line in data:
		a, b, c = map(int, line.split('x'))
		surface = 2 * (a*b + a*c + b*c)
		slack = min(a*b, a*c, b*c)
		paper = surface + slack
		total += paper
	print(total)

def solve2(path: str) -> None:
	with open(path) as f:
		data = [line.strip() for line in f.readlines()]

	total = 0
	for line in data:
		a, b, c = map(int, line.split('x'))
		volume = a*b*c
		rest = 2 * min(a+b, b+c, c+a)
		total += volume + rest
	print(total)

if __name__ == "__main__":
	n = int(sys.argv[1])
	path = sys.argv[2]

	if n == 1:
		solve1(path)
	if n == 2:
		solve2(path)