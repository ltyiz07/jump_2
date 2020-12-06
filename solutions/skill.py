def solution(skill, skill_trees):
    count = 0
    for skill_tree in skill_trees:
        temp = []
        for tree in skill_tree:
            if tree in skill:
                temp.append(skill.find(tree))
        print(temp)
        if temp == [i for i in range(len(temp))]:
            count += 1
    return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA", "ABED"]))
