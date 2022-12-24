def sort(lst=[]):
    tpl = tuple(lst)
    pos = 0
    que = []
    for e, i in enumerate(tpl):
        sub = lst.pop()
        if e == 0:
            que.insert(0, sub)
            continue
        elif sub >= que[pos]:
            for c in que[pos:]:
                if len(que[pos:]) == 1:
                    pos += 1
                    que.insert(pos, sub)
                    break
                elif que[pos] >= sub:
                    que.insert(pos, sub)
                    break
                elif 1 < len(que[pos:]):
                    pos += 1
                    continue
                else:
                    que.insert(pos, sub)
                    break
        elif sub < que[pos]:
            if len(que[:pos]) == 0:
                pos = 0
                que.insert(pos, sub)
                continue
            pos -= 1
            for c in que[:pos+1]:
                if pos == 0:
                    que.insert(pos, sub)
                elif que[pos] <= sub:
                    que.insert(pos+1, sub)
                    break
                else:
                    pos -= 1
    return que
    


a = [2, 5, 1, 8, 12, 36, 1, 0, 7, 19]
print(sort(a))
