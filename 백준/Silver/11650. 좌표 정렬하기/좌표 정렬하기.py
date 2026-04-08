def solve() -> None:
    n = int(input())
    nums = []
    for _ in range(n):
        x, y = map(int, input().split())
        nums.append((x, y))

    nums.sort(key=lambda x: (x[0], x[1]))

    for x, y in nums:
        print(x, y)


def main() -> None:
    solve()


if __name__ == "__main__":
    main()
