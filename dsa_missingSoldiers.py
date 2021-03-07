# Author: Brenda

barriers = int(input())
all_b = []
# get the coordinates from the user
for i in range(barriers):
    x, y, d = map(int, input().strip().split())
    all_b.append((x, x + d))

all_b.sort() # sort the barriers
ants_blocked = point_m = 0  # initialize blocked ants counter

# block ants in the coordinates
for b in all_b:
    if b[0] >= point_m:
        point_m = b[0]
        if point_m < b[1]:
            ants_blocked += (b[1] - point_m) + 1
            point_m = b[1] + 1
    elif point_m <= b[1]:
        ants_blocked += (b[1] - point_m) + 1
        point_m = b[1] + 1

print(ants_blocked)