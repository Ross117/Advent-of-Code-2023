import regex as re

with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

def get_number(str_to_parse):

    m = re.findall(r'\d+', str_to_parse)

    if m is not None:
        return int(m[0])

    return None

def get_string(str_to_parse):

    m = re.findall(r'\D+', str_to_parse.strip())

    if m is not None:
        return m[0].strip()

    return None

games = []

for game in input:
    info = {
        'id': 0,
        'red': [],
        'green': [],
        'blue': []
    }

    split_game = game.split(':')

    id = get_number(split_game[0])
    info['id'] = id

    cleaned_game = split_game[1].replace(';', ',').split(',')

    for value in cleaned_game:
        colour = get_string(value)
        info[colour].append(get_number(value))

    games.append(info)


powers = []

for game in games:

    max_red = max(game['red'])
    max_green = max(game['green'])
    max_blue = max(game['blue'])

    power = max_red * max_green * max_blue
    powers.append(power)

print(sum(powers))
