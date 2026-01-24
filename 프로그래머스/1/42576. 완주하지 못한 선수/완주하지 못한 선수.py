from collections import Counter

def solution(participant, completion):
    counterP = Counter(participant)
    counterC = Counter(completion)
    diff = counterP - counterC
    
    return list(diff.elements())[0]