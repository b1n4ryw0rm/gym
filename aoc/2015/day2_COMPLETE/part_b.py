import math
total = 0
with open('input.txt', 'r') as file:
    for line in file:
        values = list(map(int, line.split('x')))
        bow = math.prod(values)
        min_a = min(values)
        values.remove(min_a)
        min_b = min(values)

        wrap = 2 * min_a + 2 * min_b
        total += bow + wrap
        
print(total)