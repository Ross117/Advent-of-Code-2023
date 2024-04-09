with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

lookup = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
}

total = 0

for line in input:

    found_first_num = False
    found_second_num = False

    for ind_1, char in enumerate(line):

        if found_first_num:
            break

        if char.isdigit():
            first_num = char
            found_first_num = True

        for key in lookup.keys():  
            if key in line[0: ind_1 + 1]:
                first_num = lookup[key]
                found_first_num = True
                break

    reversed_line = line[::-1]

    for ind_2, char in enumerate(reversed_line):

        if found_second_num:
            break

        if char.isdigit():
            second_num = char
            found_second_num = True

        for key in lookup.keys():  
            if key[::-1] in reversed_line[0: ind_2 + 1]:
                second_num = lookup[key]
                found_second_num = True
                break

    value = first_num + second_num

    total += int(value)

print(total)
