import math

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

directions: list[str] = list(input[0])

network: dict[str, list[str]] = {}

# clean data to create network dictionary
for ind, value in enumerate(input):
    if ind > 1:
        network[value[0:3]] = [value[7:10], value[12:15]]

start_nodes: list[str] = [key for key in network if key.endswith('A')]
steps_list: list[int] = []

for node in start_nodes:

    end_found: bool = False
    steps: int = 0
    ind: int = 0

    while not end_found:

        steps += 1

        if directions[ind] == 'L':
            side = 0
        elif directions[ind] == 'R':
            side = 1

        node = network[node][side]

        if node.endswith('Z'):
            print(f'{node} found in {steps} steps!')
            end_found = True
            steps_list.append(steps)

        if (ind + 1) == len(directions):
            ind = 0
        else:
            ind += 1

# need to find the least common multiplier of each the step count for each invidual node
print(math.lcm(*steps_list))
