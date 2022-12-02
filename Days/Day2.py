first = ["A", "B", "C"]
second = ["X", "Y", "Z"]


def part1(_input):
    points = 0
    for line in _input:
        x, y = line.split(" ")
        # draw
        if first.index(x) == second.index(y):
            points += 3
        # win
        elif (first.index(x) + 1) % 3 == second.index(y):
            points += 6

        points += second.index(y) + 1

    return points


def part2(_input):
    points = 0
    for line in _input:
        x, y = line.split(" ")
        # lose
        if y == "X":
            points += (first.index(x) - 1) % 3 + 1
        # draw
        elif y == "Y":
            points += 3 + first.index(x) + 1
        # win
        else:
            points += 6 + (first.index(x) + 1) % 3 + 1

    return points
