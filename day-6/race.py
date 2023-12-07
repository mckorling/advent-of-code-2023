# https://adventofcode.com/2023/day/6

file = open("/Users/megankorling/Developer/advent-of-code-23/day-6/data.txt", "r")
lines = []
for line in file:
    lines.append(line.strip())
time_line = lines[0].split(":")[1].split(" ")
times = [int(t) for t in time_line if t.isdigit()]
dists_line = lines[1].split(":")[1].split(" ")
dists = [int(d) for d in dists_line if d.isdigit()]

test_times = [7, 15, 30]
test_dists = [9, 40, 200]
# answer: 4 * 8 * 9 = 288
# 4 = num of ways to win in race 1
# 8 = in race 2
# 9 = in race 3

# need to hold down the button to give the boat a starting speed
# Holiding it down for 1ms means travelling at 1mm / ms for 6ms, 
# which means the distance traveled is 6mm (not 7mm, because for 1ms, you are holding the button)
# hold for 3ms, means can travel for 4ms at 3mm / ms, so it is 12mm

# create list, track how many ways a distance can be broken per time
# loop from 1 to end of time, t, not inclusive. 
# track total of how many record distances can be travelled
# track the last processed dist, set at 0
# not holding the button or holding it the whole time means no distance is traveled
# calculate the distance travelled
# if it is greater than current record, increment total
# and update last processed dist
# elif it isn't greater, and the curr number is less than last processed, break (?)
def calculate_dist(times, dists):
    total_wins_by_dist = [0] * len(times)
    for i in range(len(times)):
        curr_total = 0
        last_processed = 0
        t = times[i]
        d = dists[i]
        for j in range(1, t):
            # calculate distance travelled
            curr_dist = (t - j) * j
            print(curr_dist)
            if curr_dist > d:
                curr_total += 1
                total_wins_by_dist[i] += 1
            elif curr_dist <= d and curr_dist < last_processed:
                break
            last_processed = curr_dist
    total = 1
    print(total_wins_by_dist)
    for wins in total_wins_by_dist:
        total *= wins
    return total             


# print(calculate_dist(test_times, test_dists)) # 288
# print(calculate_dist(times, dists)) # 449550

#---------------------------PART 2-----------------------------
# instead of a list of times, they actually combine to make one number
# so [7, 15, 30] becomes 71530
# new input data
# Time:        46     82     84     79
# Distance:   347   1522   1406   1471
file2 = open("/Users/megankorling/Developer/advent-of-code-23/day-6/data2.txt", "r")
lines2 = []
for line in file2:
    lines2.append(line.strip())
time_line2 = lines2[0].split(":")[1].split(" ")
times2 = ""
for c in time_line2:
    if c.isdigit():
        times2 += c
times2 = [int(times2)]
dists_line2 = lines2[1].split(":")[1].split(" ")
dists2 = ""
for c in dists_line2:
    if c.isdigit():
        dists2 += c
dists2 = [int(dists2)]
print(dists2)
# print(calculate_dist(times2, dists2)) # 28360140
# took a minute, maybe a little less to run
# there is probably some way to improve the speed, but the same algorithm does work
