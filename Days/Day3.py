def part1(_input):
    result = 0
    for line in _input:
        x = line[:len(line)//2]
        y = line[len(line)//2:]
        char = list(set(x).intersection(y))[0]
        if char.isupper():
            result += ord(char) - 38
        else:
            result += ord(char) - 96

    return result


def part2(_input):
    result = 0
    lines = iter(_input)
    for _ in range(len(_input) // 3):
        char = list(set(lines.__next__()).intersection(set(lines.__next__()).intersection(lines.__next__())))[0]
        if char.isupper():
            result += ord(char) - 38
        else:
            result += ord(char) - 96

    return result
