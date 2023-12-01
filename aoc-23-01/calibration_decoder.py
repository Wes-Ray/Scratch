
COUNTABLES = [str(i) for i in range(10)]
COUNTABLE_STRS = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
ALL_COUNTABLES = COUNTABLES + COUNTABLE_STRS


def tokenize_nums(line : str) -> list:
    found_list = []
    i = 0
    while i < len(line):
        for item in ALL_COUNTABLES:
            slc = line[i:i+len(item)]
            if slc == item:
                found_list.append(item)
        i += 1

    return found_list


def calculate_from_word_list(word_list : list) -> int:
    values = [word_list[0], word_list[-1]]
    int_values = []
    for v in values:
        if v in COUNTABLES:
            int_values.append(int(v))
        elif v in COUNTABLE_STRS:
            int_values.append(int(COUNTABLE_STRS.index(v))+1)

    return int_values[0] * 10 + int_values[1]


def main():
    with open("input.txt", "r") as file:
        sum = 0
        for l in file.readlines():
            sum += calculate_from_word_list(tokenize_nums(l))
        
        print("sum: ", sum)


if __name__ == '__main__':
    main()