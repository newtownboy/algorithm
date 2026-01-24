# 1. 참가자 배열을 순회하면서 이름은 key, 등장 횟수를 value로 저장
# 2. 완주자 배열을 순회하면서 해당 이름의 value를 하나씩 줄인다.
# 3. 마지막에 value가 1이상 남아있는 key가 완주하지 못한 선수
def solution(participant, completion):
    dic = {}
    
    for p in participant:
        dic[p] = dic.get(p, 0) + 1
        
    for c in completion:
        dic[c] -= 1
    
    for k, v in dic.items():
        if v > 0:
            return k