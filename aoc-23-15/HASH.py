

def Holiday_ASCII_String_Helper(key : str) -> int:
    hash = 0
    
    for c in key:
        hash += ord(c)
        hash *= 17
        hash %= 256
    
    return hash


def main():
    print("main")
    lenses = []
    with open("input.txt", "r") as f:
        lenses = f.readline().split(",")
        lenses[-1] = lenses[-1][:-1]
    print(lenses)

    boxes = {}

    for lens in lenses:
        if "=" in lens:
            label = lens.split("=")[0]
            focal_length = int(lens.split("=")[1])
            box_num = Holiday_ASCII_String_Helper(label)

            if box_num not in boxes:
                boxes.update({box_num : [[label, focal_length]]})
            else:
                # check if label exists already and replace
                replaced = False
                for item in boxes[box_num]:
                    if item[0] == label:
                        replaced = True
                        item[1] = focal_length
                # append if it doesn't
                if not replaced:
                    boxes[box_num].append([label, focal_length])


        elif "-" in lens:
            label = lens.split("-")[0]
            box_num = Holiday_ASCII_String_Helper(label)
            if box_num in boxes:
                removed = False
                for item in boxes[box_num]:
                    if item[0] == label:
                        boxes[box_num].remove(item)
                        removed = True
                        break
                if removed and len(boxes[box_num]) == 0:
                    boxes.pop(box_num)
        
        # DEBUG PRINT
        print(f"{lens} " + "-"*30)
        for b in boxes:
            print(f"\t{b} - {boxes[b]}")
        


    total = 0
    # total += Holiday_ASCII_String_Helper(label)
    for b in boxes:
        i = 1
        for item in boxes[b]:
            print(f"{item}", end=" -> ")
            lens_value = b + 1
            lens_value *= i
            i += 1
            lens_value *= item[1]
            
            print(f"{lens_value}")
            total += lens_value

    print("\nFINAL: ", total)


if __name__ == "__main__":
    main()