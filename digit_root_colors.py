# Rainbow colors assigned to digit roots 1-9
DIGIT_ROOT_COLORS = {
    1: "Red",
    2: "Orange",
    3: "Yellow",
    4: "Green",
    5: "Blue",
    6: "Indigo",
    7: "Violet",
    8: "Pink",
    9: "Magenta",
}

def digit_root(n: int, base: int = 10) -> int:
    """Compute digit root using modular arithmetic: O(1)."""
    return 0 if n == 0 else (n - 1) % (base - 1) + 1

def get_color(n: int) -> str:
    """Return the color for a number based on its digit root."""
    root = digit_root(n)
    if root == 0:
        return "Black"  # digit root of 0 is 0, no rainbow color
    return DIGIT_ROOT_COLORS[root]


if __name__ == "__main__":
    # Quick demo
    test_numbers = [0, 1, 5, 9, 10, 19, 100, 999, 12345]
    for n in test_numbers:
        print(f"{n:>6}  →  digit root {digit_root(n)}  →  {get_color(n)}")
