


def part1(input : str):
    rows = []
    with open(input, "r") as f:
        lines = f.readlines()
        for l in lines:
            rows.append(list(l[:-1]))

    for i in range(len(rows)):
        for y in range(len(rows)-1, -1, -1):
            # print(f"y: {y}")
            for x in range(len(rows[0])):
                # print(f"\tx: {x} {rows[y][x]}")
                if rows[y][x] == 'O':
                    if y-1 == -1:
                        continue
                    if rows[y-1][x] == '.':
                        rows[y-1][x] = 'O'
                        rows[y][x] = '.'
    
    mult = len(rows)
    total = 0
    for r in rows:
        total += r.count('O') * mult
        print("".join(r), mult)
        mult -= 1
    
    print(f"FINAL TOTAL: {total}")


def main():
    print("main")
    part1("input.txt")


if __name__ == "__main__":
    main()