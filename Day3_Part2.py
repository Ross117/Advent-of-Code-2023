with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

gear_ratios = []
gear_inds_added = []
part_number_inds_found = []

matrix = [list(line) for line in input]

def build_number(row_ind, col_ind):

    number = matrix[row_ind][col_ind]
    inds_used = [row_ind, col_ind]

    decrement = 1
    for _i in range(1000):
        try:
            val = matrix[row_ind][col_ind - decrement]
            if val.isdigit():
                number = val + number
                inds_used.extend([row_ind, col_ind - decrement])
                decrement += 1

            else:
                break
        except IndexError:
            break

    increment = 1
    for _j in range(1000):
        try:
            val = matrix[row_ind][col_ind + increment]
            if val.isdigit():
                number = number + val
                inds_used.extend([row_ind, col_ind + increment])
                increment += 1
            else:
                break
        except IndexError:
            break

    inds_used.sort()
    inds_used = str(inds_used)

    if inds_used not in part_number_inds_found:
        part_number_inds_found.append(inds_used)
        return number

    return False

def adjacency_check(row_ind, col_ind):

    inds_to_check = [
        [row_ind - 1, col_ind],
        [row_ind + 1, col_ind],
        [row_ind, col_ind - 1],
        [row_ind, col_ind + 1],
        [row_ind - 1, col_ind - 1],
        [row_ind + 1, col_ind + 1],
        [row_ind - 1, col_ind + 1],
        [row_ind + 1, col_ind - 1],
    ]

    part_numbers_found = 0
    part_numbers = []


    for inds in inds_to_check:
        if part_numbers_found > 2:
            break
        if matrix[inds[0]][inds[1]].isdigit():
            part_number = build_number(inds[0], inds[1])
            if part_number:
                part_numbers_found += 1
                part_numbers.append(part_number)

    if part_numbers_found == 2:
        gear_ratios.append(int(part_numbers[0]) * int(part_numbers[1]))

    return


for row_ind, row_value in enumerate(matrix):
    for col_ind, row_value in enumerate(row_value):
        if matrix[row_ind][col_ind] == '*':
            adjacency_check(row_ind, col_ind)
            gear_inds_added.append([row_ind, col_ind])
            part_number_inds_found = []


answer = sum(gear_ratios)

print(answer)
