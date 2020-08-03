# not mine but a bit simpler than mine.
def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if completion[i] != participant[i]:
            return participant[i]
    return participant[-1]

# def solution(participant, completion):
#     answer = ""
#     participant.sort()
#     completion.sort()
#     lenth = len(completion)
#     for i in range(lenth):
#         if completion[i] != participant[i]:
#             answer = participant[i]
#             break
#         else:
#             answer = participant[-1]
#     return answer
