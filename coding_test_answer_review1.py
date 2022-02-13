import re

# def solution(new_id):
#     st = new_id
#     st = st.lower()
#     st = re.sub('[^a-z0-9\-_.]', '', st)            #remove excepted a to z, 0 to 9, -, _, .
#     st = re.sub('\.+', '.', st)                     #1번이상 반복된 . 을 . 으로 치환
#     st = re.sub('^[.]|[.]$', '', st)                #삭제 맨 앞 . 맨 뒤 . 
#     st = 'a' if len(st) == 0 else st[:15]           #문자열 비었으면 a 아니면 16글자
#     st = re.sub('^[.]|[.]$', '', st)                #remove 맨 앞 . 맨 뒤 .
#     st = st if len(st) > 2 else st + "".join([st[-1] for i in range(3-len(st))])
#     return st

def solution(new_id):
    answer = new_id
    answer = answer.lower()
    answer = re.sub('[^a-z0-9\-_.]', '', answer)
    answer = re.sub('\.+','.',answer)
    answer = re.sub('^[.]|[.]$','',answer)
    answer = 'a' if not answer else answer[:15]
    answer = re.sub('^[.]|[.]$','',answer)
    answer = answer if len(answer) > 2 else answer + ''.join([answer[-1] for i in range(3-len(answer))])
    print(answer)
solution('.....asdf....alef...#@$@#asdf.s.fw%@1...')
solution('a')