
def gen_seed_rule(seed_map : list) -> tuple:
    # return (min, max, offset)
    src = seed_map[0]
    dst = seed_map[1]
    seed_range = seed_map[2]
    return (src, src + seed_range, dst - src)


def process_rules(val : int, seed_map : list) -> int:
    for seed_rule in seed_map:
        if seed_rule[0] <= val < seed_rule[1]:
            return val + seed_rule[2]
    return val


def main():
    seed_maps = []
    seeds = [] 

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
                tmp_map.append(gen_seed_rule(list(map(int,ls))))
        seed_maps.append(tmp_map)
    seed_maps.reverse()

    print("gen'd maps")

    new_seeds = []  # [(seed_start, seed_rand), (ss1, sr2), ...]
    for i in range(0, len(seeds), 2):
        new_seeds.append(((seeds[i]), seeds[i] + seeds[i+1]))

    seeds = new_seeds

    print("re-gen'd seeds")

    for final_loc in range(10**1000):
        # print(og_seed)
        tmp_seed = final_loc
        for seed_map in seed_maps:
            tmp_seed = process_rules(tmp_seed, seed_map)
        if seed_check(tmp_seed, seeds):
            print("original seed found")
            break
    print(f"final location: {final_loc}, starting at original seed {tmp_seed}")


def seed_check(seed : int, seeds : list) -> bool:
    # [(79, 93), (55, 68)]
    for og_seed_map in seeds:
        if og_seed_map[0] <= seed < og_seed_map[1]:
            return True
    
    return False


if __name__ == "__main__":
    main()