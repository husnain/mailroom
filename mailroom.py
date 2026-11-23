# Mailroom: count the subscribers in data/subscribers.csv
import sys


def read_subscribers(path):
    text = open(path, encoding="utf-8").read()
    lines = text.splitlines()
    rows = []
    for line in lines[1:]:
        if line.strip() != "":
            rows.append(line.split(","))
    return rows


def count_total(rows):
    return len(rows)


def count_by_group(rows):
    counts = {}
    for row in rows:
        group = row[3]
        if group in counts:
            counts[group] = counts[group] + 1
        else:
            counts[group] = 1
    return counts


def show_subscribers():
    rows = read_subscribers("data/subscribers.csv")
    groups = count_by_group(rows)
    print("Total:", count_total(rows))
    for group in groups:
        print(group + ":", groups[group])


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "subscribers":
        show_subscribers()
    else:
        print("Usage: uv run mailroom.py subscribers")
