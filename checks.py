# Checks: the expected answers, written before the code
from mailroom import read_subscribers, count_total, count_by_group

rows = read_subscribers("data/subscribers.csv")
assert count_total(rows) == 24
groups = count_by_group(rows)
assert len(groups) == 3
assert groups["tea-curious"] == 8
assert groups["gift-buyers"] == 8
assert groups["daily-drinkers"] == 8

print("All checks pass.")
