from numpy import array
from functools import cache
import time

class dir:
    # (y, x)
    EAST = (0, 1)
    WEST = (0, -1)
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    CARDINALS = [NORTH, WEST, SOUTH, EAST]


def tilt(matrix : array, tilt_dir : tuple) -> None:
    # print(f"tilting {tilt_dir}")

    width = matrix[0].size  # width == height

    match tilt_dir:
        case dir.SOUTH:
            for x in range(width):
                floor = 0  # y value of floor
                for y in range(width-1, -1, -1):
                    if matrix[y][x] == '#':
                        floor = y
                    elif matrix[y][x] == 'O':
                        matrix[y][x] = '.'
                        floor -= 1  # depends on direction
                        matrix[floor][x] = 'O'
        case dir.NORTH:
            for x in range(width):
                floor = 0  # y value of floor
                for y in range(0, width):
                    if matrix[y][x] == '#':
                        floor = y
                    elif matrix[y][x] == 'O':
                        matrix[y][x] = '.'
                        floor += 1  # depends on direction
                        matrix[floor][x] = 'O'
        case dir.EAST:
            for y in range(width):
                floor = 0  # x value of floor
                for x in range(width-1, -1, -1):
                    if matrix[y][x] == '#':
                        floor = x
                    elif matrix[y][x] == 'O':
                        matrix[y][x] = '.'
                        floor -= 1  # depends on direction
                        matrix[y][floor] = 'O'
        case dir.WEST:
            for y in range(width):
                floor = 0  # x value of floor
                for x in range(0, width):
                    if matrix[y][x] == '#':
                        floor = x
                    elif matrix[y][x] == 'O':
                        matrix[y][x] = '.'
                        floor += 1  # depends on direction
                        matrix[y][floor] = 'O'

    # # print
    # print("-"*20)
    # for r in matrix:
    #     print("".join(r))
    # print("-"*20)


def part2(input : str):
    rows = []
    with open(input, "r") as f:
        lines = f.readlines()
        for l in lines:
            rows.append(['#'] + list(l[:-1]) + ['#'])
    boundary = list('#' * len(rows[0]))
    matrix = array([boundary] + rows + [boundary])  # matrix[y][x]

    tilt_count = 1000
    print(f"tilting {tilt_count} times")
    for i in range(tilt_count):
        for card_dir in dir.CARDINALS:
            tilt(matrix, card_dir)
    
    print("~"*40)
    mult = matrix[0].size - 1
    total = 0
    for r in matrix:
        for v in r:
            if v == 'O':
                total += mult
        print("".join(r), mult)
        mult -= 1
    
    print(f"FINAL TOTAL: {total}")


def main():
    print("main")
    start = time.time()
    part2("input.txt")
    end = time.time()
    print(f"Elapsed Time: {end - start}")


if __name__ == "__main__":
    main()