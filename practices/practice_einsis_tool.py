import os


def pprint(line_lst):
    for e, p in enumerate(line_lst):
        print(f"{e}: {p}")
    

def log_parser101(file_path):
    parsed = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "#":
                continue
            formatted_line = line.replace(",", " ")
            formatted_line = formatted_line.replace("\t", ",")
            parsed.append(formatted_line)
    # return parsed.join("\n")
    return "".join(parsed)

def log_parser102(file_path):
    parsed = []
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "#":
                continue
            formatted_line = line.replace(",", "\t")
            parsed.append(formatted_line)
    # return parsed.join("\n")
    return "".join(parsed)

def log_parser103(file_path, column_number, column_value, include=True):
    """
    Input: log file path with version "1.0.2"
    """
    parsed = []
    sep = "\t"
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "#":
                continue

            splited = line.split(sep)
            # TODO: have to check index limit
            if (splited[column_number - 1].strip() == column_value.strip()) == include:
                parsed.append(line)

    return "".join(parsed)


if __name__ == "__main__":

    test_file_path = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample"
    test_output_file_path_101 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.101"
    test_output_file_path_102 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.102"
    test_output_file_path_103 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.103"
    test_output_file_path_103_2 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.103_2"

    # version: 1.0.1
    ## skip line with begin "#"
    ## Change comma -> tab
    ## Change tab -> comma

    # result = log_parser102(test_output_file_path_102)

    THIRD_COL = "113.198.47.187"
    result = log_parser103(test_output_file_path_102, 3, THIRD_COL, False)
    with open(test_output_file_path_103_2, "w") as file:
        file.write(result)
    print(result)

    # version: 1.0.2
    ## Change comma -> tab
