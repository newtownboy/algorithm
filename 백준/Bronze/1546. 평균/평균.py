def solve() -> None:
    n = int(input())
    nums = list(map(int, input().split()))
    m = max(nums)
    total = sum(x / m * 100 for x in nums)
    print(total / n)


def main() -> None:
    solve()


if __name__ == "__main__":
    main()
