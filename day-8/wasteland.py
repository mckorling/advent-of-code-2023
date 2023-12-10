# convert the data
# take the first line and save it as a string
# from the node lines, add each to a dictionary
# the key is the left side, the value is the right side
file = open("/Users/megankorling/Developer/advent-of-code-23/day-8/data.txt", "r")
data_list = []
for line in file:
    data_list.append(line.strip())

directions = data_list[0]
node_map = {}
for node in data_list[2:]:
    line = node.split(" = ")
    node_map[line[0]] = (line[1][1:4], line[1][6:9]) 


# have an index to track the spot in the directions
# have variable to track steps taken
# have current node variable, starts at AAA
# loop while z is not found
# check first if index is within bounds, reset index if not
# track next node which is dict[current_node][0 = R or 1 = L]
# add to steps
# if it is ZZZ, return steps
# if not, set current to next, increment index
def calculate_steps(dir, nodes):
    dir_index = 0
    steps = 0
    curr_node = 'AAA'
    z_found = False
    while not z_found:
        if (dir_index == len(dir)):
            dir_index = 0
        if dir[dir_index] == 'R':
            curr_dir = 1
        if dir[dir_index] == 'L':
            curr_dir = 0
        # print(f"{curr_node} go {curr_dir}")
        next_node = nodes[curr_node][curr_dir]
        steps += 1
        if next_node == 'ZZZ':
            z_found = True
            return steps
        else:
            curr_node = next_node
            dir_index += 1


test_dirs = 'RL'
test_nodes = {
    "AAA": ['BBB', 'CCC'],
    "BBB": ['DDD', 'EEE'],
    "CCC": ['ZZZ', 'GGG'],
    "DDD": ['DDD', 'DDD'],
    "EEE": ['EEE', 'EEE'],
    "GGG": ['GGG', 'GGG'],
    "ZZZ": ['ZZZ', 'ZZZ']
}

test_dirs_2 = 'LLR'
test_nodes_2 = {
    "AAA": ['BBB', 'BBB'],
    "BBB": ['AAA', 'ZZZ'],
    "ZZZ": ['ZZZ', 'ZZZ']
}

# print(calculate_steps(test_dirs, test_nodes)) # 2
# print(calculate_steps(test_dirs_2, test_nodes_2)) # 6

# print(calculate_steps(directions, node_map))

#-------------------------PART 2------------------------------------

# take already converted data and make list of nodes ending in AAA
a_group = []
for key in node_map:
    if key[-1] == 'A':
        a_group.append(key)
# print(a_group)

# use similar calculate logic as above but add in a for loop that uses enumerate
# so instead of moving one node at a time, move a group at a time
# while moving it, have a tracker set False if any next node doesn't end in z
# can maybe use the same tracker as above
def calculate_steps_by_group(dir, nodes, node_group):
    dir_index = 0
    steps = 0
    curr_nodes = node_group
    z_found = False
    while not z_found:
        all_z = True
        if (dir_index == len(dir)):
            dir_index = 0
        if dir[dir_index] == 'R':
            curr_dir = 1
        if dir[dir_index] == 'L':
            curr_dir = 0
        print(f"{curr_nodes} go {curr_dir}")

        # for loop with enumerate
        next_nodes = []
        for count, node in enumerate(curr_nodes):
            # nodes[curr_node][curr_dir]
            next_node = nodes[curr_nodes[count]][curr_dir]
            next_nodes.append(next_node)
            if next_node[-1] != 'Z':
                all_z = False
        steps += 1
        if all_z:
            z_found = True
            return steps
        else:
            curr_nodes = next_nodes
            dir_index += 1

test_dirs_3 = 'LR'
test_nodes_3 = {
    '11A': ['11B', 'XXX'],
    '11B': ['XXX', '11Z'],
    '11Z': ['11B', 'XXX'],
    '22A': ['22B', 'XXX'],
    '22B': ['22C', '22C'],
    '22C': ['22Z', '22Z'],
    '22Z': ['22B', '22B'],
    'XXX': ['XXX', 'XXX']
}
test_node_group = ['11A', '22A']

# print(calculate_steps_by_group(test_dirs_3, test_nodes_3, test_node_group)) # 6

print(calculate_steps_by_group(directions, node_map, a_group))
# taking a long time to run..... times out