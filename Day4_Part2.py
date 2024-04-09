with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [
                  [[card.split(':')[1].split('|')[0].strip().split(' '),
                    card.split(':')[1].split('|')[1].strip().split(' ')
                   ]] for card in input
                ]

for ind, card_container in enumerate(input_cleaned):

    for card in card_container:

        winning_nums = [int(num) for num in card[0] if num != '']
        my_nums = [int(num) for num in card[1] if num != '']

        crossover = [num for num in my_nums if num in winning_nums]

        total_winning_nums = len(crossover)

        if total_winning_nums > 0:
            for i in range(ind + 1, ind + 1 + total_winning_nums):
                input_cleaned[i].extend([input_cleaned[i][0]])

total_cards = sum(len(card_container) for card_container in input_cleaned)

print(total_cards)