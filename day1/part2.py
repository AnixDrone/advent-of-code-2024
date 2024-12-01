def solver():
    with open("day1/input.txt") as f:
        content = f.read()
    numbers = [
        number_line for number_line in content.split("\n") if number_line != "None"
    ]
    col_1 = [int(number.split("   ")[0]) for number in numbers]
    col_2 = [int(number.split("   ")[1]) for number in numbers]
    col_freq = {number: sum([1 for num in col_2 if num == number]) for number in col_2}

    print(sum([col_freq[c1] * c1 for c1 in col_1 if c1 in col_freq]))
