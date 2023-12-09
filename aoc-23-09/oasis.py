

def find_seq(seq : list) -> int:
    
    zeros = 0
    for x in seq:
        if x == 0:
            zeros += 1
    
    if zeros == len(seq):  # all zeros
        return 0
    
    new_seq = []
    for i in range(len(seq)-1):
        new_seq.append(seq[i+1] - seq[i])

    # print(f"\t{new_seq}")

    # return seq[-1] + find_seq(new_seq)  # part 1
    return seq[0] - find_seq(new_seq)  # part 2


def main():
    print("main")
    sequences = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            sequences.append(list(map(int, line.split())))
      
    final_sum = 0
    for s in sequences:
        print(f"{s} ->")
        x = find_seq(s)
        print(f"\t-> {x}")
        final_sum += x
    
    print("FINAL SUM: ", final_sum)
    

if __name__ == "__main__":
    main()