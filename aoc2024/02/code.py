import collections
import os


def part1(lines):
    ans = 0
    for l in lines:
        if check_rep(l):
            ans += 1

    return ans


def part2(lines):
    ans = 0
    for l in lines:
        for i in range(len(l)):
            l1 = l[:i] + l[i + 1 :]
            if check_rep(l1):
                ans += 1
                break

    return ans


def check_rep(l):
    inc_or_desc = l == sorted(l) or l == sorted(l, reverse=True)
    safe = True
    for i in range(1, len(l)):
        diff = abs(l[i] - l[i - 1])
        if not 0 < diff <= 3:
            safe = False
            break

    if inc_or_desc and safe:
        return True

    return False


def main():
    lines = []
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            l = line.strip().split()
            lines.append([int(i) for i in l])

    print(part1(lines))
    print(part2(lines))


main()
