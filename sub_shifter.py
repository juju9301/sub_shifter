import re
import datetime
import sys
import ntpath


def get_original_filename(path: str):
    # accepts full path, returns list, where 0=filename, [1]-extention
    original_filename =  ntpath.basename(path)
    if '.' in original_filename:
        return original_filename.rsplit(sep='.', maxsplit=1)
    else:
        return [original_filename, '']

def get_original_folder(path: str):
    # save file in directory the original is
    # rename edited file as original, rename orig file as old (optional)
    orig_filename = get_original_filename(path)
    return path.replace(orig_filename, '')

def get_new_filename(path: str):
    # get file name from the file path, create new filename with '_edited' at the end
    orig_filename = get_original_filename(path)
    new_file_list = [(orig_filename[0] + '_edited'), orig_filename[1]]
    if new_file_list[1]:
        return '.'.join(new_file_list)
    else:
        return new_file_list[0]

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
            save_path = get_original_folder(path) + get_new_filename(path)
            with open(save_path, 'a') as fixed_file:
                fixed_file.write(line_copy)



# if __name__ == '__main__':
#     main(sys.argv)
