# Takes in one string like pqr3stu8vwx
# Returns the integer value of the 
# first and last digit added together like a string
def get_int_value(calibration_value):
    first = None
    second = None

    for v in calibration_value:
        if v.isdigit():
            if first is None:
                first = v
            second = v

    return int(first + second)

map = {
    "one": "1",
    "two": "2",
    "three": "3",
    "four": "4",
    "five": "5",
    "six": "6",
    "seven": "7",
    "eight": "8",
    "nine": "9",
    "1": "1",
    "2": "2",
    "3": "3",
    "4": "4",
    "5": "5",
    "6": "6",
    "7": "7",
    "8": "8",
    "9": "9"
}

# Part two of problem where abcone2threexyz is 13, and is not 22
def get_int_value_2(calibration_value):
    copy = calibration_value
    first = None
    second = None
    while len(copy) > 0:
        for key in map:
            if copy.startswith(key):
                if first == None:
                    first = map[key]
                second = map[key]
        copy = copy[1:]

    return int(first + second)

# Takes in a list of calibration_values, like pqr3stu8vwx
# Calculates the integer value with helper function
# Adds to total sum
# Returns the sum of all integers
def calculate_total(calibration_values):
    total_sum = 0
    for value in calibration_values:
        # Part 1
        # current_int = get_int_value(value)

        # Part 2
        current_int = get_int_value_2(value)
        total_sum += current_int

    return total_sum

# Data for submitting answer
file = open("/Users/megankorling/Developer/advent-of-code-23/day-1/data.txt", "r")
values2 = []
for line in file:
    values2.append(line)


# Test of Part 1 of problem
# values = ["1abc2", "pqr3stu8vwx", "a1b2c3d4e5f","treb7uchet"]
# print(calculate_total(values))

# Submitted Answer
# print(calculate_total(values2)) #55130

#-----------------------------------
# Test of Part 2
values3 = ["two1nine", "eightwothree", "abcone2threexyz", "xtwone3four", "4nineeightseven2", "zoneight234", "7pqrstsixteen"]
# print(calculate_total(values3))

# Submitted Answer
print(calculate_total(values2)) # 54985