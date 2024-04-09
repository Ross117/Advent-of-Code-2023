with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

directions: list[str] = list(input[0])

network: dict[str, list[str]] = {}

# clean data to create network dictionary
for ind, value in enumerate(input):
    if ind > 1:
        network[value[0:3]] = [value[7:10], value[12:15]]

current_node: str = 'AAA'
steps: int = 0
end_found: bool = False

ind: int = 0

while not end_found:

    steps += 1

    if directions[ind] == 'L':
        side = 0
    elif directions[ind] == 'R':
        side = 1

    current_node = network[current_node][side]

    if current_node == 'ZZZ':
        print(f'{current_node} found in {steps} steps!')
        end_found = True

    if (ind + 1) == len(directions):
        ind = 0
    else:
        ind += 1
