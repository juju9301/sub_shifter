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