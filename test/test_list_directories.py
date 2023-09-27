import pytest
from utils import list_files
from utils_test import CONSTANTS_TEST
from utils_test import create_test_purpose_project


@pytest.fixture
def setup()->list[int]:
    """
    create test purpose project 
    """
    create_test_purpose_project.create_test_dir_with_test_data(
            root_dir=CONSTANTS_TEST.ROOT_DIR,
            structure=CONSTANTS_TEST.TEST_FILES)
    return[]

def test_list_directories(setup) -> None:
    """
    1) check all discovered files and directories are on the expected test porpose project dirctory
    2) check all files and directories from test purpose project dirctory are in discovered files
    """
    reportStructure = list(list_files.discover_files(root_path=CONSTANTS_TEST.ROOT_DIR))
    expectedList = create_test_purpose_project.slash_unify(
            create_test_purpose_project.add_root_path(
                CONSTANTS_TEST.TEST_FILES, CONSTANTS_TEST.ROOT_DIR))
    for item in reportStructure:
        assert item in expectedList
    for item in expectedList:
        assert item in reportStructure

