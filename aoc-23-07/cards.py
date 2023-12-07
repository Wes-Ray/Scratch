

def card_value(card : str) -> str:
    # A 14, K 13, Q 12, J 11, T 10, 9 - 2
    # A, K, Q, T, 9 - 2, J.
    if card.isnumeric():
        return '0' + card
    elif card == 'A':
        return '14'
    elif card == 'K':
        return '13'
    elif card == 'Q':
        return '12'
    elif card == 'J':
        return '01'
    elif card == 'T':
        return '10'


def hand_value(hand : str) -> int:
    # return value as digit
    # TYPE_VALUE + card1val + card2val + ... <- as string combined
    # 4 02 03... -> 4020311  # two digits for each card val
    hand = hand.split()[0]
    # hand = ['QQQJA', '483']
    card_vals = ''
    for ch in hand:
        card_vals += card_value(ch)

    hand = list(hand)
    hand.sort()
    # print("hand: ", hand)

    new_hands = []
    for x in range(len(hand)):
        # print(hand[x])
        tmp_hand = hand
        replace_char = hand[x]
        tmp_hand = list(map(lambda x: x.replace('J', replace_char), tmp_hand))
        tmp_hand.sort()
        new_hands.append(tmp_hand)

    # print(new_hands)
    
    max_hand_type = 0
    for hand in new_hands:
        hand_type = 0
        # five of a kind = 6 pts
        if hand.count(hand[0]) == 5:
            hand_type = 6
        # four of a kind = 5 pts
        elif (hand.count(hand[0]) == 4) or (hand.count(hand[-1]) == 4):
            hand_type = 5
        # full house = 4 pts
        elif hand.count(hand[0]) + hand.count(hand[-1]) == 5:
            hand_type = 4
        # three of a kind = 3 pts
        elif (hand.count(hand[0]) == 3) or (hand.count(hand[-1]) == 3) or (hand.count(hand[1]) == 3):
            hand_type = 3

        if hand_type == 0:
            pair_count = 0
            for ch in hand:
                if hand.count(ch) == 2:
                    pair_count += 1
            hand_type = pair_count // 2
        
        # print("hand_type: ", hand_type, end=" ")
        
        max_hand_type = max(max_hand_type, hand_type)
    
    # print(" max_hand_type: ", max_hand_type)
        

    strength = int(str(max_hand_type) + card_vals)
    # print("\tstrength: ", strength)
    return strength


def main():
    with open("input.txt", "r") as file:
        hands = file.readlines()
    
    # for hand in hands:
    #     # print(hand_value(hand))
    #     print(hand[:-1])

    hands.sort(key=hand_value)

    print("\n#######\n")

    total = 0
    for i in range(len(hands)):
        print(f"{i+1} - {hands[i][:-1]} \n-> {hand_value(hands[i])}")
        total += (i+1) * int(hands[i].split()[-1])
        print()
    print("FINAL TOTAL: ", total)
    
    

if __name__ == "__main__":
    main()