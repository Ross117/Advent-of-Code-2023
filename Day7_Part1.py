with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

hands = [val.split(' ') for val in input]

card_strength = {
    'A': '112', 'K': '111', 'Q': '110',
    'J': '109', 'T': '108', '9': '107',
    '8': '106', '7': '105', '6': '104',
    '5': '103', '4': '102', '3': '101',
    '2': '100'
}

hand_order = []

# assign a score to each hand then rank based on score - convert hand to numeric values, then will naturally sort in right order
for ind, hand in enumerate(hands):

    cards_checked = []

    # the overall score of the hand
    score = 0

    for card in hand[0]:
        if card not in cards_checked:
            if hand[0].count(card) == 5:
                score = 11
                break
            if hand[0].count(card) == 4:
                score = 10
                break
            if hand[0].count(card) == 3:
                score += 6
                cards_checked.append(card)
            if hand[0].count(card) == 2:
                score += 2
                cards_checked.append(card)

    hands[ind].append(score)

    # the total numeric value of the hand's card strength
    numeric_val = ''
    for card in hand[0]:
        numeric_val = numeric_val + card_strength[card]
    hands[ind].append(numeric_val)

hands.sort(reverse=False, key=lambda x: (x[2], x[3]))

total_winnings = sum([int(hand[1]) * (ind + 1) for ind, hand in enumerate(hands)])

print(total_winnings)
