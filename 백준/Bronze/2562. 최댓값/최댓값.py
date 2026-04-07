# 9개의 서로 다른 자연수가 주어질 때, 이들 중 최댓값을 찾고 그 최댓값이 몇 번째 수인지를 구하는 프로그램을 작성하시오.
# 예를 들어, 서로 다른 9개의 자연수
# 3, 29, 38, 12, 57, 74, 40, 85, 61
# 이 주어지면, 이들 중 최댓값은 85이고, 이 값은 8번째 수이다.

def solve() -> None:
    before_value = 0
    max_value = 0
    max_pos = 0

    n = 9

    for i in range(n):
        before_value = max_value

        num = int(input())
        max_value = max(max_value, num)

        if before_value != max_value:
            max_pos = i + 1

    print(max_value)
    print(max_pos)

def main() -> None:
    solve()


if __name__ == "__main__":
    main()