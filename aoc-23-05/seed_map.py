
def check_map(check_val : int, seed_map : list) -> int:
    """
    seed_map = [
        [50, 98, 2],  # [dst, src, range] -> [50-51, 98-99, 2]
        [52, 50, 48]
    ]
    # all values not in seed map just return the original value
    """
    ret_val = check_val

    for submap in seed_map:
        # print(f"\t\t{submap}")
        src = submap[1]
        dst = submap[0]
        map_range = submap[2]
        if src <= check_val < src + map_range:
            ret_val = dst + check_val - src

    return ret_val


def main():
    seeds = []  # list of seed int values
    seed_maps = []  # list of lists of maps, each sub-list is a map
    with open("input.txt", "r") as file:
        lines = file.readlines()
        seeds = list(map(int, lines[0].split(":")[1].split()))

        tmp_map = []
        for line in lines[2:]:
            if line == "\n":  # won't get last line, either add a new line to end of input or add special case
                seed_maps.append(tmp_map)
                tmp_map = []
                continue
            ls = line.split()
            if ls[0].isnumeric():
                tmp_map.append(list(map(int,ls)))
        seed_maps.append(tmp_map)

    """
    seeds: [79, 14, 55, 13]
    maps:
        [[50, 98, 2], [52, 50, 48]]
        [[0, 15, 37], [37, 52, 2], [39, 0, 15]]
        ...
    """

    # print(f"seeds: {seeds}")
    # print(f"maps:")
    min_dest = 10**100
    for seed in seeds:
        # print(f"checking seed: {seed}")
        dest = seed
        for seed_map in seed_maps:
            dest = check_map(dest, seed_map)
            # print(f"\t{seed} -> {seed_map} -> {dest}")
        min_dest = min(dest, min_dest)
    
    print(f"FINAL MIN DEST: {min_dest}")


if __name__ == "__main__":
    main()