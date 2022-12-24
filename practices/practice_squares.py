
def get_top_rect_idx(rects):
    top_idx = 0
    top_val = 0
    for e, rect in enumerate(rects):
        if top_val < rect[3]:
            top_val = rect[3]
            top_idx = e
    return top_idx

def is_reange_over(range_1, range_2):
    left_range = min([range_1, range_2])
    right_range = max([range_1, range_2])
    if left_range[1] > right_range[0]:
        return True
    return False

def is_rect_over(rect_1, rect_2):
    if (is_reange_over((rect_1[0], rect_1[2]), (rect_2[0], rect_2[2]))) and (is_reange_over((rect_1[1], rect_1[3]), (rect_2[1], rect_2[3]))):
        return True
    return False

def solution(rectangle, characterX, characterY, itemX, itemY):
    calced_rect_idxs = [get_top_rect_idx(rectangle)]
    while rectangle:
        for idx in calced_rect_idxs:
            top_rect = rectangle.pop(rect_idx)
            over_rects = []
            for rect in rectangle:
                if is_reange_over(top_rect, rect):
                    print("over")

    return None


if __name__ == "__main__":
    rect = [[1,1,7,4],[3,2,5,5],[4,3,6,9],[2,6,8,8]]
    char_x = 1
    char_y = 3
    item_x = 7
    item_y = 8

    print(solution(rect, char_x, char_y, item_x, item_y))
