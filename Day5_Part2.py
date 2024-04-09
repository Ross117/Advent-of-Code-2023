with open('Input.txt', mode='r', encoding='utf-8') as file:
    input = file.read().split('\n\n')

input_cleaned = [[val.split(' ') for val in val[val.index(':') + 1:].strip().split('\n')] for val in input]

seeds = [int(num) for num in input_cleaned[0][0]]
seeds_cleaned = []

for i in range(0, len(seeds), 2):
    seeds_cleaned.append([seeds[i], seeds[i] + seeds[i + 1]])


def get_mapping(rngs, mappings):

    # mapping equates to a map in the source data
    # iterate through the rows in the map

    mapped_rngs = []

    for map in mappings:

        # map is a single row in a map
        map_cleaned = [int(val) for val in map]
        destination_start, source_start, num_in_rng = map_cleaned

        # iterate through the seed ranges
        for rng in rngs.copy():

            if rng in mapped_rngs:
                continue

            differential = destination_start - source_start

            # check it's within the range - this is where we'll split the ranges
            # does the seed range fully fit within the mapping range?
            if rng[0] >= source_start and rng[1] <= (source_start + num_in_rng):

                # append the mapped range
                rngs.append([rng[0] + differential, rng[1] + differential])
                # the range has been split, so remove the original range
                rngs.remove(rng)
                # don't re-map seeds which have already been mapped in the current map
                mapped_rngs.append([rng[0] + differential, rng[1] + differential])

            # does the seed range partially fit within the mapping range?
            elif rng[0] <= source_start and (rng[1] > source_start and rng[1] < (source_start + num_in_rng)):

                # append the mapped range & the remainder of the unmapped one
                rngs.extend([[source_start + differential, rng[1] + differential], [rng[0], source_start - 1]])
                rngs.remove(rng)
                mapped_rngs.append([source_start + differential, rng[1] + differential])

            elif (rng[0] >= source_start and rng[0] < (source_start + num_in_rng)) and rng[1] >= (source_start + num_in_rng):

                rngs.extend([[rng[0] + differential, (source_start + num_in_rng) + differential], [source_start + num_in_rng, rng[1]]])
                rngs.remove(rng)
                mapped_rngs.append([rng[0] + differential, (source_start + num_in_rng) + differential])

            elif rng[0] <= source_start and rng[1] >= (source_start + num_in_rng):

                rngs.extend([[source_start + differential, (source_start + num_in_rng - 1) + differential], [rng[0], source_start - 1], [source_start + num_in_rng, rng[1]]])
                rngs.remove(rng)
                mapped_rngs.append([source_start + differential, (source_start + num_in_rng - 1) + differential])

    return rngs


min_locs = []

# container for the sub-ranges derived from the original seed range
# starts with just the source seed range
rngs = seeds_cleaned.copy()

# iterate through all the maps in the source data
for ind, mapping in enumerate(input_cleaned):

    if ind == 0:
        continue

    rngs = get_mapping(rngs, mapping)

# we want to ge the lowest number from this list
rngs.sort()
min_locs.append(rngs[0][0])

min_locs.sort()
print(min_locs[0])