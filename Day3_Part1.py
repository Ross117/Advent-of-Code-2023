with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

part_numbers = []
inds_added = []

matrix = [list(line) for line in input]

def adjacency_check(row_ind, col_ind):

    def symbol_check(r_ind, c_ind):

        try:
            if not matrix[r_ind][c_ind].isdigit() and matrix[r_ind][c_ind] != '.':
                return True
        except IndexError:
            pass

        return False

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

    is_symbol = False

    for inds in inds_to_check:
        is_symbol = symbol_check(inds[0], inds[1])
        if is_symbol:
            return True

    return False

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

    if inds_used not in inds_added:
        part_numbers.append(int(number))
        inds_added.append(inds_used)


for row_ind, row_value in enumerate(matrix):
    for col_ind, row_value in enumerate(row_value):
        if matrix[row_ind][col_ind].isdigit():
            if adjacency_check(row_ind, col_ind):
                build_number(row_ind, col_ind)


answer = sum(part_numbers)

print(answer)
