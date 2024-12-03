from re import findall
from functools import reduce
from operator import mul

def solver():
    with open("day3/input.txt") as f:
        content = f.read()
    multiplications = findall(r"mul\([0-9]{,3},[0-9]{,3}\)|don't\(\)|do\(\)", content)
    score = 0
    flag = True
    for m in multiplications:
        if m == "don't()":
            flag = False
            continue
        if m == "do()":
            flag = True
            continue
        if flag:
            score += reduce(
                mul, [int(num) for num in findall(r"[0-9]{,3}", m) if num != ""]
            )

    print(score)
