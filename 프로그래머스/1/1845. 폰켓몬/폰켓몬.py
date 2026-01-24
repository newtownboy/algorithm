def solution(nums):
    # 서로 다른 종류의 개수
    unique = len(set(nums))
    # 뽑을 수 있는 최대 개수 = 전체 길이의 절반
    limit = len(nums) // 2
    return min(unique, limit)