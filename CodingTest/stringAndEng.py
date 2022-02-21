def solution(s):
    dic = {'zero':'0', 'one':'1', 'two':'2', 'three':'3', 'four':'4', 'five':'5', 'six':'6', 'seven':'7', 'eight':'8', 'nine':'9'}
    for key in dic:
        correct = s.find(key)
        if correct != -1:
            s = s.replace(key, dic[key])
    answer = int(s)    
    return answer
print(solution("one4seveneight"))