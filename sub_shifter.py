import re
import datetime
import sys
import ntpath


def get_new_filename(path: str):
    # get file name from the file path, create new filename with '_edited' at the end
    orig_filename = ntpath.basename(path)
    if '.' in path:
        filename = orig_filename.split('.')
        name = filename[0]
        extention = filename[1]
        return name + '_edited.' + extention 
    else:
        return orig_filename + '_edited'

def find_timestamps(line: str):
    # find all occurances of timestamps
    # looking for partial strings in format '00:13:14', 
    # ignores milliseconds
    return re.findall(r'[0-9]+:[0-9]+:[0-9]+', line)

def convert_string_to_time(line: str):
    # convert string to datetime object
    return datetime.datetime.strptime(line, '%H:%M:%S')

def edit_time(old_time, operation, value):
    # edit datetime object by addition or subtraction value in seconds
    return eval(f'old_time {operation} datetime.timedelta(seconds=value)')

def convert_time_to_string(time):
    # convert datetime object to string, to timestamp format
    return datetime.datetime.strftime(time, '%H:%M:%S')

def validate_input(*args):
    # validate arguments passed to main function
    # -validate number of arguments
    # -validate argument types
    # - validate path is not '' and valid path

    pass


def main(*args):
    # path is path to file
    # value should be string in format '+2' or '-67', in seconds
    path = args[0]
    value = args[1]
    operation = value[0]
    value = int(value[1:])
    with open(path, 'r') as file:
        content = file.readlines()
        for line in content:
            line_copy = line
            timestamps = find_timestamps(line)
            if len(timestamps) > 0:
                for timestamp in timestamps:
                    old_time = convert_string_to_time(timestamp)
                    new_time = edit_time(old_time, operation, value)
                    new_string = convert_time_to_string(new_time)
                    line_copy = line_copy.replace(timestamp, new_string)
            with open(get_new_filename(path), 'a') as fixed_file:
                fixed_file.write(line_copy)



# if __name__ == '__main__':
#     main(sys.argv)



print(get_new_filename(''))