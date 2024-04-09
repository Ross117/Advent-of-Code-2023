with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

hands = [val.split(' ') for val in input]

card_strength = {
    'A': '112', 'K': '111', 'Q': '110',
    'T': '109', '9': '108', '8': '107',
    '7': '106', '6': '105', '5': '104',
    '4': '103', '3': '102', '2': '101',
    'J': '100'
}

hand_order = []

# assign a score to each hand then rank based on score - convert hand to numeric values, then will naturally sort in right order
for ind, hand in enumerate(hands):

    # if the hand includes 1+ joker - the joker is replaced by another card which appears the most
    # in the case of a tie (highest card count is 1 OR 2), joker is replaced by the highest ranking card
    # need to keep the joker in the hand when working out the total numeric value though!!

    if 'J' in hand[0] and hand[0].count('J') < 5:
        card_counts = [[card, hand[0].count(card),
                        int(card_strength[card])] for card in hand[0] if card != 'J']
        card_counts.sort(reverse=True, key=lambda x: (x[1], x[2]))
        updated_hand = hand[0].replace('J', card_counts[0][0])
    else:
        updated_hand = hand[0]

    cards_checked = []

    # the overall score of the hand
    score = 0

    for card in updated_hand:

        if card not in cards_checked:
            if updated_hand.count(card) == 5:
                score = 11
                break
            elif updated_hand.count(card) == 4:
                score = 10
                break
            elif updated_hand.count(card) == 3:
                score += 6
                cards_checked.append(card)
            elif updated_hand.count(card) == 2:
                score += 2
                cards_checked.append(card)

    hands[ind].append(score)

    numeric_val = ''
    for card in hand[0]:
        numeric_val = numeric_val + card_strength[card]
    hands[ind].append(numeric_val)

hands.sort(reverse=False, key=lambda x: (x[2], x[3]))

total_winnings = sum([int(hand[1]) * (ind + 1) for ind, hand in enumerate(hands)])

print(total_winnings)
