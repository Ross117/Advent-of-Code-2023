with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

total = 0

for line in input:

    for char in line:
        if char.isdigit():
            first_num = char
            break

    for char in line[::-1]:
        if char.isdigit():
            second_num = char
            break

    value = first_num + second_num

    total += int(value)

print(total)