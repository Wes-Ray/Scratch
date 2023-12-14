from numpy import array
import time

class dir:
    # (y, x)
    EAST = (0, 1)
    WEST = (0, -1)
    NORTH = (-1, 0)
    SOUTH = (1, 0)
    CARDINALS = [NORTH, WEST, SOUTH, EAST]


def tilt(matrix : array, tilt_dir : tuple) -> None:
    print("tilt")

    width = matrix[0].size  # width == height

    # for i in range(width):  # repeats
    #     for y in range(width-1, -1, -1):
    #         # print(f"y: {y}")
    #         for x in range(width):
    #             # print(f"\tx: {x} {matrix[y][x]}")
    #             if matrix[y][x] == 'O':
    #                 if y-1 == -1:
    #                     continue
    #                 if matrix[y-1][x] == '.':
    #                     matrix[y-1][x] = 'O'
    #                     matrix[y][x] = '.'

    # for y in range(width)

    

def part1(input : str):
    rows = []
    with open(input, "r") as f:
        lines = f.readlines()
        for l in lines:
            rows.append(list(l[:-1]))
    
    matrix = array(rows)  # matrix[y][x]
    # print(f"matrix: \n{matrix}")
    
    tilt(matrix, dir.NORTH)
    
    print("-"*20)
    mult = matrix[0].size
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
    part1("ezinput.txt")
    end = time.time()
    print(f"Elapsed Time: {end - start}")


if __name__ == "__main__":
    main()