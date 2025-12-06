def read_data():
    with open("input.txt", mode="r", encoding="utf-8") as file:
        ranges, ids = file.read().split("\n\n", maxsplit=1)
    ranges = ranges.split()
    ids = ids.split()
    return ids, ranges

def count_fresh(ids, ranges):
    count = 0

    for ingredient in ids:
        x = int(ingredient)
        for start, end in ranges:
            if start <= x <= end:
                count += 1
                break

    return count

def function():
    print("Etape 1")
    ids, ranges = read_data()
    ranges = [tuple(map(int, r.split("-"))) for r in ranges]
    print("Etape 2")
    total = count_fresh(ids, ranges)
    print(total)

function()