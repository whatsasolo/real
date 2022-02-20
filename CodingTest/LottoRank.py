'''
1	6개 번호가 모두 일치
2	5개 번호가 일치
3	4개 번호가 일치
4	3개 번호가 일치
5	2개 번호가 일치
6(낙첨)	그 외
'''

def solution(lottos, win_nums):
    prize_number = []                   #당첨 번호 리스트
    rank = 1                            #rank 기본값
    for number in lottos:
        if number in win_nums:
            prize_number.append(number)         #당첨번호랑 일치하는 숫자 리스트
    highRank = rank + (6 - (len(prize_number) + lottos.count(0)))   #highest rank
    lowRank = rank + (6 - len(prize_number))                        #lowest rank
    if lowRank >= 6:                                                #7나오는 경우의 수 제거
        lowRank = 6
    answer = [highRank, lowRank]
    return answer
print(solution([0, 0, 0, 0, 0, 0],[38, 19, 20, 40, 15, 25]))
