def solve() -> None:
    max_value = 0
    max_pos = 0

    for i in range(9):
        num = int(input())
        if num > max_value:
            max_value = num
            max_pos = i + 1

    print(max_value)
    print(max_pos)


def main() -> None:
    solve()


if __name__ == "__main__":
    main()
