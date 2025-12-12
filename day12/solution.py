def part1(data):
    """
    Count the number of regions that can fit all the presents' quantities.
    """

    # Parse all the presents
    presents = []
    idx = 0
    while idx < len(data):
        line = data[idx]

        if "x" in line:
            break

        # the next three lines are the shape rows
        shape = []
        for j in range(3):
            shape.append([char == "#" for char in data[idx + j + 1]])
        presents.append(shape)

        # Update index to skip the next 5 rows
        idx += 5

    # Parse all the regions
    regions = []
    while idx < len(data):
        line = data[idx]
        if not line:
            idx += 1
            continue
        rows, cols, *quantities = line.replace("x", " ").replace(":", " ").split()
        quantities = [int(q) for q in quantities]
        regions.append((int(rows), int(cols), quantities))
        idx += 1

    # Calculate the total number of presents that can fit in the regions
    total = 0
    presents = [sum([sum(row) for row in present]) for present in presents]
    for rows, cols, quantities in regions:
        # Element wise multiplication of the quantities and the presents
        required = sum([q * p for q, p in zip(quantities, presents)])
        total += required < (rows * cols)

    # Return the total number of presents that can fit in the regions
    return total


if __name__ == "__main__":
    with open("day12/example.txt") as f:
        data_example = f.readlines()
        data_example = [datum.strip() for datum in data_example]
    with open("day12/input.txt") as f:
        data_input = f.readlines()
        data_input = [datum.strip() for datum in data_input]

    print(f"Part 1 (example): {part1(data_example)}")
    print(f"Part 1 (input): {part1(data_input)}")
