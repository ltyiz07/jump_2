def read_lines(file_name):
    """

    :param file_name: 파일 이름.
    :return: 각줄을 리스트에 붙여서 리턴
    """
    text = []
    with open(file_name, 'r', encoding="utf-8") as f:
        text.append(f.readline().strip())
        temp_text = "start"
        while temp_text != "":
            temp_text = f.readline().strip()
            text.append(temp_text)
    return text[:-1]


def print_2d(lst):
    for i in lst:
        print(i)


if __name__ == "__main__":
    print(read_lines("example_files\\침몰타이타닉1.txt"))
    print(chr(10))
