import sys

class Status:
    move_costs = {
        (0, 0): 1, (0, 1): 7, (0, 2): 6, (0, 3): 7, (0, 4): 5, (0, 5): 4, (0, 6): 5, (0, 7): 3, (0, 8): 2, (0, 9): 3,
        (1, 1): 1, (1, 2): 2, (1, 3): 4, (1, 4): 2, (1, 5): 3, (1, 6): 5, (1, 7): 4, (1, 8): 5, (1, 9): 6,
        (2, 2): 1, (2, 3): 2, (2, 4): 3, (2, 5): 2, (2, 6): 3, (2, 7): 5, (2, 8): 4, (2, 9): 5,
        (3, 3): 1, (3, 4): 5, (3, 5): 3, (3, 6): 2, (3, 7): 6, (3, 8): 5, (3, 9): 4,
        (4, 4): 1, (4, 5): 2, (4, 6): 4, (4, 7): 2, (4, 8): 3, (4, 9): 5,
        (5, 5): 1, (5, 6): 2, (5, 7): 3, (5, 8): 2, (5, 9): 3,
        (6, 6): 1, (6, 7): 5, (6, 8): 3, (6, 9): 2,
        (7, 7): 1, (7, 8): 2, (7, 9): 4,
        (8, 8): 1, (8, 9): 2,
        (9, 9): 1,
    }
    def __init__(self):
        self.left = "4"
        self.right = "6"
        self.cost = 0

    def copy(self):
        s = Status()
        s.left = self.left
        s.right = self.right
        s.cost = self.cost
        return s

    def get_cost(self, f, t):
        arr = (int(f), int(t))
        return Status.move_costs[(min(arr), max(arr))]

    def move_left(self, to):
        self.cost += self.get_cost(self.left, to)
        self.left = to

    def move_right(self, to):
        self.cost += self.get_cost(self.right, to)
        self.right = to


def solution(numbers):

    ar = []
    # TODO: chage this function and Status class to DP
    def dfs(status, word):
        # print(f"left: {status.left}, right: {status.right}, cost: {status.cost}")
        if len(word) == 0:
            ar.append(status.cost)
            return
        else:

            if word[0] == status.left:
                status.move_left(word[0])
                dfs(status, word[1:])
            elif word[0] == status.right:
                status.move_right(word[0])
                dfs(status, word[1:])
            else:
                c_status = status.copy()
                status.move_left(word[0])
                dfs(status, word[1:])
                c_status.move_right(word[0])
                dfs(c_status, word[1:])

    dfs(Status(), numbers)
    return min(ar)


if __name__ == "__main__":
    # sol = solution("1756")    # result: 10
    sol = solution("0000000000")
    print(sol)
