# 선형탐색: 모든 원소를 한 번씩 보며 최소·최대 갱신. 시간 복잡도 O(N)

def solve() -> None:
    n = int(input())

    nums = list(map(int, input().split()))

    print(min(nums), max(nums))


def main() -> None:
    solve()


if __name__ == "__main__":
    main()