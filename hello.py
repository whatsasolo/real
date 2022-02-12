from copy import copy
from hashlib import new
from multiprocessing.connection import answer_challenge
import re
from string import punctuation
def solution(new_id):   #최소시간:0.07ms 최대시간:0.21ms 최소용량:12.2MB 최대용량:12.4MB 정확도:92.3
    symbols = punctuation.replace('-','').replace('_','').replace('.','')
    new_id = new_id.casefold()
    if new_id:
        for symbol in symbols:
            new_id = new_id.replace(symbol,'')
        p = re.compile('[.]{2,}')
        m = p.findall(new_id)
        for i in range(0, len(m)):
            new_id = new_id.replace(m[i],'.')
        new_id = new_id.strip('.')
        if len(new_id) >= 16:
            new_id = new_id[0:15]
        elif len(new_id) == 0:
            new_id = 'aaa'
        else:
            while len(new_id) <= 2:
                new_id = new_id + new_id[-1]
        new_id = new_id.strip('.')
    else:
        new_id = 'aaa'
    answer = new_id
    return answer
def solution2(new_id):
    if not new_id:
        answer = 'a'
    else:
        answer = copy(new_id)
    symbols = punctuation.replace('-','').replace('_','').replace('.','')
    answer = answer.casefold()
    while answer:
        for symbol in symbols:
            answer = answer.replace(symbol,'')
        p = re.compile('[.]{2,}')
        m = p.findall(answer)
        for i in range(0, len(m)):
            answer = answer.replace(m[i],'.')
        answer = answer.strip('.')
        if len(answer) >= 16:
            answer = answer[0:15]
        elif len(answer) == 0:
            answer = 'aaa'
        else:
            while len(answer) <= 2:
                answer = answer + answer[-1]
        result = answer
        print(result)
        print(answer)
        if answer == result:
            break
        answer =  result
    return answer
# print(solution('abcdefghijklmn.p'))
print(solution2('abcdefghijklmn.p'))
# from concurrent.futures.process import _ExceptionWithTraceback
# import re
# from string import punctuation
# #"...!@BaT#*..y.abcdefghijklm"
# new_id = "...!@BaT#*..y.abcdefghijklm"
# empty_id = ""
# # new_string = re.sub(r"[^a-zA-Z0-9]","",new_id)
# # print(new_string)
# p = re.compile('[.]{2,}')
# m = p.findall(new_id)
# # print(m)
# symbols = punctuation.replace('-','').replace('_','').replace('.','')       #제외할 특수문자 리스트

# new_id = new_id.casefold()
# if new_id:
#     print(new_id)
#     for symbol in symbols:                                      #문제 제외하기
#         new_id = new_id.replace(symbol,'')
#     print(new_id)
#     for i in range(0, len(m)):
#         new_id = new_id.replace(m[i],'.')
#     # new_id.replace(r'[.+]','')
    
#     print(len(new_id))
#     if len(new_id) >= 16:
#         new_id = new_id[0:15]
#     elif len(new_id) == 0:
#         new_id = 'aaa'
#     else:
#         while len(new_id) <= 2:
#             new_id = new_id + new_id[-1]
#         print(new_id)
#     new_id = new_id.strip('.')
# else:
#     new_id = 'aaa'
# print(new_id)


# p1 = re.compile('[a-z]')
# p2 = re.compile('[0-9]')
# print(p1.findall('...!@BaT#*..y.abcdefghijklm'))
# print(p2.findall('...!@BaT#*..y.abcdefghijklm'))
# excepted_new_id = new_id.pop(p1.findall('...!@BaT#*..y.abcdefghijklm'))

# print(excepted_new_id)
# print(type(p))


# print(new_id.casefold())
# if new_id == "":
#     new_id = 'a'
# elif  in new_id :
#     casefold_new_id = new_id.casefold()
