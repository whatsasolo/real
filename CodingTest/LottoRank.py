#로또의 최고 순위와 최저 순위
def solution(lottos, win_nums):
    prize_number = []                   #당첨 번호 리스트
    rank = 1                            #rank 기본값
    for number in lottos:
        if number in win_nums:
            prize_number.append(number)
                     #당첨번호랑 일치하는 숫자 리스트
    highRank = rank + (6 - (len(prize_number) + lottos.count(0)))   #highest rank
    lowRank = rank + (6 - len(prize_number))                        #lowest rank
    if lowRank >= 6:                                                #7나오는 경우의 수 제거
        lowRank = 6
    answer = [highRank, lowRank]
    print(len(prize_number))
    print(lottos)
    print(answer)
    return answer
solution([1,2,3,4,5,6], [7,8,9,10,11,12])

#= [6,6]