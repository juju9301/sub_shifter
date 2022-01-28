import re
import datetime
import sys, os
import ntpath
from my_logger import get_my_logger

logger = get_my_logger(__name__)


def find_srt_files():
    # find all srt files in folder, return error if none
    files = []
    current_path = os.getcwd()
    for x in os.listdir(current_path):
        if x.endswith('.ass') or x.endswith('.srt'):
            files.append(x)
    if len(files) == 1:
        f = files[0]
        logging.info(f'file {f} will be processed')
        path = current_path + '\\' + f
    elif len(files) == 0:
        raise Exception('No subtitle file in current directory')
    elif len(files) > 1:
        raise Exception(f'Found {len(files)} files in current directory. Please choose one to process')
    
    return path

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
    orig_filename = ntpath.basename(path)
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

def validate_input(string):
    # validate value
    try:
        string[0] == '+' or string[0] == '-'
    except Exception:
        logging.error('Invalid operator!!')
    finally:
        if not string[1:].isnumeric():
            logging.error('Value is not numeric')



def main(args):
    # path is path to file
    # value should be string in format '+2' or '-67', in seconds
    print(f'args are {", ".join([a for a in args])}')
    if len(args) < 3:
        try: 
            path = find_srt_files()
            value = args[1]
        except IndexError:
            logging.error('Please provide value!!')
            return
        except Exception as error:
            logging.error(error)
            return
    elif len(args) > 3:
        raise Exception('too many arguments!!')
        return
    elif len(args) == 3:            
        path = args[1]
        value = args[2]
    validate_input(value)
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



if __name__ == '__main__':
    main(sys.argv)

