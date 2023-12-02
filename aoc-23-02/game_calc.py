
MAX_DICT = {
    "red" : 12,
    "green" : 13,
    "blue" : 14,
}

def check_game_list_is_possible(game_list : list) -> tuple:
    print(f"\t{game_list}")
    ret = True
    min_colors = {
        "red" : 0,
        "green" : 0,
        "blue" : 0,
    }
    for game in game_list:
        print(f"\t\t{game} -> {game.split(',')}")
        for round in game.split(","):
            turn = round.split(" ")
            color = turn[2]
            count = int(turn[1])
            is_possible = MAX_DICT[color] >= count
            print(f"\t\t\t{round} -> possible? {is_possible}")
            if not is_possible:
                ret = False

            # check for min req'd colors
            min_colors[color] = max(min_colors[color], count)

    ret_value = 1
    for c in min_colors.values():
        ret_value *= c
    print(f"\t\tfinal colors: {min_colors}")
    return ret, ret_value


def main():
    print("main")

    sum = 0
    cube_sum = 0
    with open("input.txt", "r") as file:
        for line in file.readlines():
            print(line[:-1])
            x = line.split(":")
            game_num = int(x[0].split(" ")[1])
            game_list = x[1].split(";")
            game_list[-1] = game_list[-1][:-1]  # strip off new line char
            
            check = check_game_list_is_possible(game_list)
            if not check[0]:
                print(f"## Game {game_num} was impossible")
            else:
                sum += game_num
            
            cube_sum += check[1]
    
    print(f"SUM: {sum} -- CUBE SUM: {cube_sum}")



if __name__ == '__main__':
    main()