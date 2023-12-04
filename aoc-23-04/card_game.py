

def find_round_winners(win_nums : list, nums : list) -> list:
    matching_nums = []

    for num in nums:
        if num in win_nums:
            matching_nums.append(num)

    return matching_nums


def add_card_to_dict(card_num : int, add_val : int, card_dict : dict) -> None:
    # TODO: check for falling off the end of the deck (can't add additional cards)
    # init the value if not here, increment otherwise
    if card_num not in card_dict:
        card_dict[card_num] = add_val
    else:
        card_dict[card_num] += add_val


def main():
    print("main")

    total_point_vals = 0
    card_dict = {}  # {card_name_num : number_of_occurences, ...}
    with open("input.txt", "r") as file:
        for card in file.readlines():
            card_split = card.replace(":", "|").split("|")
            card_name_num = int(card_split[0].split()[1])
            win_nums = card_split[1].split()
            nums = card_split[2].split()
            print(card_name_num,":", list(map(int, win_nums)), "|", list(map(int, nums)))

            round_winners = find_round_winners(list(map(int, win_nums)), list(map(int, nums)))
            print("\tround winners: ", round_winners)
            point_val = 0
            if len(round_winners) > 0:
                point_val = 2**(len(round_winners)-1)
            print("\tpoint val: ", point_val)
            total_point_vals += point_val
            
            # adding additional later cards based on current, multiply by number of current cards
            add_card_to_dict(card_name_num, 1, card_dict)  # current, original card
            for i in range(card_name_num + 1, card_name_num + len(round_winners) + 1):  # adding winners
                add_card_to_dict(i, card_dict[card_name_num], card_dict)

            print(f"\tCard Dict Updated: {card_dict}")

    
    print("FINAL POINT VAL: ", total_point_vals)
    print("FINAL DICT: ")
    total_card_count = 0
    for card in card_dict:
        print(f"\tCard {card} count: {card_dict[card]}")
        total_card_count += card_dict[card]
    print("FINAL CARD COUNT: ", total_card_count)

if __name__ == "__main__":
    main()