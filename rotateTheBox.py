box1 = [["#",".","#"]]

box2 = [["#",".","*","."],
        ["#","#","*","."]]

box3 = [["#","#","*",".","*","."],
        ["#","#","#","*",".","."],
        ["#","#","#",".","#","."]]

box4 = [
    ['#'],
    ['#'],
    ['#'],
]
def rotateTheBox(box):
    """
    :type box: List[List[str]]
    :rtype: List[List[str]]
    """
    rock,empty,obstacle = '#', '.','*'
    rowLen,columnLen = len(box),len(box[0])
    for row in range(rowLen):
        movePos = columnLen-1
        for column in range(columnLen-1,-1,-1):
            curr = box[row][column]
            if curr == obstacle: movePos=column-1
            elif curr==rock:
                 box[row][column],box[row][movePos]= empty,rock 
                 movePos-=1
    return list(zip(*box[::-1]))

    
    
print(rotateTheBox(box3))

'''
[('.', '#', '#'),
 ('.', '#', '#'),
 ('#', '#', '*'),
 ('#', '*', '.'),
 ('#', '.', '*'),
 ('#', '.', '.')]'''