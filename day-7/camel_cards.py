from collections import Counter

# In Camel Cards, you get a list of hands, and your goal is to order them based on the strength of each hand. A hand consists of five cards labeled one of A, K, Q, J, T, 9, 8, 7, 6, 5, 4, 3, or 2. The relative strength of each card follows this order, where A is the highest and 2 is the lowest.

# Every hand is exactly one type. From strongest to weakest, they are:

# Five of a kind, where all five cards have the same label: AAAAA
# Four of a kind, where four cards have the same label and one card has a different label: AA8AA
# Full house, where three cards have the same label, and the remaining two cards share a different label: 23332
# Three of a kind, where three cards have the same label, and the remaining two cards are each different from any other card in the hand: TTT98
# Two pair, where two cards share one label, two other cards share a second label, and the remaining card has a third label: 23432
# One pair, where two cards share one label, and the other three cards have a different label from the pair and each other: A23A4
# High card, where all cards' labels are distinct: 23456
# Hands are primarily ordered based on type; for example, every full house is stronger than any three of a kind.

# If two hands have the same type, a second ordering rule takes effect. Start by comparing the first card in each hand. If these cards are different, the hand with the stronger first card is considered stronger. If the first card in each hand have the same label, however, then move on to considering the second card in each hand. If they differ, the hand with the higher second card wins; otherwise, continue with the third card in each hand, then the fourth, then the fifth.

# So, 33332 and 2AAAA are both four of a kind hands, but 33332 is stronger because its first card is stronger. Similarly, 77888 and 77788 are both a full house, but 77888 is stronger because its third card is stronger (and both hands have the same first and second card).

# To play Camel Cards, you are given a list of hands and their corresponding bid (your puzzle input). For example:

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483

# This example shows five hands; each hand is followed by its bid amount. Each hand wins an amount equal to its bid multiplied by its rank, where the weakest hand gets rank 1, the second-weakest hand gets rank 2, and so on up to the strongest hand. Because there are five hands in this example, the strongest hand will have rank 5 and its bid will be multiplied by 5.

# So, the first step is to put the hands in order of strength:

# 32T3K is the only one pair and the other hands are all a stronger type, so it gets rank 1.
# KK677 and KTJJT are both two pair. Their first cards both have the same label, but the second card of KK677 is stronger (K vs T), so KTJJT gets rank 2 and KK677 gets rank 3.
# T55J5 and QQQJA are both three of a kind. QQQJA has a stronger first card, so it gets rank 5 and T55J5 gets rank 4.
# Now, you can determine the total winnings of this set of hands by adding up the result of multiplying each hand's bid with its rank (765 * 1 + 220 * 2 + 28 * 3 + 684 * 4 + 483 * 5). So the total winnings in this example are 6440.

test_values = {
    "32T3K": 765,
    "T55J5": 684,
    "KTJJT": 220,
    "KK677": 28,
    "QQQJA": 483,
    "QJJQ2": 100,
    "QQQQ2": 200
    # "33332": 100,
    # "2AAAA": 200,
    # "77888": 300,
    # "77788": 400
}

# convert data to a dict
# key is hand
# value is bid
def convert_file(file_name):
    data_map = {}
    file = open(file_name, "r")
    for line in file:
        key_value = line.strip().split(" ")
        data_map[key_value[0]] = int(key_value[1])
    return data_map

# print(convert_file("/Users/megankorling/Developer/advent-of-code-23/day-7/data.txt"))

def is_two_pair(card_map):
    for c in card_map:
        if card_map[c] == 3:
            return False
    return True

def is_full_house(card_map):
    for c in card_map:
        if card_map[c] == 4:
            return False
    return True

# go through each key and find it's type
# put the hand in a list (or something) depending on it's type
# custom sort (make sure lower number is prioritized) after all hands have been processed
# use one for loop to loop through all lists
# i + 1 is the rank
# then track the overall total
# add: ((i+1) * map[key]) this will get the bid number because the hand hasn't been modified
def get_hand_type(cards):
    card_map = Counter(cards)
    map_len = len(card_map)
    if map_len == 5:
        return "high"
    elif map_len == 4:
        return "one-pair"
    elif map_len == 3:
        if is_two_pair(card_map):
            return "two-pair"
        return "three"
    elif map_len == 2:
        if is_full_house(card_map):
            return "full"
        return "four"
    else:
        return "five"
    
card_hands_map = {
    "high": [],
    "one-pair": [],
    "two-pair": [],
    "three": [],
    "full": [],
    "four": [],
    "five": []
}

SORT_ORDER = "23456789TJQKA"

def process_hands(data_map):
    for hand in data_map:
        hand_type = get_hand_type(hand)
        card_hands_map[hand_type].append(hand)

    for key, value in card_hands_map.items():
        card_hands_map[key] = sorted(value, key=lambda word: [SORT_ORDER.index(c) for c in word])
    # print(card_hands_map)
    total = 0
    rank = 1
    for hand_type in card_hands_map:
        for hand in card_hands_map[hand_type]:
            # print(f"{rank} * {data_map[hand]} = {rank * data_map[hand]}")
            total += (rank * data_map[hand])
            rank += 1

    return total

# print(process_hands(test_values)) # 6440

data = convert_file("/Users/megankorling/Developer/advent-of-code-23/day-7/data.txt")
# print(process_hands(data)) # 250474325


#---------------------------Part 2----------------------------------
# Now, J cards are jokers - wildcards that can act like whatever card would make the hand the strongest type possible.

# To balance this, J cards are now the weakest individual cards, weaker even than 2. The other cards stay in the same order: A, K, Q, T, 9, 8, 7, 6, 5, 4, 3, 2, J.

# J cards can pretend to be whatever card is best for the purpose of determining hand type; for example, QJJQ2 is now considered four of a kind. However, for the purpose of breaking ties between two hands of the same type, J is always treated as J, not the card it's pretending to be: JKKK2 is weaker than QQQQ2 because J is weaker than Q.

# Now, the above example goes very differently:

# 32T3K 765
# T55J5 684
# KK677 28
# KTJJT 220
# QQQJA 483
# 32T3K is still the only one pair; it doesn't contain any jokers, so its strength doesn't increase.
# KK677 is now the only two pair, making it the second-weakest hand.
# T55J5, KTJJT, and QQQJA are now all four of a kind! T55J5 gets rank 3, QQQJA gets rank 4, and KTJJT gets rank 5.
# With the new joker rule, the total winnings in this example are 5905.

SORT_ORDER_TWO = "J23456789TQKA"

def get_max_card_count(card_map):
    max_count = 0
    max_char = ''
    for c in card_map:
        if c == 'J':
            continue
        else:
            if card_map[c] > max_count:
                max_count = card_map[c]
                max_char = c
    if max_char:
        return max_char
    else:
        return 'J'

def is_two_pair_part_2(card_map):
    j_count = card_map['J']
    max_char = get_max_card_count(card_map)
    card_map[max_char] += j_count
    for c in card_map:
        if c != 'J' and card_map[c] == 3:
            # 3 of a kind
            return False 
    return True

def is_full_house_part_2(card_map):
    j_count = card_map['J']
    max_char = get_max_card_count(card_map)
    card_map[max_char] += j_count
    # print(card_map)
    for c in card_map:
        if c != 'J' and card_map[c] == 4:
            # 4 of a kind
            return False
    return True

def get_hand_type_part_2(cards):
    card_map = Counter(cards)
    map_len = len(card_map)
    if 'J' in card_map:
        map_len -= 1
    # print(f"{cards} {map_len}")
    if map_len == 5:
        return "high"
    elif map_len == 4:
        return "one-pair"
    elif map_len == 3:
        if is_two_pair_part_2(card_map):
            return "two-pair"
        return "three"
    elif map_len == 2:
        if is_full_house_part_2(card_map):
            return "full"
        return "four"
    else:
        return "five"

# this would be easy to adapt to use for either scenario
# just add a parameter, boolean, is_part_two, then only need to update:
# hand_type variable and SORT_ORDER    
def process_hands_part_2(data_map):
    for hand in data_map:
        hand_type = get_hand_type_part_2(hand)
        card_hands_map[hand_type].append(hand)

    for key, value in card_hands_map.items():
        card_hands_map[key] = sorted(value, key=lambda word: [SORT_ORDER_TWO.index(c) for c in word])
    total = 0
    rank = 1
    for hand_type in card_hands_map:
        for hand in card_hands_map[hand_type]:
            total += (rank * data_map[hand])
            rank += 1

    return total

# print(process_hands_part_2(test_values)) # 5905

print(process_hands_part_2(data)) # 248909434
# first submission was too high: 249407075
# it was because i didn't update all the function names to use '_part_2'