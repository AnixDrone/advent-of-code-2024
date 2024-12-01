def solver():
    with open("day1/input.txt") as f:
        content = f.read()
    numbers = [
        number_line for number_line in content.split("\n") if number_line != "None"
    ]
    col_1 = [int(number.split("   ")[0]) for number in numbers]
    col_2 = [int(number.split("   ")[1]) for number in numbers]
    col_1.sort()
    col_2.sort()
    score = 0
    for c1, c2 in zip(col_1, col_2):
        score += abs(c1 - c2)
    print(score)
