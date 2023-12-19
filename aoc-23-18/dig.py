import time


class Vector2:
    def __init__(self, y : int, x : int) -> None:
        self.y = y
        self.x = x
    
    def __str__(self) -> str:
        return f"(y={self.y}, x={self.x})"
    
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __hash__(self) -> int:
        return (1000 * self.y) + self.x
    
    def __add__(self, __value: object):
        return Vector2(self.y + __value.y, self.x + __value.x)
    
    def __sub__(self, __value: object):
        return Vector2(self.y - __value.y, self.x - __value.x)

    def scalar_multiply(self, scalar : int):
        self.x *= scalar
        self.y *= scalar
        return self


class Instr:
    def __init__(self, direction_letter : str, distance : int, color : str) -> None:
        self.distance = distance
        self.color = color

        match direction_letter:
            case 'R':
                self.direction = Vector2(0, 1)
            case 'L':
                self.direction = Vector2(0, -1)
            case 'D':
                self.direction = Vector2(1, 0)
            case 'U':
                self.direction = Vector2(-1, 0)
            case _:
                raise Exception("Invalid direction provided.")
    
    def __str__(self) -> str:
        return f"[dir:{self.direction}, dist:{self.distance}, color:{self.color}]"


def fast_remove(cur_list : list, idx : int) -> None:
    # doesn't maintain order
    cur_list[idx] = cur_list[-1]
    cur_list.pop()


def flood_fill(start : Vector2, grid: list):
    flood_queue = [start]
    while len(flood_queue) > 0:
        current_vec = flood_queue[0]
        fast_remove(flood_queue, 0)
        grid[current_vec.y][current_vec.x] = ','
        
        for move in (Vector2(0, 1), Vector2(0, -1), Vector2(1, 0), Vector2(-1, 0)):
            check_vec = current_vec + move
            if grid[check_vec.y][check_vec.x] == '#':
                continue
            if grid[check_vec.y][check_vec.x] == ',':
                continue
            flood_queue.append(check_vec)

        # print("---- FLOOD ----")
        # for f in flood_queue:
        #     print(f, end=", ")
        # print()
        # for row in grid:
        #     print("".join(row))
        
        # if len(input()) > 0:
        #     break


def part2(file_name : str) -> None:
    instructions = []
    with open(file_name, "r") as f:
        for l in f.readlines():
            tmp = l.split()

            cstr = tmp[2]
            cdist = int(cstr[2:-2], 16)
            cdir_num = int(cstr[-2:-1])

            match cdir_num:
                case 0:
                    cdir = 'R'
                case 1:
                    cdir = 'D'
                case 2:
                    cdir = 'L'
                case 3:
                    cdir = 'U'

            instructions.append(Instr(cdir, cdist, ""))
    
    vecs = [Vector2(1,1)]
    border_length = 0
    for inst in instructions:
        border_length += inst.distance

        tmp_vec = vecs[-1] + (inst.direction.scalar_multiply(inst.distance))
        vecs.append(tmp_vec)
        # print(tmp_vec)
        # input()
    
    print("%"*40)
    
    # expects 16.5 for below vecs of polygon
    # vecs = [Vector2(1,6), Vector2(3,1), Vector2(7,2), Vector2(4,4), Vector2(8,5), Vector2(1,6)]
    # apply shoelace algo to vecs
    summation = 0
    for i in range(len(vecs)-1):
        
        determinant = (vecs[i].x * vecs[i+1].y) - (vecs[i].y * vecs[i+1].x)
        # print(f"vec1 {vecs[i]} to vec2 {vecs[i+1]} -> {determinant}")
        # input()
        summation += determinant
    
    print(f"summation: {summation} / 2 -> {summation/2} :: border len: {border_length}")

    area = (summation/2) + (border_length/2) + 1

    print(f"AREA: {area}")


def part1(file_name : str) -> None:
    instructions = []
    with open(file_name, "r") as f:
        for l in f.readlines():
            tmp = l.split()
            instructions.append(Instr(tmp[0], int(tmp[1]), tmp[2]))
    
    vecs = [Vector2(0,0)]
    min_x = 0
    min_y = 0
    max_x = 0
    max_y = 0
    for inst in instructions:
        # print("-"*40)
        for steps in range(inst.distance):
            tmp_vec = vecs[-1] + inst.direction
            # print(tmp_vec)
            vecs.append(tmp_vec)
            max_x = max(max_x, tmp_vec.x)
            max_y = max(max_y, tmp_vec.y)
            min_x = min(min_x, tmp_vec.x)
            min_y = min(min_y, tmp_vec.y)
        # input()
    
    # build grid
    grid = []
    for y in range(min_y, max_y+1):
        tmp_row = []
        for x in range(min_x, max_x+1):
            tmp_vec = Vector2(y,x)
            if tmp_vec in vecs:
                tmp_row.append("#")
            else:
                tmp_row.append(".")
        grid.append(tmp_row)
        tmp_row = []
    
    for row in grid:
        print("".join(row))
    
    flood_fill(Vector2(0,0), grid)

    print("*"*40)
    for row in grid:
        print("".join(row))
    
    count_comma = 0
    count_pound = 0
    count_period = 0
    for row in grid:
        count_comma += row.count(",")
        count_pound += row.count("#")
        count_period += row.count(".")
    
    print(f"FINAL COUNT . + #: {count_pound + count_period}")
    print(f"FINAL COUNT , + #: {count_pound + count_comma}")


def main():
    t1 = time.time()
    # part1("input.txt")
    part2("input.txt")
    t2 = time.time()

    print("elapsed time :", t2 - t1)


if __name__ == "__main__": 
    main()