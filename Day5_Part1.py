with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n\n')

input_cleaned = [[val.split(' ') for val in val[val.index(':') + 1:].strip().split('\n')] for val in input]

seeds = [int(num) for num in input_cleaned[0][0]]

def get_mapping(source, mappings):

    for map in mappings:

        map_cleaned = [int(val) for val in map]
        destination_start, source_start, range = map_cleaned

        if source >= source_start and source < (source_start + range):
            differential = destination_start - source_start
            new_source = source + differential
            return new_source

    # if no mapping found, return source number unchanged
    return source

min_location = 0

for seed in seeds:

    source = seed

    for ind, mapping in enumerate(input_cleaned):

        if ind == 0:
            continue

        source = get_mapping(source, mapping)

    if min_location == 0:
        min_location = source
    elif source < min_location:
        min_location = source

print(min_location)
