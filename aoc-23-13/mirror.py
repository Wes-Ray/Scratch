import time


def mirror_calc(matrix : list) -> int:

    height = len(matrix)
    width = len(matrix[0])

    # check left/right

    # process first row to generate candidate set
    candidate_x_delims = set()
    dy = 0
    for delim in range(1, width - 1):
        # print("delim:", delim)
        row_reflects = True
        for dx in range(1, width//2+1):
            # print("\tdx:", dx)
            left_x = delim - dx
            right_x = delim + dx - 1
            if left_x >= 0 and right_x < width:
                # print(f"\t\t({left_x}){matrix[dy][left_x]} = ({right_x}){matrix[dy][right_x]}")
                if matrix[dy][left_x] != matrix[dy][right_x]:
                    row_reflects = False
        if row_reflects:
            # print("adding candidate: ", delim)
            candidate_x_delims.add(delim)

    print("candidates: ", candidate_x_delims)

    invalid_x_delimns = set()
    for dy in range(1, height): # skip first row
        # print(f"dy {dy} ---------------------")
        for delim in candidate_x_delims:
            # print("delim:", delim)
            row_reflects = True
            for dx in range(1, width//2+1):
                # print("\tdx:", dx)
                left_x = delim - dx
                right_x = delim + dx - 1
                if left_x >= 0 and right_x < width:
                    print(f"\t({left_x}){matrix[dy][left_x]} = ({right_x}){matrix[dy][right_x]}")
                    if matrix[dy][left_x] != matrix[dy][right_x]:
                        print(f"\t\tINVALID")
                        row_reflects = False
            if not row_reflects:
                print("CANDIDATE INVALID, REMOVING: ", delim)
                print("".join(matrix[dy]))
                invalid_x_delimns.add(delim)
        candidate_x_delims = candidate_x_delims - invalid_x_delimns
        # invalid_x_delimns = set()
    
    # print("final candidates: ", candidate_x_delims)
    # print("final invalid candidates: ", invalid_x_delimns)

    if len(candidate_x_delims) == 0:
        return 0
    elif len(candidate_x_delims) == 1:
        return candidate_x_delims.pop()
    else:
        raise Exception("more than one reflection found: ", candidate_x_delims)


def part1(file_name : str):
    patterns = []  # list of 2d lists, each of which represents a pattern
    with open(file_name, "r") as f:
        tmp_pattern = []
        for line in f.readlines():
            if line in ['\n', '\r\n']:
                patterns.append(tmp_pattern)
                tmp_pattern = []
            else:
                tmp_pattern.append(list(line[:-1]))
        patterns.append(tmp_pattern)

    total = 0
    idx = 0
    for p in patterns:
        print(f"idx {idx} " + "-"*30)
        idx += 1

        for r in p:
            print(''.join(r))

        col = mirror_calc(p)
        # print("RESULT COL: ", col)

        row = 0
        # if col == 0:
        #     # print("FLIPPING MATRIX")
        #     # print("-"*30)
        #     new_p = [[p[j][i] for j in range(len(p))] for i in range(len(p[0])-1,-1,-1)]
        #     row = mirror_calc(new_p)
        #     # print("row: ", row)
        
        print(f"\tcol={col}, row={row}")
        if row == 0 and col == 0:
            raise Exception("No reflection found")
        
        total += (100 * row) + col
        #####################
        break
        #####################
        
    print("FINAL TOTAL: ", total)


def main():
    print("main")
    start = time.time()
    part1("ezinput.txt")
    end = time.time()
    print(f"Elapsed Time: {end - start}")


if __name__ == "__main__":
    main()