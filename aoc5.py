def read_data():
    with open("input.txt", mode="r", encoding="utf-8") as file:
        ranges, ids= file.read().split("\n\n", maxsplit=1)
    ranges = ranges.split()
    return ranges

def merge_ranges(ranges):
    ranges = sorted(ranges)
    merged = [ranges[0]]

    for start, end in ranges[1:]:
        last_start, last_end = merged[-1]

        if start <= last_end + 1:
            merged[-1] = (last_start, max(last_end, end))
        else:
            merged.append((start, end))

    return merged

def count_ids(ranges):
    return sum(end - start + 1 for start, end in ranges)

def function():
    ranges = read_data()
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]

    merged = merge_ranges(ranges)

    total_ids = count_ids(merged)
    print(total_ids)

function()