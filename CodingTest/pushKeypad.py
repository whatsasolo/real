def solution(numbers, hand):
    keypad = [[1, 4, 7, '*'],[2, 5, 8, 0],[3, 6, 9, '#']]
    answer = []
    leftHand = [0, 3]                   #초기 왼손 위치
    rightHand = [2, 3]                  #초기 오른손 위치
    for number in numbers:
        for column in range(0, 3):
            if number in keypad[column] and column == 0:            #왼쪽줄   
                answer.append('L')
                leftHand = [keypad[column].index(number), column]       #왼손 위치 변경
                # print(leftHand)
                print('number = ' , number)                 # == 1,1
                print('leftHand = ' , leftHand)             # == 1,0
                print('rightHand = ' , rightHand)           # == 0,2
            elif number in keypad[column] and column == 2:              #오른쪽줄
                answer.append('R')
                rightHand = [keypad[column].index(number), column]      #오른손 위치 변경
                # print(rightHand)
                print('number = ' , number)                 # == 1,1
                print('leftHand = ' , leftHand)             # == 1,0
                print('rightHand = ' , rightHand)           # == 0,2 
            elif number in keypad[column] and column == 1:                  #가운데 줄
                # keypad[column][keypad[column].index(number)]      # == keypad[1,1]
                if abs((leftHand[0] - column)) + abs((leftHand[1] - keypad[column].index(number))) < abs((rightHand[0] - column)) + abs((rightHand[1] - keypad[column].index(number))):
                    leftHand = [keypad[column].index(number), column]           #왼손 옮기기
                    answer.append('L')
                elif abs((leftHand[0] - column)) + abs((leftHand[1] - keypad[column].index(number))) == abs((rightHand[0] - column)) + abs((rightHand[1] - keypad[column].index(number))):  #중립구간
                    if hand == 'right':                     #오른손잡이
                        rightHand = [keypad[column].index(number), column]
                        answer.append('R')
                    else:                                   #왼손잡이
                        leftHand = [keypad[column].index(number), column]
                        answer.append('L')
                else:                                            #오른손 옮기기
                    rightHand = [keypad[column].index(number), column]
                    answer.append('R')
                print('number = ' , number)                 # == 1,1
                print('leftHand = ' , leftHand)             # == 1,0
                print('rightHand = ' , rightHand)           # == 0,2
                #5, 8, 2, 5, 5
    print(answer)
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")        #4누르고 5누르려면?
keypad = [[1, 2, 3],[4, 5, 6],[7, 8, 9],['*', 0, '#']]
keypad[0].pop()
# print(keypad)
# print(keypad[0].index(1))
#"LRLLLRLLRRL"
#['L', 'R', 'L', 'L', 'R', 'L', 'L', 'L', 'L', 'R', 'L']    
#['L', 'R', 'L', 'R', 'R', 'L', 'L', 'L', 'R', 'R', 'L']    #abs 적용