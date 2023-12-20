import time


class xmas:
    def __init__(self, x : int, m : int, a : int, s :int) -> None:
        self.x = x
        self.m = m
        self.a = a
        self.s = s
    
    def __str__(self):
        return f"[x={self.x}, m={self.m}, a={self.a}, s={self.s}]"
    
    def value(self) -> int:
        return self.x + self.m + self.a + self.s


class xmas_range:
    def __init__(self, workflow, x1, x2, m1, m2, a1, a2, s1, s2) -> None:
        self.workflow = workflow
        self.x1 = x1
        self.x2 = x2
        self.m1 = m1
        self.m2 = m2
        self.a1 = a1
        self.a2 = a2
        self.s1 = s1
        self.s2 = s2
    
    def copy(self) -> object:
        return xmas_range(self.workflow, self.x1, self.x2, self.m1, self.m2, self.a1, self.a2, self.s1, self.s2)
    
    def __str__(self) -> str:
        return f"[ {self.workflow} :: x:{self.x1}->{self.x2}, m:{self.m1}->{self.m2}, a:{self.m1}->{self.m2}, s:{self.s1}->{self.s2} ]"


def process(inp : xmas, workflows : dict) -> bool:

    result = "in"  # always starts with in

    x = inp.x
    m = inp.m
    a = inp.a
    s = inp.s

    while result not in ["A", "R"]:
        rules = workflows[result]
        print(f"\trules: {rules}")
        print(f"\txmas: {inp}")
        for r in rules:
            if ":" in r:
                # print("true", end=" ")
                rs = r.split(":")
                # print(f"test: {eval(rs[0])}")
                if eval(rs[0]):
                    # print("eval to true")
                    result = rs[1]
                    break
            else:  # catch-all found
                result = r
                break
        
    print(f"\tfinal: {result}")

    # exit()

    if result == "A":
        return True
    elif result == "R":
        return False
    else:
        raise Exception("Invalid Result Found")


def part1(file_name : str) -> None:

    workflows = {}
    inputs = []


    with open(file_name, "r") as f:
        lines = f.readlines()
        all_workflows_found = False
        for l in lines:
            if l == "\n":
                all_workflows_found = True
                continue
            
            if not all_workflows_found:
                # add workflows to dict
                s = l[:-2].split("{")
                workflows[s[0]] = s[1].split(",")
            else:
                s = l[1:-2].split(",")
                inputs.append(xmas(int(s[0][2:]), int(s[1][2:]), int(s[2][2:]), int(s[3][2:])))
    
    print("workflows: ")
    for w in workflows:
        print(f"{w} : {workflows[w]}")
    print("inputs: ")
    for i in inputs:
        print(i)
    
    print("-"*40)
    
    total = 0
    for i in inputs:
        acceptable = process(i, workflows)
        if acceptable:
            total += i.value()

    print("FINAL TOTAL: ", total)


def part2(file_name : str) -> None:
    workflows = {}
    with open(file_name, "r") as f:
        lines = f.readlines()
        all_workflows_found = False
        for l in lines:
            if l == "\n":
                break
            # add workflows to dict
            s = l[:-2].split("{")
            workflows[s[0]] = s[1].split(",")

    print(workflows)
    seed = xmas_range("in", 1, 4000, 1, 4000, 1, 4000, 1, 4000)
    seeds = [seed]

    accepts = []
    rejects = []

    while len(seeds) > 0:
        print("-"*40)
        tmp_seed = seeds.pop()
        print(f"processing: {tmp_seed}, len(seeds) = {len(seeds)}")

        if tmp_seed.workflow == "A":
            print(f"tmp_seed = A: {tmp_seed}")
            accepts.append(tmp_seed)
            continue
        elif tmp_seed.workflow == "R":
            print(f"tmp_seed = R: {tmp_seed}")
            rejects.append(tmp_seed)
            continue

        rules = workflows[tmp_seed.workflow]
        print(f"rules: {rules}")
        for rule in rules:
            print("rule: ", rule)
            # new_seed = xmas_range("UNSET", 0, 0, 0, 0, 0, 0, 0, 0)
            new_seed = tmp_seed.copy()
            if ":" in rule:  # non-catch-all
                rs = rule.split(":")  # rs[0] = x>50 ; rs[1] = target workflow label (e.g. px)
                new_seed.workflow = rs[1]
                if ">" in rs[0]:
                    print("\tgt")
                    rss = rs[0].split(">")
                    match rss[0]:
                        case "x":
                            print("\tx")
                            new_seed.x1 = int(rss[1]) + 1
                            new_seed.x2 = tmp_seed.x2
                            if new_seed.x1 > new_seed.x2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.x2 = int(rss[1])  # strip tmp_seed
                        case "m":
                            print("\tm")
                            new_seed.m1 = int(rss[1]) + 1
                            new_seed.m2 = tmp_seed.m2
                            if new_seed.m1 > new_seed.m2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.m2 = int(rss[1])  # strip tmp_seed
                        case "a":
                            print("\ta")
                            new_seed.a1 = int(rss[1]) + 1
                            new_seed.a2 = tmp_seed.a2
                            if new_seed.a1 > new_seed.a2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.a2 = int(rss[1])  # strip tmp_seed
                        case "s":
                            print("\ts")
                            new_seed.s1 = int(rss[1]) + 1
                            new_seed.s2 = tmp_seed.s2
                            if new_seed.s1 > new_seed.s2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.s2 = int(rss[1])  # strip tmp_seed
                elif "<" in rs[0]:
                    print("\tlt")
                    rss = rs[0].split("<")
                    match rss[0]:
                        case "x":
                            print("\tx")
                            new_seed.x1 = tmp_seed.x1
                            new_seed.x2 = int(rss[1]) - 1
                            if new_seed.x1 > new_seed.x2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.x1 = int(rss[1])  # strip tmp_seed
                        case "m":
                            print("\tm")
                            new_seed.m1 = tmp_seed.m1
                            new_seed.m2 = int(rss[1]) - 1
                            if new_seed.m1 > new_seed.m2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.m1 = int(rss[1])  # strip tmp_seed
                        case "a":
                            print("\ta")
                            new_seed.a1 = tmp_seed.a1
                            new_seed.a2 = int(rss[1]) - 1
                            if new_seed.a1 > new_seed.a2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.a1 = int(rss[1])  # strip tmp_seed
                        case "s":
                            print("\ts")
                            new_seed.s1 = tmp_seed.s1
                            new_seed.s2 = int(rss[1]) - 1
                            if new_seed.s1 > new_seed.s2:
                                print("\tcontinuing")
                                continue
                            tmp_seed.s1 = int(rss[1])  # strip tmp_seed
                else:
                    raise Exception("gt/lt not found in rule")
                
            else:  # catch-all
                new_seed.workflow = rule  # no other modifications to copy of tmp_seed needed
                # this should be the end of each for loop, and tmp_seed is no longer valid/relevant

            print(f"\tappending {new_seed}, current seed(modified) {tmp_seed}")
            seeds.append(new_seed)

            # print("\tbreaking after first rule")
            # break


        print(f"current seeds: {seeds}")

        # break
    
    print("*"*40)

    sum_seed = [0, 0, 0, 0]
    for acc in accepts:
        print(acc)
        sum_seed[0] += acc.x2 - acc.x1
        sum_seed[1] += acc.m2 - acc.m1
        sum_seed[2] += acc.a2 - acc.a1
        sum_seed[3] += acc.s2 - acc.s1
    
    for acc in rejects:
        print(acc)
        sum_seed[0] -= acc.x2 - acc.x1
        sum_seed[1] -= acc.m2 - acc.m1
        sum_seed[2] -= acc.a2 - acc.a1
        sum_seed[3] -= acc.s2 - acc.s1
    
    print(sum_seed)

    total = 1
    for x in sum_seed:
        total *= x
    
    # should be 167409079868000
        # get   156993005505498624
        #       4183390145088414
    print(f"FINAL TOTAL: {total}")





def main():
    print("main")
    t1 = time.time()
    # part1("input.txt")
    part2("ezinput.txt")

    t2 = time.time()

    print(f"\ntime elapsed: {t2 - t1}")

if __name__ == "__main__":
    main()