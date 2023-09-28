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
    1) Verify that all discovered files and directories exist within the designated test purpose project directory.
    2) Confirm that all files and directories within the test purpose project directory are present in the discovered files.
    """
    reportStructure = list(list_files.discover_files(root_path=CONSTANTS_TEST.ROOT_DIR))
    expectedList = list_files.slash_unify(
            list_files.add_root_path(
                CONSTANTS_TEST.TEST_FILES, CONSTANTS_TEST.ROOT_DIR))
    for item in reportStructure:
        assert item in expectedList
    for item in expectedList:
        assert item in reportStructure



def test_check_if_sorted(setup)->None:
    """
    Sort the discovered list of files and compare it to the expected list; they must match.
    """
    reportStructure = list_files.sort_data(list(list_files.discover_files(root_path=CONSTANTS_TEST.ROOT_DIR)))
    expectedList = list_files.slash_unify(
            list_files.add_root_path(
                CONSTANTS_TEST.TEST_FILES, CONSTANTS_TEST.ROOT_DIR))
    assert reportStructure == expectedList
