
SYMBOLS = ['#', '$', '%', '&', '*', '+', '-', '/', '=', '@']


def main():

    schematic_matrix = []  # a list of strings
    number_locs = [] # list of lists of tuple locs, each sub list is a single number
    gear_locs = [] # list of tuple locs for gears (no sub-lists)

    with open("input.txt", "r") as file:
        for line in file.readlines():
            schematic_matrix.append(line[:-1])

    for y in range(len(schematic_matrix)):
        tmp_locs = []
        for x in range(len(schematic_matrix[y])):
            print(f"({x},{y})={schematic_matrix[y][x]}",end=" ")
            if schematic_matrix[y][x].isnumeric():
                tmp_locs.append((x, y))
            elif len(tmp_locs) > 0:
                number_locs.append(tmp_locs)
                tmp_locs = []
            # check for gears
            if schematic_matrix[y][x] == "*":
                gear_locs.append((x, y))
        if len(tmp_locs) > 0:  # add when tmp_locs are at the end of a line
            number_locs.append(tmp_locs)
        print()

    print("########")
    sum = 0
    for num_list in number_locs:
        val_str = ""
        is_valid = False
        for loc in num_list:
            y = loc[1]
            x = loc[0]
            val_str += schematic_matrix[y][x]

            if neighboring_symbol_exists(x, y, schematic_matrix):
                is_valid = True
        if is_valid:
            sum += int(val_str)

        print(f"{is_valid} = above value {val_str}")
    print("FINAL SUM: ", sum)

    print("\n\n---------------Finding Gear Ratios-------------\n\n")

    gear_sum = 0

    for gear in gear_locs:
        gear_y = gear[1]
        gear_x = gear[0]
        gear_ratio = gear_ratio_finder(gear_x, gear_y, number_locs, schematic_matrix)
        gear_sum += gear_ratio
    
    print("FINAL GEAR RATIO: ", gear_sum)


def gear_ratio_finder(x : int, y : int, num_list : list, matrix : list) -> int:
    print("num_list: ", num_list)

    adjacent_coords = [(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]
    check_cords = []
    for check in adjacent_coords:
        check_x = x + check[0]
        check_y = y + check[1]
        check_cords.append((check_x, check_y))

    adjacent_nums = []  # add adjacent nums as found, check for location duplicates before adding
    gear_ratio = 0  # multiply values to get gear ratio
    for num_locs in num_list:
        is_in_list = False
        for check_loc in check_cords:
            if check_loc in num_locs:
                is_in_list = True
        if is_in_list:
            adjacent_nums.append(num_locs)
    
    print("adjacent nums: ", adjacent_nums)
    if len(adjacent_nums) == 2:
        gear_ratio = 1
        for num_lst in adjacent_nums:
            print("num_lst: ", num_lst)
            num = ""
            for loc in num_lst:
                loc_y = loc[1]
                loc_x = loc[0]
                num += matrix[loc_y][loc_x]
            gear_ratio *= int(num)

    return gear_ratio


def neighboring_symbol_exists(x : int, y : int, matrix : list) -> bool:
    ret = False

    # gen neighboring coords
    check_coords = [(-1,1), (0,1), (1,1), (1,0), (1,-1), (0,-1), (-1,-1), (-1,0)]
    for check in check_coords:
        check_x = x + check[0]
        check_y = y + check[1]
        # assumes each line in matrix is the same len
        if (check_x >= 0 and check_y >= 0) and (check_y < len(matrix)) and (check_x < len(matrix[0])):
            print(f"({check_x},{check_y})", end="=")
            check_val = matrix[check_y][check_x]
            if check_val in SYMBOLS:
                ret = True
            print(check_val, end=" ")
    print(f" final: {ret}")
    return ret
    

if __name__ == "__main__":
    main()