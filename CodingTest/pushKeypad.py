
def solution(numbers, hand):
    keypad = [[1, 4, 7, '*'],[2, 5, 8, 0],[3, 6, 9, '#']]
    answer = []
    leftHand = [0, 3]                   #initial lefthand position
    rightHand = [2, 3]                  #initial righthand position
    
    
    for pushToNum in numbers:
        for row in range(0,3):
            if pushToNum in keypad[row] and row == 0: 
                #lefthand
                column = keypad[row].index(pushToNum)
                nowNum = keypad[row][column]
                leftHand = [row, column]
                print(f"nowNum : {nowNum}")
                print(f"leftHand : {leftHand}")
                answer.append("L")
            elif pushToNum in keypad[row] and row == 2:
                #righthand
                column = keypad[row].index(pushToNum)
                nowNum = keypad[row][column]
                rightHand = [row, column]
                print(f"nowNum : {nowNum}")
                print(f"rightHand : {rightHand}")
                answer.append("R")
            elif pushToNum in keypad[row] and row == 1: 
                #caution!
                column = keypad[row].index(pushToNum)
                nowNum = keypad[row][column]
                leftComparison = abs(row - leftHand[0]) + abs(column - leftHand[1])
                rightComparison = abs(row - rightHand[0]) + abs(column - rightHand[1])
                if leftComparison > rightComparison:
                    #righthand is closer
                    rightHand = [row, column]
                    answer.append("R")
                    pass
                elif leftComparison == rightComparison:
                    #same distance
                    if hand == "left":
                        leftHand = [row, column]
                        answer.append("L")
                    else:
                        rightHand = [row, column]
                        answer.append("R")
                else:
                    #lefthand is closer
                    leftHand = [row, column]
                    answer.append("L")
                    pass
                print(f"nowNum : {nowNum}")
                print(abs(row - leftHand[0]), abs(row - rightHand[0]))
                print(abs(column - leftHand[1]), abs(column - rightHand[1]))
                print(leftComparison, rightComparison)
                print("-----------------------------")
                # print(f"leftHand : {leftHand}")
                # print(f"rightHand : {rightHand}")
                
    print(''.join(answer))
solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right")
'''
5 : [1,1]
LH : [0,1]
RH : [2,0]
abs?
rowcomparison : LH = 1, RH = 1
columncomparison : LH = 0, RH = 1
1, -1       abs -> 1, 1
0, 1        abs -> 0, 1
            plus-> 1, 2
'''

# print(keypad)
# print(keypad[0].index(1))
#"LRLLLRLLRRL"
#"LRLLLRLLRRL"
#['L', 'R', 'L', 'L', 'R', 'L', 'L', 'L', 'L', 'R', 'L']    
#['L', 'R', 'L', 'R', 'R', 'L', 'L', 'L', 'R', 'R', 'L']    #abs 적용