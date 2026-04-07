def solve() -> None:
    word = input().upper()

    dict = {}

    for alphabet in word:
        cnt = dict.get(alphabet, 0)
        dict[alphabet] = cnt + 1

    max_cnt = max(dict.values())
    winners = [ch for ch, c in dict.items() if c == max_cnt]

    print(winners[0] if len(winners) == 1 else "?")


def main() -> None:
    solve()


if __name__ == "__main__":
    main()