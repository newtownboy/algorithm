import sys


def solve() -> None:
    # 표준 입력 전체를 한 번에 읽고 공백/줄바꿈 기준으로 나눔 (수 백만 개에 유리)
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    nums = list(map(int, data[1 : n + 1]))
    nums.sort()
    sys.stdout.write("\n".join(map(str, nums)))


def main() -> None:
    solve()


if __name__ == "__main__":
    main()