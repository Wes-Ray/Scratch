
from math import gcd



def main():

    # {'AAA': ('BBB', 'BBB'), 'BBB': ('AAA', 'ZZZ'), 'ZZZ': ('ZZZ', 'ZZZ')}
    node_map = {}
    nodes = []

    with open("input.txt", "r") as file:
        lines = file.readlines()

        instructions = lines[0][:-1]

        for entry in lines[2:]:
            # print(entry.split())
            es = entry.split()
            node_map[es[0]] = (es[2][1:-1], es[3][:-1])

            if es[0][-1] == 'A':
                nodes.append(es[0])
    
    # print("nodes: ", nodes)
    
    print(instructions)
    # print(node_map)

    counts = []

    for i in range(len(nodes)):
        counts.append(0)
        while True:

            # print("nodes: ", nodes)

            
            current_instruction = instructions[counts[i]%len(instructions)]

            if current_instruction == 'L':
                nodes[i] = node_map[nodes[i]][0]
            if current_instruction == 'R':
                nodes[i] = node_map[nodes[i]][1]
                
            # print(f"\tcurrent instr: {current_instruction} -> node {nodes[i]}")

            
            # if count >= 2:
            #     break
            
            counts[i] += 1

            if nodes[i][-1] == 'Z':
                print(f"found final node {i} after {counts[i]} steps")
                break
    
    print("##############")

    print(counts)

    lcm = 1
    for count in counts:
        lcm = lcm * count // gcd(lcm, count)

    print("LCM: ", lcm)


if __name__ == "__main__":
    main()