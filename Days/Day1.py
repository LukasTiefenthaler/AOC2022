def part1(_input):
    most_calories = 0
    current_calories = 0
    for line in _input:
        if line:
            current_calories += int(line)
        else:
            most_calories = max(current_calories, most_calories)
            current_calories = 0

    most_calories = max(current_calories, most_calories)

    return most_calories


def part2(_input):
    most_calories = [0, 0, 0]
    current_calories = 0
    for value in _input:
        if value:
            current_calories += int(value)
        else:
            most_calories.sort()
            most_calories[0] = max(current_calories, most_calories[0])
            current_calories = 0

    most_calories.sort()
    most_calories[0] = max(current_calories, most_calories[0])

    return most_calories[0] + most_calories[1] + most_calories[2]
