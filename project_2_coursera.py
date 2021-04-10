import re
import csv
import operator
import sys

file_name = sys.argv[1]
def read_log_errors(file_name):
    with open(file_name,"r") as file:
        file = file.readlines()
        error_dict = {}
        count = 1
        for line in file:
            error_line = re.search(r": ([\w]*).([\w ']*).*\(([\w\.]*)\)", line)
            error_line = error_line.groups()
            if error_line[0] == "INFO":
                continue
            if error_line[1] not in error_dict and error_line[0] != "INFO":
                error_dict[error_line[1]] = count
            else:
                error_dict[error_line[1]] += count
        error_dict = sorted(error_dict.items(), key = operator.itemgetter(1), reverse = True)
    error_dict_columns = ["Error", "Count"]
    csv_file = "error_message.csv"
    with open(csv_file,"w", newline = "") as f:
        write = csv.writer(f)
        write.writerow(error_dict_columns)
        for data in error_dict:
            write.writerow(data)
    return "Error counts file created!"

def read_log_counts(file_name):
    with open(file_name, "r") as file:
        file = file.readlines()
        username_dict = {}
        count = 1
        for line in file:
            username_line = re.search(r": ([\w]*).([\w ']*).*\(([\w\.]*)\)", line)
            username_line = username_line.groups()
            if username_line[2] not in username_dict.keys():
                username_dict[username_line[2]] = {}
                username_dict[username_line[2]]["INFO"] = 0
                username_dict[username_line[2]]["ERROR"] = 0
            if username_line[0] == "INFO":
                username_dict[username_line[2]]["INFO"] += count
            elif username_line[0] == "ERROR":
                username_dict[username_line[2]]["ERROR"] += count
        username_dict = sorted(username_dict.items(), reverse = False)
    count_dict_columns = ["Username", "INFO", "ERROR"]
    csv_file = "user_statistics.csv"
    username_list = []
    with open(csv_file,"w", newline = "") as f:
        write = csv.writer(f)
        write.writerow(count_dict_columns)
        i = 0
        for items in username_dict:
            username, dictionary = username_dict[i]
            username, dictionary = username_dict[i]
            key, value = dictionary.items()
            username_tuple = (username, str(key[1]), str(value[1]))
            write.writerow(username_tuple)
            i += 1
    return "Username counts file created!"

print(read_log_errors(file_name))
print(read_log_counts(file_name))
