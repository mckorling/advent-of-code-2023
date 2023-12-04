# convert file
file = open("/Users/megankorling/Developer/advent-of-code-23/day-3/data.txt", "r")
schematic = []
for line in file:
    schematic.append(line.strip())

# any number that has a digit that touches a special character (diagonal counts)
# is add to a running total
# return that total
def calculate_all_part_numbers(schematic_values):
    total = 0
    for i in range(len(schematic_values)):
        for j in range(len(schematic_values[i])):
            if is_special_character(schematic_values[i][j]):
                total += get_surrounding_numbers(i, j, len(schematic_values), len(schematic_values[0]), schematic_values)

    return total

# returns the total of numbers surrounding a special character
def get_surrounding_numbers(i, j, max_i, max_j, schematics):
    # print(schematics[i][j])
    totals = []
    used_coords = set()
    directions = [
        [i-1, j], # up
        [i-1, j+1], # up right
        [i, j+1], # right
        [i+1, j+1], # down right
        [i+1, j], # down
        [i+1, j-1], # down left
        [i, j-1], # left
        [i-1, j-1]  # up left
    ]
    # loop through the eight possible neighbors to i and j
    for d in directions:
        if 0<= d[0] < max_i and 0 <= d[1] < max_j:
            # print(schematics[d[0]][d[1]])

            if schematics[d[0]][d[1]].isdigit():
                if f"({d[0]}, {d[1]})" in used_coords:
                    continue
                used_coords.add(f"({d[0]}, {d[1]})")
                pre_j = d[1] - 1
                post_j = d[1] + 1
                num = schematics[d[0]][d[1]]
                while pre_j >= 0:
                    if schematics[d[0]][pre_j].isdigit():
                        num = schematics[d[0]][pre_j] + num
                        used_coords.add(f"({d[0]}, {pre_j})")
                        pre_j -= 1
                    else:
                        pre_j = -1
                while post_j < max_j:
                    if schematics[d[0]][post_j].isdigit():
                        num += schematics[d[0]][post_j]
                        used_coords.add(f"({d[0]}, {post_j})")
                        post_j += 1
                    else:
                        post_j = max_j + 1
                totals.append(int(num))

    # print(totals)
    return sum(totals)

def is_special_character(x):
    return not x.isalnum() and x != '.'


# Test case
test_values = [
    "467..114..",
    "...*......",
    "..35..633.",
    "......#...",
    "617*......",
    ".....+.58.",
    "..592.....",
    "......755.",
    "...$.*....",
    ".664.598.."
]

# Part 1, test
# print(calculate_all_part_numbers(test_values)) # 4361

# Part 1, Submit answer
# print(calculate_all_part_numbers(schematic)) # 559667

#-------------PART 2------------------------------------
# Only special character that counts is '*'
# It must have exactly two numbers touching it, two separate numbers (not two digits of the same number)
# Multiply numbers belonging to adjacent gears
# then sum all powers and return that number
def calculate_all_part_numbers_2(schematic_values):
    total = 0
    for i in range(len(schematic_values)):
        for j in range(len(schematic_values[i])):
            if schematic_values[i][j] == "*":
                total += get_surrounding_numbers_2(i, j, len(schematic_values), len(schematic_values[0]), schematic_values)

    return total

# returns the total of part numbers surrounding a special character
def get_surrounding_numbers_2(i, j, max_i, max_j, schematics):
    # print(schematics[i][j])
    numbers = []
    used_coords = set()
    directions = [
        [i-1, j], # up
        [i-1, j+1], # up right
        [i, j+1], # right
        [i+1, j+1], # down right
        [i+1, j], # down
        [i+1, j-1], # down left
        [i, j-1], # left
        [i-1, j-1]  # up left
    ]
    # loop through the eight possible neighbors to i and j
    for d in directions:
        if 0<= d[0] < max_i and 0 <= d[1] < max_j:
            # print(schematics[d[0]][d[1]])

            if schematics[d[0]][d[1]].isdigit():
                if f"({d[0]}, {d[1]})" in used_coords:
                    continue
                used_coords.add(f"({d[0]}, {d[1]})")
                pre_j = d[1] - 1
                post_j = d[1] + 1
                num = schematics[d[0]][d[1]]
                while pre_j >= 0:
                    if schematics[d[0]][pre_j].isdigit():
                        num = schematics[d[0]][pre_j] + num
                        used_coords.add(f"({d[0]}, {pre_j})")
                        pre_j -= 1
                    else:
                        pre_j = -1
                while post_j < max_j:
                    if schematics[d[0]][post_j].isdigit():
                        num += schematics[d[0]][post_j]
                        used_coords.add(f"({d[0]}, {post_j})")
                        post_j += 1
                    else:
                        post_j = max_j + 1
                numbers.append(int(num))

    # print(numbers)
    if len(numbers) == 2:
        return numbers[0] * numbers[1]
    return 0

# Part 2, test
print(calculate_all_part_numbers_2(test_values)) # 467835

# Part 2, submit answer
print(calculate_all_part_numbers_2(schematic)) # 86841457
