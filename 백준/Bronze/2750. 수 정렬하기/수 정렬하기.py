def solve() -> None:
    n = int(input())
    nums = [int(input()) for _ in range(n)]
    nums.sort()
    print("\n".join(map(str, nums)))


def main() -> None:
    solve()


if __name__ == "__main__":
    main()
