def part1(data):
    """
    Count how many times the dial ends up on 0 after a series of rotations.
    """
    # Open the input file and read all of the rotations
    rotations = data

    # Initialize the starting points
    dial = 50
    count = 0

    # Iteratively parse the rotations and count the 0s
    for rot in rotations:
        dir, dist = rot[:1], int(rot[1:])
        dial = (dial + dist if dir == "R" else dial - dist) % 100
        if dial == 0:
            count += 1

    # Output the final count
    return count


def part2(data):
    """
    Count how many times the dial touches 0 after a series of rotations,
    considering full rotations.
    """
    # Open the input file and read all of the rotations
    rotations = data

    # Initialize the starting points
    dial = 50
    count = 0

    # Iteratively parse the rotations and count the 0s
    for rot in rotations:
        dir, dist = rot[:1], int(rot[1:])

        # Update the count and dist
        count += dist // 100
        dist = dist % 100

        # Update the dial
        for i in range(dist):
            dial = (dial + 1 if dir == "R" else dial - 1) % 100
            if dial == 0:
                count += 1

    # Output the final count
    return count


if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    # Output the final counts
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
