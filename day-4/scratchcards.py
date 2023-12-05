test_values = [
    "Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53",
    "Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19",
    "Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1",
    "Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83",
    "Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36",
    "Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11"
]

file = open("/Users/megankorling/Developer/advent-of-code-23/day-4/data.txt", "r")
cards = []
for line in file:
    cards.append(line.strip())

# winning numbers are before the '|'
# number user holds is after
# the first match is worth 1 point
# every other match is worth *2 poinst
# return the total number of points from all cards

# helper function
# translates the string representing a whole game and translates it to return
# [{winning numbers}, {user numbers}]
def convert_card(card):
    all_nums = card.split(": ")[1]
    [wins, users] = all_nums.split(" | ")
    winning_nums = wins.split(" ")
    user_nums = users.split(" ")

    winning_nums_set = set()
    for w in winning_nums:
        if w != "":
            winning_nums_set.add(int(w))
    
    user_nums_set = set()
    for u in user_nums:
        if u != "":
            user_nums_set.add(int(u))

    return [winning_nums_set, user_nums_set]

# helper function
# calculate points per card
def get_card_points(winning_nums, user_nums):
    found_match = False
    total = 0
    for w_num in winning_nums:
        if w_num in user_nums:
            if not found_match:
                found_match = True
                total = 1
            else:
                total *= 2
    return total

# main function
# loops through each game
# returns the total number of points
def calculate_points(cards):
    total = 0
    for card in cards:
        [winning_nums, user_nums] = convert_card(card)
        points = get_card_points(winning_nums, user_nums)
        total += points

    return total

# Part 1, test
# print(calculate_points(test_values)) # 13
# Part 1, actual
# print(calculate_points(cards)) # 25183


#-------------------------PART 2---------------------------------
# instead of adding points, count scratch cards won
# where x number of matches gives you the next x cards after the current one
# so 3 matches on card 3, means you get cards 4, 5, and 6 to process as a copy

# convert file to a dictionary 
# key = card number
# value = [{winning nums}, {user nums}]
def convert_card_with_key(card):
    sections = card.split(": ")
    all_nums = sections[1]
    id = int(sections[0].split(' ')[-1])
    [wins, users] = all_nums.split(" | ")
    winning_nums = wins.split(" ")
    user_nums = users.split(" ")

    winning_nums_set = set()
    for w in winning_nums:
        if w != "":
            winning_nums_set.add(int(w))
    
    user_nums_set = set()
    for u in user_nums:
        if u != "":
            user_nums_set.add(int(u))

    return [id, winning_nums_set, user_nums_set]

cards_map = {}
for card in cards:
    card_values = convert_card_with_key(card)
    cards_map[card_values[0]] = [card_values[1], card_values[2]]

test_map = {}
for card in test_values:
    card_values = convert_card_with_key(card)
    test_map[card_values[0]] = [card_values[1], card_values[2]]

# track list with cards
# loop through it and find matches
# add the next card numbers to list
# once the loop is exited, return the length of the list
def get_card_matches(winning_nums, user_nums):
    total = 0
    for w_num in winning_nums:
        if w_num in user_nums:
            total += 1
    return total

def calculate_matches(cards_map):
    valid_cards = list(cards_map.keys())
    i = 0
    while i < len(valid_cards):
        # print(f"i: {i}, valid cards: {sorted(valid_cards)}")
        curr_card = valid_cards[i]
        [winning_nums, user_nums] = cards_map[curr_card]
        matches = get_card_matches(winning_nums, user_nums)
        # print(f"current card: {curr_card}, matches: {matches}")

        for j in range(matches):

            valid_cards.append(j + curr_card + 1)
        i += 1

    return len(valid_cards)

# print(test_map)
print(calculate_matches(test_map)) # 30
print(calculate_matches(cards_map)) # 5667240