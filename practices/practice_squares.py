

def solution(rectangle, characterX, characterY, itemX, itemY):

    # X2 to all value of rectangle
    for rect in rectangle:
        rect[0] *= 2
        rect[1] *= 2
        rect[2] *= 2
        rect[3] *= 2

    # get min x and y
    min_x = 1000
    min_y = 1000
    max_x = 0
    max_y = 0
    for rect in rectangle:
        if min_x > rect[0]:
            min_x = rect[0]
        if min_y > rect[1]:
            min_y = rect[1]
        if max_x < rect[2]:
            max_x = rect[2]
        if max_y < rect[3]:
            max_y = rect[3]

    # move rects to min_x and min_y
    for rect in rectangle:
        rect[0] -= min_x
        rect[1] -= min_y
        rect[2] -= min_x
        rect[3] -= min_y

    # make grid
    grid = [ [0] * max_x for _ in range(max_y) ]
    for rect in rectangle:
        for c in range(rect[1], rect[3]):
            for r in range(rect[0], rect[2]):
                grid[c][r] = 1

    # check start and end point as 2 and 3
    char_x, char_y = characterX, characterY
    char_x *= 2
    char_y *= 2
    char_x -= min_x
    char_y -= min_y
    grid[char_y-1][char_x-1] = 2

    item_x, item_y = itemX, itemY
    item_x *= 2
    item_y *= 2
    item_x -= min_x
    item_y -= min_y
    print(item_x, item_y)
    grid[item_y-1][item_x-1] = 3
    
    [ print(g) for g in grid]



if __name__ == "__main__":
    rect = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    char_x = 1
    char_y = 3
    item_x = 7
    item_y = 8

    print(solution(rect, char_x, char_y, item_x, item_y))
