import time

MAX_COST = 99

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


class City:
    def __init__(self, heat : int, cost : int, direction : Vector2, steps : int):
        self.heat = heat
        self.cost = cost
        self.direction = direction
        self.steps = steps
    
    def __str__(self) -> str:
        return f"[heat: {self.heat}, cost: {self.cost}, dir: {self.direction}, steps: {self.steps}]"


def find_closest_neighbor(current_city : Vector2, knowns : list, city_map : dict) -> Vector2:
    # print("*"*30)
    # print(f"current: {current_city}")
    neighbors = [
                current_city + Vector2(-1,0),
                current_city + Vector2(1,0),
                current_city + Vector2(0,-1),
                current_city + Vector2(0,1),
                 ]
    potentials = []
    # print("neighbors")
    for n in neighbors:
        # print("\t",n)
        # if neighbor in knowns, skip
        if n in knowns:
            continue
        if n not in city_map:
            continue
        # linear_count exceeding 3 (>>> is max), skip linear neighbor
        if city_map[current_city].steps > 2:
            print("DEBUG 1")
            if n == current_city + city_map[current_city].direction:
                print("DEBUG 2 LINEAR COUNT EXCEEDING")
                continue

        potentials.append(n)
    
    # print("potentials")
    min_p_val = MAX_COST
    min_p = None
    for p in potentials:
        # print("\t", p, city_map[p])
        if city_map[p].heat < min_p_val:
            min_p_val = city_map[p].heat
            min_p = p
        # update overall cost for each adjacent city
        city_map[p].cost = city_map[current_city].cost + city_map[p].heat
        city_map[min_p].direction = min_p - current_city
        # print(f"DEBUG: {current_city} -> dir: {city_map[min_p].direction}")
        # if turning, reset linear_count to 0
        if p == current_city + city_map[current_city].direction:
            city_map[min_p].steps += 1
        else:
            city_map[min_p].steps = 1
    
    # print("min_p: ", min_p)
    if min_p is None:  # find next lowest and explore, will prob have to save dir/steps to dict as well
        print("DEBUG min_p is NONE", MAX_COST)
        for np in city_map:
            if np in knowns:
                continue
            if city_map[np].cost < min_p_val:
                min_p_val = city_map[np].cost
                min_p = np
            # print("\t", np)
        print(f"NEW min_p: {min_p}")

    return min_p


def part1(file_name : str) -> None:
    # enumerate cities, add to set
    city_map = {}
    with open(file_name, "r") as f:
        rl = f.readlines()
        for y in range(len(rl)):
            for x in range(len(rl[0])-1): # strip new line
                city_map[Vector2(y,x)] = City(int(rl[y][x]), MAX_COST, Vector2(0,0), 1)
    
    # for c in city_map:
    #     print(f"{c} : {city_map[c]}")
    
    knowns = [Vector2(0,0)]  # known city vectors (don't attach additional info)
    city_map[Vector2(0,0)].cost = 0
    # city_map[Vector2(0,0)].steps = 4
    # city_map[Vector2(0,0)].direction = Vector2(0, 1)

    while len(knowns) < len(city_map):
        next_city = find_closest_neighbor(knowns[-1], knowns, city_map)
        
        # print(next_city)
        knowns.append(next_city)
        # print("="*30)
            

        # for k in knowns:
        #     print(k)
        # with linear restriction, expecting 12 instead of 10 for 5,5
        print("="*40)
        # for v in city_map:
        #     print(v, city_map[v])

        row = 0
        for v in city_map:
            # print(v, city_map[v])
            if v.y > row:
                print()
                row += 1
            print(f"{city_map[v].cost}-{city_map[v].steps}", end="\t")
        print()
        
        if len(input()) > 0:
            break
    
    print("#"*40)
    print("#"*40)
    row = 0
    for v in city_map:
        # print(v, city_map[v])
        if v.y > row:
            print()
            row += 1
        print(f"{city_map[v].cost}-{city_map[v].steps}", end="\t\t")
    print()


def main():
    t1 = time.time()
    part1("ezinput.txt")
    t2 = time.time()

    print("elapsed time :", t2 - t1)


if __name__ == "__main__":
    main()