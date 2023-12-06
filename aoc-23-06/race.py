

def main():
    # could combine these into one dict
    total_times = []
    record_distances = []
    with open("input.txt", "r") as file:
        lines = file.readlines()
        total_times = list(map(int, lines[0].split()[1:]))
        record_distances = list(map(int, lines[1].split()[1:]))
    times_to_records = dict(zip(total_times, record_distances))

    total_num_ways = 1
    for total_time in times_to_records:
        print(f"time: {total_time} record dist: {times_to_records[total_time]}")
        num_ways = 0
        for i in range(1, total_time):
            current_dist = calc_dist(i, total_time)
            if current_dist > times_to_records[total_time]:
                num_ways += 1
        if num_ways > 0:
            total_num_ways *= num_ways
    print(f"total ways to beat: {total_num_ways}")
        

def calc_dist(in_time : int, total_time : int) -> int:
    return in_time * (total_time - in_time)


if __name__ == "__main__":
    main()