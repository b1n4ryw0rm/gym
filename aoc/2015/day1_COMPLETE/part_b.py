with open('input.txt', 'r') as file:
    left_count = 0
    right_count = 0
    count = 0
    while True:
        character = file.read(1)
        if character == '(':
            left_count += 1
            count += 1
        elif character == ')':
            right_count += 1
            count += 1
        if left_count == right_count and character == ')':
            count += 1
            print(count)
            break
        if not character:
            break      
