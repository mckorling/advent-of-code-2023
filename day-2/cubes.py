cube_limit_map = {
    "red": 12,
    "green": 13,
    "blue": 14
}

def convert_game(game):
    id_and_reveals = game.split(': ')
    id = int(id_and_reveals[0].split(' ')[1])
    all_reveals = id_and_reveals[1]
    reveals = all_reveals.split('; ')
    for r in reveals:
        grab = r.split(', ')
        for g in grab:
            [count, color] = g.split(' ')
            if cube_limit_map[color] < int(count):
                return None
    return int(id)

# convert file
games_list = []
file = open("/Users/megankorling/Developer/advent-of-code-23/day-2/data.txt", "r")
for line in file:
    clean_line = line.strip()  
    games_list.append(clean_line)

# main function
def get_id_sum(games):
    id_sum = 0
    for g in games:
        id = convert_game(g)
        if id:
            id_sum += id

    return id_sum

# Submitting answer
print(get_id_sum(games_list))

# Test case, expecting 8
test_games = [
    "Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
    "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
    "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
    "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
    "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"
]
# print(get_id_sum(test_games))