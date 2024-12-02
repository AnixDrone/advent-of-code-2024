from day1.part1 import solver as day1_part1_solver
from day1.part2 import solver as day1_part2_solver
from day2.part1 import solver as day2_part1_solver
from day2.part2 import solver as day2_part2_solver
import argparse


def parse_args():
    parser = argparse.ArgumentParser(description="Advent of Code 2024")
    parser.add_argument("day", type=int, help="Which day to run")
    parser.add_argument("part", type=int, help="Which part to run")
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    if args.day == 1:
        if args.part == 1:
            print(day1_part1_solver())
        if args.part == 2:
            print(day1_part2_solver())
    if args.day == 2:
        if args.part == 1:
            print(day2_part1_solver())
        if args.part == 2:
            print(day2_part2_solver())
    else:
        print("Invalid part number")
