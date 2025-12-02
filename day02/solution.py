def part1(data):
    """
    Count how many numbers within the given ranges repeat some substring of
    digits exactly twice consecutively.
    """

    # Initialize total count
    total = 0

    # Iteratively parse the ranges
    for ranges in data.split(","):
        ind = ranges.find("-")
        start, end = int(ranges[:ind]), int(ranges[ind + 1 :])

        for i in range(start, end + 1):
            s = str(i)
            digits = len(s)

            if s[: digits // 2] == s[digits // 2 :]:
                total += i

    # Output the final count
    return total


def part2(data):
    """
    Count how many numbers within the given ranges repeat some substring of
    digits at least twice consecutively.
    """

    # Initialize total count
    total = 0

    # Iteratively parse the ranges
    for ranges in data.split(","):
        ind = ranges.find("-")
        start, end = int(ranges[:ind]), int(ranges[ind + 1 :])

        # Check each number in the range
        for i in range(start, end + 1):
            s = str(i)
            digits = len(s)
            # Try every block size that divides the digit length
            for size in range(1, digits // 2 + 1):
                if digits % size != 0:
                    continue
                blocks = digits // size
                if all((s[block * size : (block + 1) * size] == 
                        s[(block + 1) * size : (block + 2) * size])
                    for block in range(blocks - 1)
                ):
                    total += i
                    break  # don't add i multiple times

    # Output the final count
    return total


if __name__ == "__main__":
    data = open("input.txt", "r").read()
    # Output the final counts
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
