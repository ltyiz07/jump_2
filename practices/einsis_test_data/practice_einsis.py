import os

def pprint(line_lst):
    for e, p in enumerate(line_lst):
        print(f"{e}: {p}")
    

def log_parser101(file_path):
    """
    # version: 1.0.1
    ## skip line with begin "#"
    ## Change comma -> tab
    ## Change tab -> comma
    """
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
    """
    # version: 1.0.2
    ## input log file should be version 1.0.1
    ## Change comma -> tab
    """
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
    # version: 1.0.3
    ## write only include or exclude column_value
    ## column_number starts with 0
    ## to support command line args using sys.argv or commandline arg libraries...
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


def log_parser104(file_path, column_number, column_value):
    from collections import defaultdict
    """
    # version: 1.0.4
    ## count matched colum values
    Input: log file path with version "1.0.2"
    """
    sep = "\t"
    value_set = defaultdict(int)
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "#":
                continue

            splited = line.split(sep)
            # TODO: have to check index limit
            value_set[splited[column_number - 1].strip()] += 1

    return value_set


def log_parser105(file_path):
    """
    # version: 1.0.5
    ## Change time formats timestamp -> timeformat
    Input: log file path with version "1.0.2"
    changes time format
    """
    # TODO: have to move this import to top...
    import datetime
    import time

    parsed = []
    sep = "\t"
    with open(file_path, "r") as f:
        lines = f.readlines()
        for line in lines:
            if line[0] == "#":
                continue

            splited = line.split(sep)
            timestamp = splited[0]
            datetime_obj = datetime.datetime.fromtimestamp(int(float(timestamp)))
            # a = time.mktime(datetime_obj.timetuple())
            splited[0] = str(datetime_obj)

            parsed.append(sep.join(splited))
            # TODO: have to check index limit

    return "".join(parsed)



if __name__ == "__main__":

    test_file_path = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample"
    test_output_file_path_101 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.101"
    test_output_file_path_102 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.102"
    test_output_file_path_103 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.103"    # include
    test_output_file_path_103_2 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.103_2"    # exclude 
    test_output_file_path_105 = r"C:\pyth\jump_2\practices\einsis_test_data\http.log.sample.105"
    # result = log_parser102(test_output_file_path_102)

    THIRD_COL = "113.198.47.187"
    result = log_parser105(test_output_file_path_102)
    with open(test_output_file_path_105, "w") as file:
        file.write(result)
    print(result)

    # version: 1.0.2
    ## Change comma -> tab
