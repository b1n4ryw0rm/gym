with open('input.txt', 'r') as file:
    total = 0
    for line in file:
        a, b, c = map(int, line.split('x'))
        x = a * b
        y = b * c
        z = a * c
        k = x if x < y and x < z else (y if y < z else z) 
        sum = 2 * x + 2 * y + 2 * z + k
        total += sum
print(total)
