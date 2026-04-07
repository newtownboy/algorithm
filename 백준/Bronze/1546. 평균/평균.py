def solve() -> None:
    n = int(input())
    nums = list(map(int, input().split()))

    sum = 0
    max_num = max(nums)
    for i in range(len(nums)):
        sum = sum + ((nums[i] / max_num) * 100)
    print(sum / len(nums))


def main() -> None:
    solve()


if __name__ == "__main__":
    main()