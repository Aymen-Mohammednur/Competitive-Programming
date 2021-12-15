# https://www.hackerrank.com/challenges/counting-valleys/problem

def countingValleys(steps, path):
    # Write your code here
    level = 0
    valley = 0
    for i in range(steps):
        print(valley)
        if (path[i] == "U"):
            level += 1
        if (path[i] == "D"):
            level -= 1
        if (i != 0 and level == 0 and path[i] == "U"):
            valley += 1
    return valley


steps = 6
path = "DUUDDU"
print(countingValleys(steps, path))
# print(len("UUDD"))
