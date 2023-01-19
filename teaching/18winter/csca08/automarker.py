import marks


def auto_mark():
    original = 9
    actual = marks.mark_adjustment(original)
    expected = 30
    return actual == expected
