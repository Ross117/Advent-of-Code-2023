with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n')

input_cleaned = [[val for val in val if val.isdigit()] for val in input]
input_cleaned = [int(''.join(val)) for val in input_cleaned]

def beats_record(hold_time, race_time, distance):

    if hold_time * (race_time - hold_time) > distance:
        return True

    return False

ways = 0

race_time = input_cleaned[0]
distance = input_cleaned[1]

for hold_time in range(1, race_time):
    if beats_record(hold_time, race_time, distance):
        ways += 1

print(ways)
