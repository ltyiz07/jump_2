import copy
def solution(skill, skill_trees):
    answer = 0
    for tree in skill_trees:
        temp_index_list = []
        for k in skill:
            if k in tree:
                index_k = tree.index(k)
                temp_index_list.append(index_k)
        temp_copied_list = copy.copy(temp_index_list)
        temp_copied_list.sort()
        print(temp_index_list)
        print(temp_copied_list)
        temp_tree = []
        if temp_copied_list == temp_index_list:
            for i in skill:
                if i in tree:
                    pass





            answer += 1

    return answer

solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"])