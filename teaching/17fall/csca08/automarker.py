# Don't worry about how this function is implemented.
def break_print():
    def fake_print(s):
        raise Exception("NO PRINT STATEMENTS!!!")
    import builtins
    builtins.print = fake_print









def auto_mark():
    break_print()
    import curve
    if curve.mark_adjustment(9) == 30:
        result = "Test passed"
    else:
        result = "Test failed"
    return result
