import os
import pytest
import sub_shifter

TEST_FOLDER = 'test_folder'
CONTENT = '''
62
00:06:17,393 --> 00:06:21,063
There has been someone
swimming at nighttime.

63
00:06:21,272 --> 00:06:26,068
I hear sp... Sp... Sp...
Splashing some nights.

64
00:06:27,027 --> 00:06:30,281
I left here yesterday afternoon,
this filter was empty.

'''

@pytest.fixture
def set_test_folder():
    os.mkdir(TEST_FOLDER)

@pytest.fixture
def delete_test_folder():
    os.rmdir(TEST_FOLDER)


def create_test_sub_file(filename, extention):
    with open(f'/{TEST_FOLDER}/{filename}.{extention}', 'w') as file:
        file.write(CONTENT)
    
def test_startup(set_test_folder):
    dirs = []
    for entry in  os.listdir('.'):
        if os.path.isdir(entry):
            dirs.append(entry)
    assert 'test_folder' in dirs



def test_teardown(delete_test_folder):
    dirs = []
    for entry in  os.listdir('.'):
        if os.path.isdir(entry):
            dirs.append(entry)
    assert 'test_folder' not in dirs





