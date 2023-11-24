"""
python3 solve.py 1/2 input.txt
"""
import sys

def solve1(path: str) -> None:
    with open(path) as file:
        data = file.read().strip()
    visited = set()
    visited.add((0,0))
    pos = (0,0)
    for c in data:
        if c == '^':
            pos = (pos[0], pos[1] + 1)
        elif c == 'v':
            pos = (pos[0], pos[1] - 1)
        elif c == '>':
            pos = (pos[0] + 1, pos[1])
        elif c == '<':
            pos = (pos[0] - 1, pos[1])
        visited.add(pos)
    print(len(visited))

def update(pos, c):
    if c == '^':
        return (pos[0], pos[1] + 1)
    elif c == 'v':
        return (pos[0], pos[1] - 1)
    elif c == '>':
        return (pos[0] + 1, pos[1])
    elif c == '<':
        return (pos[0] - 1, pos[1])

def solve2(path: str) -> None:
    with open(path) as file:
        data = file.read().strip()
    visited = set()
    visited.add((0,0))
    santa = (0,0)
    robo = (0,0)
    for i, c in enumerate(data):
        if i%2 == 0:
            robo = update(robo, c)
            visited.add(robo)
        else:
            santa = update(santa, c)
            visited.add(santa)
    print(len(visiteD))

if __name__ == "__main__":
    n = int(sys.argv[1])
    path = sys.argv[2]
    if n == 1:
        solve1(path)
    elif n == 2:
        solve2(path)
