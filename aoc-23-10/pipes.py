


class dir:
    RIGHT = (1, 0)
    LEFT = (-1, 0)
    UP = (0, -1)
    DOWN = (0, 1)
    DIAGONALS = [RIGHT, LEFT, UP, DOWN]


def fillable(current_pos : tuple, check_dir : tuple, matrix : list) -> bool:
    check_pos = (current_pos[0] + check_dir[0], current_pos[1] + check_dir[1])  # (x, y)
    # check if off matrix
    if check_pos[0] < 0 or check_pos[0] >= len(matrix[0]):
        # print("\toff side of matrix")
        return False
    if check_pos[1] < 0 or check_pos[1] >= len(matrix):
        # print("\toff top/bottom of matrix")
        return False
    
    check_symbol = matrix[check_pos[1]][check_pos[0]]

    if check_symbol == '.':
        return True

    return False


def connects(current_pos : tuple, check_dir : tuple, matrix : list) -> bool:

    # if current_pos == (0, 3) and check_dir == dir.DOWN:
    #     print("0,3")

    current_symbol = matrix[current_pos[1]][current_pos[0]]  # [y][x]
    check_pos = (current_pos[0] + check_dir[0], current_pos[1] + check_dir[1])  # (x, y)
    # print(f"\tcurrent symbol: {current_symbol}")
    # print(f"\tcheck_pos: {check_pos}")
    
    # check if off matrix
    if check_pos[0] < 0 or check_pos[0] >= len(matrix[0]):
        # print("\toff side of matrix")
        return False
    if check_pos[1] < 0 or check_pos[1] >= len(matrix):
        # print("\toff top/bottom of matrix")
        return False
    
    check_symbol = matrix[check_pos[1]][check_pos[0]]
    # print(f"\tcheck symbol: {check_symbol}")

    # check if check_symbol is 'S'
    # if check_symbol == 'S':
    #     return True

    match current_symbol:
        case 'S':
            match check_dir:
                case dir.RIGHT:
                    if check_symbol in ['-', 'J', '7', 'S']:
                        return True
                case dir.DOWN:
                    if check_symbol in ['|', 'L', 'J', 'S']:
                        return True
                case dir.UP:
                    if check_symbol in ['|', '7', 'F', 'S']:
                        return True
                case dir.LEFT:
                    if check_symbol in ['-', 'L', 'F', 'S']:
                        return True
        case '|':
            match check_dir:
                case dir.DOWN:
                    if check_symbol in ['|', 'L', 'J', 'S']:
                        return True
                case dir.UP:
                    if check_symbol in ['|', '7', 'F', 'S']:
                        return True
        case '-':
            match check_dir:
                case dir.RIGHT:
                    if check_symbol in ['-', 'J', '7', 'S']:
                        return True
                case dir.LEFT:
                    if check_symbol in ['-', 'L', 'F', 'S']:
                        return True
        case 'L':
            match check_dir:
                case dir.RIGHT:
                    if check_symbol in ['-', 'J', '7', 'S']:
                        return True
                case dir.UP:
                    if check_symbol in ['|', '7', 'F', 'S']:
                        return True
        case 'J':
            match check_dir:
                case dir.LEFT:
                    if check_symbol in ['-', 'L', 'F', 'S']:
                        return True
                case dir.UP:
                    if check_symbol in ['|', '7', 'F', 'S']:
                        return True
        case '7':
            match check_dir:
                case dir.LEFT:
                    if check_symbol in ['-', 'L', 'F', 'S']:
                        return True
                case dir.DOWN:
                    if check_symbol in ['|', 'L', 'J', 'S']:
                        return True
        case 'F':
            match check_dir:
                case dir.RIGHT:
                    if check_symbol in ['-', 'J', '7', 'S']:
                        return True
                case dir.DOWN:
                    if check_symbol in ['|', 'L', 'J', 'S']:
                        return True
        case other: # for '.'
            pass

    return False


def part1() -> None:
    starting_point = ()  # (x, y)

    matrix = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            matrix.append(lines[i][:-1])

            if 'S' in lines[i]:
                starting_point = (lines[i].find('S'), i)
    

    print(f"start: {starting_point}")
    # print(f"check pos RIGHT: {connects(starting_point, dir.RIGHT)}")
    # print(f"check pos DOWN: {connects(starting_point, dir.DOWN)}")
    # print(f"check pos LEFT: {connects(starting_point, dir.LEFT)}")
    # print(f"check pos UP: {connects(starting_point, dir.UP)}")

    second_pts = []
    for diag in dir.DIAGONALS:
        candidate_pos = (starting_point[0] + diag[0], starting_point[1] + diag[1])
        if connects(starting_point, diag, matrix):
            second_pts.append(candidate_pos)

    # routes = [[starting_point, second_pts[0]], [starting_point, second_pts[1]]]
    routes = [[starting_point, second_pts[0]]]

    print(f"init routes: {routes}")

    for route in routes:
        end_found = False
        while not end_found:
        # for i in range(5):
            current_pos = route[-1]
            prev_pos = route[-2]
            for diag in dir.DIAGONALS:
                candidate_pos = (current_pos[0] + diag[0], current_pos[1] + diag[1])
                if connects(current_pos, diag, matrix):
                    if prev_pos == candidate_pos:
                        # print(f"prev route found, skipping")
                        # print(f"\tcurrent: {current_pos} - candidate: {candidate_pos}")
                        pass
                    else:
                        # print(f"appending: {candidate_pos}")
                        if candidate_pos == starting_point:
                            print("END FOUND")
                            end_found = True
                        route.append(candidate_pos)
    

    print(f"LEN: {len(routes[0])//2}")


    clean_matrix = [['.' for i in range(len(matrix[0])+2)] for y in range(len(matrix))]

    for route in routes:
        for i in range(len(route)):
            pos = route[i]
            symbol = matrix[pos[1]][pos[0]]
            clean_matrix[pos[1]][pos[0]] = symbol

    with open("clean.txt", "w") as f:
        for row in clean_matrix:
            f.write("".join(row))
            f.write("\n")


def replace_dot(matrix : list, pos : tuple, direction : tuple, new_symbol : str):
    replace_pos = (pos[0] + direction[0], pos[1] + direction[1])
    symbol = matrix[replace_pos[1]][replace_pos[0]]
    # print()
    if symbol == '.':
        matrix[replace_pos[1]][replace_pos[0]] = new_symbol
        # print("check")


def expand_item(matrix : list, pos : tuple) -> None:
    symbol = matrix[pos[1]][pos[0]]
    # print(f"expand: {symbol}")
    match symbol:
        case 'S':
            pass
        case '|':
            replace_dot(matrix, pos, dir.UP, '|')
            replace_dot(matrix, pos, dir.DOWN, '|')
        case '-':
            replace_dot(matrix, pos, dir.LEFT, '-')
            replace_dot(matrix, pos, dir.RIGHT, '-')
        case 'L':
            replace_dot(matrix, pos, dir.UP, '|')
            replace_dot(matrix, pos, dir.RIGHT, '-')
        case 'J':
            replace_dot(matrix, pos, dir.UP, '|')
            replace_dot(matrix, pos, dir.LEFT, '-')
        case '7':
            replace_dot(matrix, pos, dir.LEFT, '-')
            replace_dot(matrix, pos, dir.DOWN, '|')
        case 'F':
            replace_dot(matrix, pos, dir.DOWN, '|')
            replace_dot(matrix, pos, dir.RIGHT, '-')


def maximize_matrix(matrix : list) -> list:
    new_matrix = [['.' for x in range(2*len(matrix[0]))] for y in range(2*len(matrix))]

    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            symbol = matrix[y][x]
            if symbol != '.':
                new_matrix[y*2][x*2] = symbol

    for y in range(len(new_matrix)):
        for x in range(len(new_matrix[0])):
            symbol = new_matrix[y][x]
            if symbol != '.':
                expand_item(new_matrix, (x, y))

    # print for debug    
    # for y in range(len(new_matrix)):
    #     for x in range(len(new_matrix[0])):
    #         symbol = new_matrix[y][x]
    #         print(new_matrix[y][x],end="")
    #     print()

    return new_matrix

def simple_remove(cur_list : list, idx : int) -> None:
    cur_list[idx] = cur_list[-1]
    cur_list.pop()


def part2() -> None:
    print("part2")

    matrix = []
    with open("clean.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            matrix.append([x for x in lines[i][:-1]])
    
    print("#### before matrix")
    for row in matrix:
        print("".join(row))

    print("maximizing")
    
    matrix = maximize_matrix(matrix)
    
    flood_queue = [(0, 0)]

    print("flooding")

    counter = 0
    while len(flood_queue) > 0:
        current_pt = flood_queue[0]
        # flood_queue.remove(flood_queue[0])
        simple_remove(flood_queue, 0)
        matrix[current_pt[1]][current_pt[0]] = ','  # flood with ,

        for move in dir.DIAGONALS:
            if fillable(current_pt, move, matrix):
                flood_queue.append((current_pt[0] + move[0], current_pt[1] + move[1]))
        
        counter += 1
        if counter % 10000 == 0:
            # for y in range(len(matrix)):
            #     for x in range(len(matrix[0])):
            #         item = matrix[y][x]
            #         print(item,end="")
            #     print()
            print(f"len queue: {len(flood_queue)} #############################")
            # print(f"\tflood queue: {flood_queue}")
            # if counter > 6:
            #     break


    print("#### flooded matrix")
    for row in matrix:
        print("".join(row))

    print("### counting")
    total_commas = 0
    total_dots = 0
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if x % 2 == 0 and y % 2 == 0:
                item = matrix[y][x]
                if item == ',':
                    total_commas += 1
                if item == '.':
                    total_dots += 1
        #         print(item,end="")
        # print()
    
    # 53 dots, 49 commas (4), 99 total for open gap example
    # 46 dots, 34 commas (12), 90 for closed gap example
    
    print(f"total_dots: {total_dots}")
    print(f"total_commas: {total_commas}")


def main():
    print("main")
    # part1()
    part2()


if __name__ == "__main__":
    main()