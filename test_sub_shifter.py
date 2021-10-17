import pytest
import sub_shifter

# test get_new_filename

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
    # need to change function to check len of extention
    assert sub_shifter.get_new_filename('.') == '_edited.'

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
    pass

def test_file_without_extention():
    pass

def test_relative_path():
    # currently test fails, should modify the fumction
    path = r'..pytest_cache\v\cache\lastfailed'
    assert sub_shifter.get_new_filename(path) == 'last_failed_edited'
