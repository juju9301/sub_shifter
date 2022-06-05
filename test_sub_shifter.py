import pytest
import sub_shifter
import datetime

# test get_new_filename


timestamp_str = '''121
00:10:32,940 --> 00:10:34,440
- Ты что, шутишь, бли1н?'''

# 
def test_numeric_input():
    with pytest.raises(TypeError):
        sub_shifter.get_new_filename(12)


def test_other_data_types_input():
    with pytest.raises(TypeError):
        sub_shifter.get_new_filename([1,2,3])

def test_more_than_one_argument():
    with pytest.raises(TypeError):
        sub_shifter.get_new_filename('new_file.srt', 45)

def test_blank_str():
    assert sub_shifter.get_new_filename('') == '_edited'

def test_path_only_dot():
    assert sub_shifter.get_new_filename('.') == '_edited'

def test_valid_path_win():
    path = r'E:\python_proj\subtitle_timing_changer\sub_shifter.py' 
    assert sub_shifter.get_new_filename(path) == 'sub_shifter_edited.py'

def test_valid_path_lin():
    path = '/mnt/sherpa/Marketing'
    assert sub_shifter.get_new_filename(path) == 'Marketing_edited'

def test_valid_path_mac():
    path = '/Volumes/sherpa/Marketing'
    assert sub_shifter.get_new_filename(path) == 'Marketing_edited'

def test_file_with_extention():
    # present in other testcases
    pass

def test_file_without_extention():
    # present in other testcases
    pass

def test_relative_path():
    path = r'..pytest_cache\v\cache\last_failed'
    assert sub_shifter.get_new_filename(path) == 'last_failed_edited'

    # path = r"E:\!MOVIES\All.of.Us.Are.Dead.S01.WEBRip.Rus.HDRezka\An.Education.2009.720p.BluRay.x264.[YTS.MX]-English.srt"
    # main([os.getcwd(), path, '+5'])

class TestTimestampOperations:

    def test_find_timestamps_with_milliseconds(self):
        assert sub_shifter.find_timestamps(timestamp_str) == ['00:10:32,940', '00:10:34,440']

    @pytest.mark.parametrize(
        'timestamp,datetime_obj',
        [
            ('00:10:32,940', datetime.datetime(1900, 1, 1, 0, 10, 32, 940000)),
            ('11:41:17,436', datetime.datetime(1900, 1, 1, 11, 41, 17, 436000))
        ]
    )
    def test_convert_str_into_datetime(self, timestamp, datetime_obj):
        assert sub_shifter.convert_string_to_time(timestamp) == datetime_obj

    @pytest.mark.parametrize('old_time, operation, value, datetime_obj',
        [
            (datetime.datetime(1900, 1, 1, 0, 10, 32, 940000), '+', 1, datetime.datetime(1900, 1, 1, 0, 10, 33, 940000)),
            (datetime.datetime(1900, 1, 1, 0, 10, 32, 945000), '+', 13.5, datetime.datetime(1900, 1, 1, 0, 10, 46, 445000))
        ]
    )
    def test_edit_time(self, old_time, operation, value, datetime_obj):
        assert sub_shifter.edit_time(old_time, operation, value) == datetime_obj

    @pytest.mark.parametrize('datetime_obj, result_str',
        [
            (datetime.datetime(1900, 1, 1, 0, 10, 33, 940000), '00:10:33,940')
        ]
    )
    def test_time_to_string(self, datetime_obj, result_str):
        assert sub_shifter.convert_time_to_string(datetime_obj) == result_str
