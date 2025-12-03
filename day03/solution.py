def part1(data):
    """
    Find the largest two-digit number of consecutive digits in each line
    and return the sum of these numbers.
    """

    # Strip whitespace from each line
    lines = [line.strip() for line in data]

    total = 0
    # Process each line to find the largest two-digit number
    for line in lines:
        max = 0
        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                num = int(line[i]) * 10 + int(line[j])
                if num > max:
                    max = num
        print(max)
        total += max

    # Return the final total
    return total


def part2(data):
    """
    Find the largest twelve-digit number of consecutive digits in each line
    and return the sum of these numbers.
    """

    # Convert each line into a list of integers
    lines = [list(map(int, line.strip())) for line in data]

    total = 0
    k = 12

    # Process each line to find the largest k-digit number
    for line in lines:
        n = len(line)
        left = 0
        max_num = 0

        # Build the largest k-digit number step by step
        for i in range(k):
            end = n - (k - i) + 1
            window = line[left:end]
            m = max(window)
            ind = window.index(m) + left

            max_num = max_num * 10 + line[ind]
            left = ind + 1

        total += max_num

    # Return the final total
    return total


if __name__ == "__main__":
    data = open("input.txt", "r").readlines()
    # Output the final totals
    print(f"Part 1: {part1(data)}")
    print(f"Part 2: {part2(data)}")
