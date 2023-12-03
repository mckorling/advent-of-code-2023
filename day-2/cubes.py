cube_limit_map = {
    "red": 12,
    "green": 13,
    "blue": 14
}

# if the game can be played within the limit map, return the game's id
# the id's of all playable games will be added together and returned in different method
# Game 1: 8 green, 4 red, 4 blue; 1 green, 6 red, 4 blue; 7 red, 4 green, 1 blue; 2 blue, 8 red, 8 green
# each reveal is seperated by a ';' (a reveal is a handful of dice grabbed)
# only three colored dice exist, and that count is separted by ',
def convert_game(game):
    id_and_reveals = game.split(': ')
    id = int(id_and_reveals[0].split(' ')[1])
    all_reveals = id_and_reveals[1]
    reveals = all_reveals.split('; ')
    for r in reveals:
        combo = r.split(', ')
        for c in combo:
            [count, color] = c.split(' ')
            if cube_limit_map[color] < int(count):
                return None
    return int(id)

# Find the minimum number of dice for each game
# minimum number of dice = highest value for r, g, b in each hand
# minimum number is multipled against each other and returned
# different method will sum all ints returned here
def convert_game_part_2(game):
    id_and_reveals = game.split(': ')
    reveals = id_and_reveals[1].split('; ')
    min_map = {
        "red": 0,
        "green": 0,
        "blue": 0
    }
    for r in reveals:
        combo = r.split(', ')
        for c in combo:
            [count, color] = c.split(' ')
            if int(count) > min_map[color]:
                min_map[color] = int(count)

    return min_map["red"] * min_map["blue"] * min_map["green"]

# convert file
games_list = []
file = open("/Users/megankorling/Developer/advent-of-code-23/day-2/data.txt", "r")
for line in file:
    clean_line = line.strip()  
    games_list.append(clean_line)

# Test case, expecting 8
test_games = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]


# main function for part 1 (id sums)
def get_id_sum(games):
    id_sum = 0
    for g in games:
        id = convert_game(g)
        if id:
            id_sum += id

    return id_sum

# Submitting answer
print(get_id_sum(games_list)) #2085
# print(get_id_sum(test_games)) # 8


# main function for part 2 (power sums)
def get_power_sum(games):
    total = 0
    for g in games:
        curr_power_sum = convert_game_part_2(g)
        total += curr_power_sum
    return total

# print(get_power_sum(test_games)) # 2286
print(get_power_sum(games_list))