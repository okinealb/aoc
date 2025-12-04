def part1(data):
    """
    Count the number of accessible cells in the grid.
    """

    # Clean data
    data = [line.strip() for line in data if line.strip()]

    # Get dimensions
    m = len(data)
    n = len(data[0])

    # Initialize count
    count = 0

    # Iterate through each cell, counting the number accessible
    for row in range(m):
        for col in range(n):
            if data[row][col] != "@":
                continue

            # Set the bounds for adjacent cells
            top = max(0, row - 1)
            bot = min(m, row + 2)
            lft = max(0, col - 1)
            rgt = min(n, col + 2)

            # Initialize total adjacent count
            total = 0
            # Check all adjacent cells
            for i in range(top, bot):
                for j in range(lft, rgt):
                    if data[i][j] == "@":
                        total += 1

            # Subtract one to not count the cell itself
            if total - 1 < 4:
                count += 1

    # Return final count
    return count


def part2(data):
    """
    Count the number of accessible cells in the grid, removing them and
    re-evaluating until no more can be removed.
    """

    # Clean data
    data = [line.strip() for line in data if line.strip()]

    # Get dimensions
    m = len(data)
    n = len(data[0])

    # Initialize count and stack
    count = 0
    stack = []

    # Function to count accessible cells and add to the stack
    # (nearly the same as part 1)
    def count_accessible():
        count = 0
        for row in range(m):
            for col in range(n):
                if data[row][col] != "@":
                    continue
                total = 0
                top = max(0, row - 1)
                bot = min(m, row + 2)
                lft = max(0, col - 1)
                rgt = min(n, col + 2)
                for i in range(top, bot):
                    for j in range(lft, rgt):
                        if data[i][j] == "@":
                            total += 1
                if total - 1 < 4:
                    stack.append((row, col))
                    count += 1

        return count

    # Iteratively count and remove accessible cells
    while True:
        if (curr_count := count_accessible()) == 0:
            return count
        else:
            count += curr_count
            # Remove cells in stack
            while stack:
                row, col = stack.pop()
                data[row] = data[row][:col] + "." + data[row][col + 1 :]


if __name__ == "__main__":
    data = open("day04/example.txt").readlines()
    # Output results
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
