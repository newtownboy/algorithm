# 선형탐색: 모든 원소를 한 번씩 보며 최소·최대 갱신. 시간 복잡도 O(N)

def solve() -> None:
    n = int(input())
    nums = set(map(int, input().split()))

    m = int(input())
    targets = list(map(int, input().split()))

    for target in targets:
        if target in nums:
            print(1)
        else:
            print(0)


def main() -> None:
    solve()


if __name__ == "__main__":
    main()