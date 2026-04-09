def solve() -> None:
    t = int(input())
    for _ in range(t):
        s = input().rstrip()
        stack = []
        ok = True
        for ch in s:
            if ch == "(":
                stack.append(ch)
            elif ch == ")":
                if not stack:
                    ok = False
                    break
                stack.pop()
            # '(' ')' 외 문자는 9012에서 없음. 다른 문제면 else 처리.

        if ok and not stack:
            print("YES")
        else:
            print("NO")


def main() -> None:
    solve()


if __name__ == "__main__":
    main()
