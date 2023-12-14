from functools import cache


@cache
def count_combos(rec : tuple, grps : tuple, started : bool = False) -> int:

    # print(f"\t{''.join(rec)} {grps} {started}")
    
    if len(grps) == 0:
        if rec.count("#") == 0:
            # print("VALID COMBO")
            return 1
        else:
            return 0
    
    if rec.count('#') == 0 and rec.count('?') == 0:
        return 0
    

    match rec[0]:
        case '.':
            if started:
                return 0
            return count_combos(rec[1:], grps)
        
        case '#':
            tmp_grps = (grps[0] - 1,) + grps[1:]
            if tmp_grps[0] == 0:
                tmp_grps = tmp_grps[1:]
                if rec[1] in ['?', '.']:
                    return count_combos(rec[2:], tmp_grps, False)
                else:
                    return 0

            return count_combos(rec[1:], tmp_grps, True)
        
        case '?':
            return count_combos(tuple('.') + rec[1:], grps, started) \
                 + count_combos(tuple('#') + rec[1:], grps, started)

    raise Exception


def part1(input : str):
    entries = []
    with open(input, "r") as f:
        lines = f.readlines()
        for l in lines:
            ls = l.split()
            # appending a '.' to each record tuple to make things easier to parse
            entries.append([tuple(ls[0]) + tuple('.'), list(map(int,ls[1].split(",")))])
    
    count = 0
    for e in entries:
        currrent_count = count_combos(e[0], e[1])
        count += currrent_count
        print(f"{currrent_count} valid combos for: {''.join(e[0])} - {e[1]}")
    
    print(f"total: {count}")


def part2(input : str):
    entries = []
    with open(input, "r") as f:
        lines = f.readlines()
        for l in lines:
            ls = l.split()

            rec = []
            for i in range(5):
                rec += ls[0]
                rec += '?'
            rec.pop()
            tmp_grps = list(map(int,ls[1].split(",")))
            grps = []
            for i in range(5):
                grps += tmp_grps

            # appending a '.' to each record tuple to make things easier to parse
            entries.append([tuple(rec) + tuple('.'), tuple(grps)])

    count = 0
    for e in entries:
        currrent_count = count_combos(e[0], e[1])
        count += currrent_count
        print(f"{currrent_count} valid combos for: {''.join(e[0])} - {e[1]}")
    
    print(f"total: {count}")


def main():
    print("main")
    # part1("input.txt")
    part2("input.txt")


if __name__ == "__main__":
    main()