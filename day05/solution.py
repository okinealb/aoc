def part1(data):
    """
    Count the number of IDs that fall within any of the given ranges.
    """

    # Read and clean input data
    lines = [line.strip() for line in data]

    # Initialize variables
    ranges = []
    total = 0

    # Process each line in the input
    for line in lines:
        # Skip empty lines
        if line == "":
            continue

        # Try to parse the ID and check if it is in any range
        try:
            id = int(line)
            for start, end in ranges:
                if start <= id <= end:
                    total += 1
                    break

        # Otherwise, parse the range and add it to the list
        except Exception:
            start, end = line.split("-")
            start, end = int(start), int(end)
            ranges.append((start, end))

    # Return the total count of IDs found in ranges
    return total


def part2(data):
    """
    Find the total length covered by the given ranges, merging any
    overlapping ranges.
    """

    # Read and clean input data
    lines = [line.strip() for line in data]

    # Initialize variables
    ranges = []

    # Process each line in the input, adding ranges to the list
    for line in lines:
        if line == "":
            break
        start, end = line.split("-")
        ranges.append((int(start), int(end)))

    # Merge overlapping ranges
    ranges.sort(key=lambda x: x[0])
    merged = []

    # Iteratively merge ranges
    curr_start, curr_end = ranges[0]
    for s, e in ranges[1:]:
        if s <= curr_end + 1:
            curr_end = max(curr_end, e)
        else:
            merged.append((curr_start, curr_end))
            curr_start, curr_end = s, e
    merged.append((curr_start, curr_end))

    # Calculate the total length of merged ranges
    total = 0
    for start, end in merged:
        total += end - start + 1
    return total


if __name__ == "__main__":
    # Read input data from file
    with open("day05/input.txt") as f:
        data = f.readlines()

    # Output results for both parts
    print("Part 1:", part1(data))
    print("Part 2:", part2(data))
