"""Helper that checks your exercise answers. You don't need to edit this file."""

_results = {"passed": 0, "total": 0}


def check(description, func, expected):
    """Run func() and compare its result with expected. Prints PASS or FAIL."""
    _results["total"] += 1
    try:
        got = func()
    except Exception as error:  # show the error instead of crashing
        print(f"  FAIL  {description}\n        error: {type(error).__name__}: {error}")
        return
    if got == expected:
        _results["passed"] += 1
        print(f"  PASS  {description}")
    else:
        print(f"  FAIL  {description}\n        expected {expected!r}, got {got!r}")


def summary():
    passed, total = _results["passed"], _results["total"]
    print(f"\n{passed}/{total} checks passed.")
    if total and passed == total:
        print("Nice work! Move on to the next file.")
