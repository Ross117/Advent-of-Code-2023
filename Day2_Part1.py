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

bag_contents = {
    'red': 12,
    'green': 13,
    'blue': 14
}

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


valid_game_ids = []

for game in games:

    valid = True

    invalid_red = [red for red in game['red'] if red > bag_contents['red']]
    invalid_green = [green for green in game['green'] if green > bag_contents['green']]
    invalid_blue = [blue for blue in game['blue'] if blue > bag_contents['blue']]

    if len(invalid_red) > 0  or len(invalid_green) > 0 or len(invalid_blue) > 0:
        valid = False

    if valid:
        valid_game_ids.append(game['id'])

print(sum(valid_game_ids))