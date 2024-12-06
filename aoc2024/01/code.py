import os
from collections import defaultdict


def part1(l, r):
    l.sort()
    r.sort()
    dist = 0
    for i in range(len(l)):
        dist += abs(l[i] - r[i])

    return dist


def part2(l, r):
    mp = defaultdict(lambda: 0)

    for v in r:
        mp[v] += 1

    sim = 0
    for v in l:
        sim += v * mp[v]

    return sim


def main():
    l = []
    r = []
    with open(f"{os.path.dirname(__file__)}/input.txt") as f:
        for line in f:
            line = line.strip()
            l1, r1 = line.split()
            l.append(int(l1))
            r.append(int(r1))

    print(part1(l, r))
    print(part2(l, r))


main()
