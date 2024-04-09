with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [
                  [card.split(':')[1].split('|')[0].strip().split(' '),
                    card.split(':')[1].split('|')[1].strip().split(' ')
                  ] for card in input
                ]

total_points = 0

for card in input_cleaned:

    winning_nums = [int(num) for num in card[0] if num != '']
    my_nums = [int(num) for num in card[1] if num != '']

    crossover = [num for num in my_nums if num in winning_nums]

    total_winning_nums = len(crossover)

    points = 0

    if len(crossover) > 0:
        points = 1
        for i in range(1, len(crossover)):
            points = points * 2

    total_points += points

print(total_points)