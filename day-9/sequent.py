# convert data
# make into list of lists
data = []
file = open("/Users/megankorling/Developer/advent-of-code-23/day-9/data.txt", "r")
for line in file:
    line = line.strip()
    str_vals = line.split(" ")
    int_vals = [int(x) for x in str_vals]
    data.append(int_vals)

test_values = [
    [0, 3, 6, 9, 12, 15],
    [1, 3, 6, 10, 15, 21],
    [10, 13, 16, 21, 30, 45]
]

# go through each sequence in the loop
# make a temporary array for current sequence
# go through each number in the loop (starting at index 1)
# calculate the differnce and add it to a new list
# if all are 0, that is the base case, return the last number of the array
# else repeat calculating difference
def calculate_sequences(sequences):
    all_totals = 0
    for seq in sequences:
        all_totals += seq[-1] + calculate_single_sequence(seq)
        # print("")
        # print(f"sequence {seq}, total {all_totals}")
    return all_totals


def calculate_single_sequence(sequence): 
    # print(sequence)
    if len(set(sequence)) == 1:
        # print(f"base case, adding {sequence[-1]}")
        return 0
    
    temp_list = []
    for i in range(1, len(sequence)):
        difference = sequence[i] - sequence[i-1]
        temp_list.append(difference)
    # print(f"new sequence {temp_list}, adding {temp_list[-1]}")
    return temp_list[-1] + calculate_single_sequence(temp_list)
        
# print(calculate_sequences(test_values)) # 114
print(calculate_sequences(data)) # 1834108701