

def calc_distance(from_pos : tuple, to_pos : tuple, space : list) -> int:
    # pos (y, x), space[y][x]

    visited = []
    for x in range(from_pos[1]+1, to_pos[1]+1):
        y = from_pos[0]
        symbol = space[y][x]
        # print(f"({y}, {x}):{symbol}", end="->")
        visited.append(symbol)
    for y in range(from_pos[0]+1, to_pos[0]+1):
        x = to_pos[1]
        symbol = space[y][x]
        # print(f"({y}, {x}):{symbol}", end="->")
        visited.append(symbol)
    
    # print(f"\nvisited: {visited}")
    dist = 0
    for v in visited:
        if v == '.' or v == '#':
            dist += 1
        if v == ',':
            # dist += 2
            dist += 1000000

    return dist


def main():
    print("main")
    space = []
    with open("input.txt", "r") as f:
        lines = f.readlines()
        for i in range(len(lines)):
            space.append([x for x in lines[i][:-1]])
    
    galaxies = []
    for y in range(len(space)):
        for x in range(len(space[0])):
            if space[y][x] == '#':
                galaxies.append((y, x))
    

    # add 'empty space' indicators with , replacing .
    for y in range(len(space)):
        if space[y].count('#') == 0:
            space[y] = list(","*len(space[0]))
    
    for x in range(len(space[0])):
        tmp_col = []
        for y in range(len(space)):
            tmp_col.append(space[y][x])
        if tmp_col.count('#') == 0:
            for y in range(len(space)):
                space[y][x] = ','
    
    # for row in space:
    #     print("".join(row))

    count = 0
    total_dist = 0
    for g1 in galaxies:
        for g2 in galaxies:
            dist = calc_distance(g1, g2, space)
            # print(f"{galaxies.index(g1)+1} to {galaxies.index(g2)+1}: {dist}")
            count += 1
            total_dist += dist
    
    print(f"comparisons: {count}")
    print(f"total dist: {total_dist}")
        


if __name__ == "__main__":
    main()