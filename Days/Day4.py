def part1(_input):
    result = 0
    for line in _input:
        a, b, c, d = getTuple([pairs.split("-") for pairs in line.split(",")])
        if a <= c and b >= d or c <= a and d >= b:
            result += 1

    return result


def part2(_input):
    result = 0
    for line in _input:
        a, b, c, d = getTuple([pairs.split("-") for pairs in line.split(",")])
        if a <= c <= b or c <= a <= d:
            result += 1

    return result


def getTuple(pairs: list):
    return int(pairs[0][0]), int(pairs[0][1]), int(pairs[1][0]), int(pairs[1][1])
