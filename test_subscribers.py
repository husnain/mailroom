from mailroom import read_subscribers, count_total, count_by_group

rows = read_subscribers("data/subscribers.csv")


def test_total_subscriber_count_is_24():
    assert count_total(rows) == 24


def test_there_are_3_groups():
    assert len(count_by_group(rows)) == 3


def test_tea_curious_has_8_subscribers():
    assert count_by_group(rows)["tea-curious"] == 8


def test_gift_buyers_has_8_subscribers():
    assert count_by_group(rows)["gift-buyers"] == 8


def test_daily_drinkers_has_8_subscribers():
    assert count_by_group(rows)["daily-drinkers"] == 8
