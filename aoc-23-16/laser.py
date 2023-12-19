import time


class Flag:
    CONTINUE = 0
    SPLIT = 1
    DELETE = -1


class Dir:
    def __init__(self, dir_name : str) -> None:
        self.dir_name = dir_name
        if dir_name == "RIGHT":
            self.y = 0
            self.x = 1
        elif dir_name == "LEFT":
            self.y = 0
            self.x = -1
        elif dir_name == "UP":
            self.y = -1
            self.x = 0
        elif dir_name == "DOWN":
            self.y = 1
            self.x = 0
        else:
            raise Exception("Invalid Direction")
    
    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __str__(self) -> str:
        return self.dir_name


class Vector2:
    def __init__(self, y : int, x : int) -> None:
        self.y = y
        self.x = x

    def __eq__(self, __value: object) -> bool:
        return self.x == __value.x and self.y == __value.y
    
    def __str__(self) -> str:
        return f"({self.y}, {self.x})"


class Light:
    def __init__(self, pos : Vector2, dir : Dir) -> None:
        self.pos = pos
        self.dir = dir
    
    def __eq__(self, __value: object) -> bool:
        return self.pos == __value.pos and self.dir == __value.dir

    def __str__(self) -> str:
        return f"[{self.pos} -> {self.dir}]"


def simulate(grid : list, particle : Light, save_grid : list) -> (Flag, Light):
    # return a new Light if a new one is made
    # print(f"sim: {particle}")

    particle.pos.x += particle.dir.x
    particle.pos.y += particle.dir.y

    current_char = grid[particle.pos.y][particle.pos.x]
    # save grid
    if current_char not in ['#', 'o']:
        # match particle.dir:
        if particle.dir == Dir("LEFT"):
            save_dir = "<"
        elif particle.dir == Dir("RIGHT"):
            save_dir = ">"
        elif particle.dir == Dir("DOWN"):
            save_dir = "v"
        elif particle.dir == Dir("UP"):
            save_dir = "^"
        
        if save_dir == save_grid[particle.pos.y][particle.pos.x]:
            # print("DUPLICATE PATH FOLLOW, DELETING")
            return Flag.DELETE, None

        save_grid[particle.pos.y][particle.pos.x] = save_dir

    # logic
    if current_char == '#':
        return Flag.DELETE, None
    elif current_char == '.':
        grid[particle.pos.y][particle.pos.x] = 'o'
        return Flag.CONTINUE, None
    elif current_char == 'o':
        return Flag.CONTINUE, None
    elif current_char == '|':
        # print(f"\t{current_char} - {particle} - {particle.pos} - {particle.dir}")
        if particle.dir == Dir("RIGHT") or particle.dir == Dir("LEFT"):
            particle.dir = Dir("UP")
            new_particle = Light(Vector2(particle.pos.y, particle.pos.x), Dir("DOWN"))
            return Flag.SPLIT, new_particle
        else:
            return Flag.CONTINUE, None
    elif current_char == '-':
        if particle.dir == Dir("DOWN") or particle.dir == Dir("UP"):
            particle.dir = Dir("RIGHT")
            new_particle = Light(Vector2(particle.pos.y, particle.pos.x), Dir("LEFT"))
            return Flag.SPLIT, new_particle
        else:
            return Flag.CONTINUE, None
    elif current_char == '\\':
        if particle.dir == Dir("RIGHT"):
            particle.dir = Dir("DOWN")
        elif particle.dir == Dir("UP"):
            particle.dir = Dir("LEFT")
        elif particle.dir == Dir("LEFT"):
            particle.dir = Dir("UP")
        elif particle.dir == Dir("DOWN"):
            particle.dir = Dir("RIGHT")
        return Flag.CONTINUE, None
    elif current_char == '/':
        if particle.dir == Dir("RIGHT"):
            particle.dir = Dir("UP")
        elif particle.dir == Dir("UP"):
            particle.dir = Dir("RIGHT")
        elif particle.dir == Dir("LEFT"):
            particle.dir = Dir("DOWN")
        elif particle.dir == Dir("DOWN"):
            particle.dir = Dir("LEFT")
        return Flag.CONTINUE, None
    else:
        return Flag.CONTINUE, None


def part1(file_name : str, start_particle : Light = Light(Vector2(1,0), Dir("RIGHT"))) -> int:
    grid = []
    with open(file_name, "r") as f:
        for l in f.readlines():
            grid.append(list("#" + l[:-1] + "#"))
    grid.insert(0, list("#"*len(grid[0])))
    grid.append(list("#"*len(grid[0])))

    light_particles = [start_particle]

    grid_cpy = [row.copy() for row in grid]

    for x in range(1000):
        if len(light_particles) == 0:
            # print(f"NO MORE LIGHT PARTICLES TO SIMULATE AFTER {x+1} STEPS")
            break

        to_remove = []
        to_append = []
        for lp in light_particles:
            f, new_light = simulate(grid, lp, grid_cpy)
            if f == Flag.CONTINUE:
                continue
            elif f == Flag.DELETE:
                to_remove.append(lp)
            elif f == Flag.SPLIT:
                to_append.append(new_light)
        
        for lp in to_remove:
            light_particles.remove(lp)
        for lp in to_append:
            if lp not in light_particles:
                light_particles.append(lp)
        # draw  
        print("-"*30)
        for row in grid:
            print("".join(row))
        input()

    print(f"simulated in {x+1} steps")
    
    # draw
    # print("-"*30)
    # for row in grid:
    #     print("".join(row))
    
    
    # print("*"*30)
    # print("GRID COPY")
    count = 0
    for row in grid_cpy:
        count += row.count('>')
        count += row.count('<')
        count += row.count('v')
        count += row.count('^')
        # print("".join(row))
    # print("FINAL COUNT: ", count)

    return count


def part2(file_name : str):
    GRID_WIDTH = 110  # 10 for ez, 110 for input
    all_start_lights = []
    # from top
    for i in range(1, GRID_WIDTH+1):
        all_start_lights.append(Light(Vector2(0, i), Dir("DOWN")))
    # from bottom
    for i in range(1, GRID_WIDTH+1):
        all_start_lights.append(Light(Vector2(GRID_WIDTH+1, i), Dir("UP")))
    # from left
    for i in range(1, GRID_WIDTH+1):
        all_start_lights.append(Light(Vector2(i, 0), Dir("RIGHT")))
    # fromt right
    for i in range(1, GRID_WIDTH+1):
        all_start_lights.append(Light(Vector2(i, GRID_WIDTH+1), Dir("LEFT")))

    max_result = 0
    for sl in all_start_lights:
        max_result = max(part1(file_name, sl), max_result)
    print("result:", max_result)


def main():
    t1 = time.time()
    print(part1("ezinput.txt"))
    # part2("input.txt")
    t2 = time.time()

    print("elapsed time: ", t2 - t1)

if __name__ == "__main__":
    main()
