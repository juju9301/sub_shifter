import re
import datetime
import sys




def find_timestamps(line):
    return re.findall(r'[0-9]+:[0-9]+:[0-9]+', line)

def convert_string_to_time(line):
    return datetime.datetime.strptime(line, '%H:%M:%S')

def calculated_datetime(old_time, operation, value):
    return eval(f'old_time {operation} datetime.timedelta(seconds=value)')

def convert_time_to_string(time):
    return datetime.datetime.strftime(time, '%H:%M:%S')




def main(path, value):
    # format '+2' or '-67', in seconds
    operation = value[0]
    value[1:] = value
    with open(path, 'r') as file:
        content = file.readlines()
        for line in content:
            line_copy = line
            timestamps = find_timestamps(line)
            if len(timestamps) > 0:
                for timestamp in timestamps:
                    old_time = convert_string_to_time(timestamp)
                    new_time = calculated_datetime(old_time, operation, value)
                    new_string = convert_time_to_string(new_time)
                    line_copy = line_copy.replace(timestamp, new_string)
            with open('sub_fixed.srt', 'a') as fixed_file:
                fixed_file.write(line_copy)



if __name__ == '__main__':
    main(*args)


