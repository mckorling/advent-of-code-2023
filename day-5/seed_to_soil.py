# test_values = [
#     "seeds: 79 14 55 13",
#     "",
#     "seed-to-soil map:",
#     "50 98 2",       # 79 = 79
#     "52 50 48",       # 79 = 81
#     "",
#     "soil-to-fertilizer map:",
#     "0 15 37",       # 79 = 79, 81 = 81
#     "37 52 2",      # 79 = 79, 81 = 81
#     "39 0 15",      # 79 = 79, 81 = 81
#     "", #14, 53
#     "fertilizer-to-water map:",
#     "49 53 8",  # 79 = 79, 81 = 81
#     "0 11 42",  # 79 = 79, 81 = 81
#     "42 0 7",   # 79 = 79, 81 = 81
#     "57 7 4",   # 79 = 79, 81 = 81
#     "", #14, 49, 3, 42, 53
#     "water-to-light map:",
#     "88 18 7",  # 79 = 79, 81 = 81
#     "18 25 70", # 79 = 72, 81 = 74
#     "", #14, 3, 42, 49, 53, 35, 46
#     "light-to-temperature map:",
#     "45 77 23", # 72 = 72, 74 = 74, 79 = 47, 81 = 49
#     "81 45 19", # 72, 74, 79, 81
#     "68 64 13", # 72, 74 = 78, 79 = 83, 81 = 85
#     "", #14, 3, 42, 49, 35, 89, 82
#     "temperature-to-humidity map:",
#     "0 69 1",   # 47, 49, 72, 74, 79, 81, 83, 85
#     "1 0 69",   # 47 = 48, 49 = 50, 72, 74, 79, 81, 83, 85
#     "", #14, 
#     "humidity-to-location map:",
#     "60 56 37", # 48 = 52, 50 = 54, 72 = 76, 74 = 78, 79 = 83, 81 = 85, 83 = 87, 85 = 89
#     "56 93 4"
# ]
test_values = [
    [79, 14, 55, 13],
    [
        "50 98 2",       # 79 = 79
        "52 50 48",       # 79 = 81
    ],
    [
        "0 15 37",       # 79 = 79, 81 = 81
        "37 52 2",      # 79 = 79, 81 = 81
        "39 0 15",      # 79 = 79, 81 = 81
    ],
    [
        "49 53 8",  # 79 = 79, 81 = 81
        "0 11 42",  # 79 = 79, 81 = 81
        "42 0 7",   # 79 = 79, 81 = 81
        "57 7 4",   # 79 = 79, 81 = 81
    ],
    [
        "88 18 7",  # 79 = 79, 81 = 81
        "18 25 70", # 79 = 72, 81 = 74
    ],
    [
        "45 77 23", # 72 = 72, 74 = 74, 79 = 47, 81 = 49
        "81 45 19", # 72, 74, 79, 81
        "68 64 13", # 72, 74 = 78, 79 = 83, 81 = 85
    ],
    [
        "0 69 1",   # 47, 49, 72, 74, 79, 81, 83, 85
        "1 0 69",   # 47 = 48, 49 = 50, 72, 74, 79, 81, 83, 85
    ],
    [
        "60 56 37", # 48 = 52, 50 = 54, 72 = 76, 74 = 78, 79 = 83, 81 = 85, 83 = 87, 85 = 89
        "56 93 4"
    ]
]
# expected answer is 35
# Seed 79, soil 81, fertilizer 81, water 81, light 74, temperature 78, humidity 78, location 82.
# Seed 14, soil 14, fertilizer 53, water 49, light 42, temperature 42, humidity 43, location 43.
# Seed 55, soil 57, fertilizer 57, water 53, light 46, temperature 82, humidity 82, location 86.
# Seed 13, soil 13, fertilizer 52, water 41, light 34, temperature 34, humidity 35, location 35.

# The map is not a series of options, but rather describes a whole range of numbers
# so:
# seed  soil
# 0     0
# 1     1
# ...   ...
# 48    48
# 49    49
# 50    52
# 51    53
# ...   ...
# 96    98
# 97    99
# 98    50
# 99    51

file = "/Users/megankorling/Developer/advent-of-code-23/day-5/data.txt"
def convert_file(file_string):
    values = ["seeds", [], [], [], [], [], [], []]
    file = open(file_string, "r")
    index = 0
    for line in file:
        line = line.strip()
        if line.startswith("seeds"):
            str_seeds = line.split(": ")[1]
            seeds = str_seeds.split(" ")
            int_seeds = [int(x) for x in seeds]
            values[index] = int_seeds
        elif line != "" and not line[0].isdigit():
            index += 1
        else:
            if line == "":
                continue
            values[index].append(line)

    return values
            
# helper function
# destination, source, range
# if input number is within source + range
# then return the input + (source - destination)
def conversion(value, destination, source, range):
    difference = destination - source
    if source <= value <= source + range:
        value += difference
    return value

# track a set for each map that tracks numbers that have been processed
# if a number is in the set, break
# otherwise, keep looping and calculating, then add it to set
# loop through each seed
# loop through each map
# loop through each interval, run helper function
# track the minimum returned by the last map
data = convert_file(file)
def calculate_lowest_local_num(data):
    seeds = data[0]
    lowest_local = float('inf')
    for s in seeds:
        # print(f"s: {s}")
        curr_num = s
        for i in range(1, len(data)):
            for j in range(len(data[i])):
                values = data[i][j].split(" ")
                # print(values)
                dest = int(values[0])
                source = int(values[1])
                r = int(values[2])
                # mapped_val = conversion(curr_num, dest, source, r)
                if source <= curr_num <= source + r:
                    # print(values)
                    curr_num += (dest - source)
                    break

        lowest_local = min(lowest_local, curr_num)
        # print(f"s: {s}, lowest: {lowest_local}")
    return lowest_local


# print(calculate_lowest_local_num(data)) # 535088217
# print(calculate_lowest_local_num(test_values)) # 35


# local_num = s
#         for i in range(1, len(data)):
#             values = data[i].split(" ")
#             dest = int(values[0])
#             source = int(values[1])
#             r = int(values[2])
#             local_num = conversion(local_num, dest, source, r)
#         lowest_local = min(lowest_local, local_num)