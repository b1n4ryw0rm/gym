with open('input.txt', 'r') as file:
    left_count = 0
    right_count = 0
    while True:
        character = file.read(1)
        if character == '(':
            left_count += 1
        elif character == ')':
            right_count += 1
        if not character:
            break

floor = 0
if left_count > right_count:
    floor = left_count - right_count
elif right_count > left_count:
    floor = right_count - left_count

print(floor)
