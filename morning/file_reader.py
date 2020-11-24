def read_lines(file_name):
    text = []
    with open(file_name, 'r', encoding="utf-8") as f:
        text.append(f.readline())
        temp_text = "start"
        while temp_text != "":
            temp_text = f.readline()
            text.append(temp_text)
    return text


if __name__ == "__main__":
    print(read_lines("example_files\\침몰타이타닉1.txt"))
