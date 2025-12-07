def part1(lines):
    """
    Count the number of splitters (^) that the beams hit as they travel down
    from the starting point (S).
    """

    # Initialize total splitters hit and starting columns
    total = 0
    cols = {lines[0].find("S")}

    # Process each row below the starting row
    for line in lines[1:]:
        next_cols = set()

        for c in cols:
            if line[c] == "^":
                # Beam hits splitter: it stops and splits
                total += 1
                next_cols.add(c - 1)
                next_cols.add(c + 1)
            else:
                # Non-splitter: beam continues straight down
                next_cols.add(c)

        # Move to next row with updated beams
        cols = next_cols

    # Return total splitters hit
    return total


def part2(lines):
    """
    Count the total number of distinct paths the beams can take from the
    starting point (S) to the bottom of the grid, considering all possible
    splits at each splitter (^).
    """

    # Initialize starting counts
    counts = [0] * len(lines[0])
    counts[lines[0].find("S")] = 1

    # Process each row below the starting row
    for line in lines[1:]:
        for i, c in enumerate(counts):
            if line[i] == "^":
                counts[i] = 0
                counts[i - 1] += c
                counts[i + 1] += c

    # Return total distinct paths
    return sum(counts)


if __name__ == "__main__":
    with open("day07/example.txt") as f:
        data_example = f.readlines()
        data_example = [datum.strip() for datum in data_example]
    with open("day07/input.txt") as f:
        data_input = f.readlines()
        data_input = [datum.strip() for datum in data_input]

    print(f"Part 1 (example): {part1(data_example)}")
    print(f"Part 2 (example): {part2(data_example)}")
    print(f"Part 1 (input): {part1(data_input)}")
    print(f"Part 2 (input): {part2(data_input)}")
