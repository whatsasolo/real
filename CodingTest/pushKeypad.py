def solution(numbers, hand):
    keypad = [[1, 4, 7, '*'],[2, 5, 8, 0],[3, 6, 9, '#']]
    answer = []
    leftHand = [0, 3]
    rightHand = [2, 3]
    for number in numbers:
        for column in range(0, 3):
            if number in keypad[column] and column == 0:
                answer.append('L')
                leftHand = [keypad[column].index(number), column]
                # print(leftHand)
                print('number = ' , number)                 # == 1,1
                print('leftHand = ' , leftHand)             # == 1,0
                print('rightHand = ' , rightHand)           # == 0,2
            elif number in keypad[column] and column == 2:
                rightHand = [keypad[column].index(number), column]
                answer.append('R')
                # print(rightHand)
                print('number = ' , number)                 # == 1,1
                print('leftHand = ' , leftHand)             # == 1,0
                print('rightHand = ' , rightHand)           # == 0,2
            elif number in keypad[column] and column == 1:
                # keypad[column][keypad[column].index(number)]      # == keypad[1,1]
                if (leftHand[0] - column) + (leftHand[1] - keypad[column].index(number)) < (rightHand[0] - column) + (rightHand[1] - keypad[column].index(number)):
                    leftHand = [keypad[column].index(number), column]           #왼손 옮기기
                    answer.append('L')
                elif (leftHand[0] - column) + (leftHand[1] - keypad[column].index(number)) == (rightHand[0] - column) + (rightHand[1] - keypad[column].index(number)):  #중립구간
                    if hand == 'right':
                        rightHand = [keypad[column].index(number), column]
                        answer.append('R')
                    else:
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