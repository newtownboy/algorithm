import sys


def solve() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    cards = set(map(int, data[1 : n + 1]))
    m = int(data[n + 1])
    targets = list(map(int, data[n + 2 : n + 2 + m]))

    out = ["1" if t in cards else "0" for t in targets]
    sys.stdout.write(" ".join(out))


def main() -> None:
    solve()


if __name__ == "__main__":
    main()
