

def main():
    # convert maps to dicts, each map is its own dict
    seeds = []  # list of seed int values
    maps = []  # list of dicts, each dict is a map
    with open("ezinput.txt", "r") as file:
        lines = file.readlines()
        seeds = list(map(int, lines[0].split(":")[1].split()))

        for line in lines[1:]:
            print(line[:-1])
    
    print()
    print(f"seeds: {seeds}")
    print(f"maps: {maps}")


if __name__ == "__main__":
    main()