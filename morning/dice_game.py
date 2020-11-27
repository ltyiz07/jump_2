from morning.file_reader import read_lines


def dice_game(lst):
    answer = []
    for l in lst:
        for i in range(2):
            if l.count(l[2 * i]) == 3:
                answer.append(int(l[0]) * 1000 + 10000)
                continue
            elif l.count(l[2 * i]) == 2:
                answer.append(int(l[2 * i]) * 100 + 1000)
                continue
        else:
            temp = []
            for j in range(3):
                temp.append(int(l[2 * j]))
            answer.append(max(temp) * 100)

    print("우승자 상금: ", max(answer), "    우승자 * ", answer.count(max(answer)))
    return max(answer)


if __name__ == "__main__":
    print(dice_game(read_lines("example_files\\주사위게임1.txt")[1:-1]))
    print(dice_game(read_lines("example_files\\주사위게임2.txt")[1:-1]))
    print(dice_game(read_lines("example_files\\주사위게임4.txt")[1:-1]))

