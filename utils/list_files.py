from typing import Generator, Optional, List
import os



def discover_files(root_path: str, extensions: Optional[List[str]] = None) -> Generator[str, None, None]:

    """
    Discover files within a directory tree.

    Args:
        root_path (str): The root directory to start searching from.
        extensions (list, optional): A list of file extensions to filter by. If None, all files are included.

    Yields:
        str: The path to each discovered file.
    """
    for root, _, files in os.walk(root_path):
        if not _ and not files:
            yield (root+'\\').replace('\\', '/')
        for file_name in files:
            if extensions is None or any(file_name.endswith(ext) for ext in extensions):
                file_path = os.path.join(root, file_name).replace('\\', '/')
                yield file_path
 

def add_root_path(relativePathList:list[str], root_path:str)->list[str]:
    """
    convert relative path to absolute
    """
    list_with_root_path = []
    for relativePath in relativePathList:
        list_with_root_path.append(os.path.join(root_path, relativePath[2:]))
    return list_with_root_path

def slash_unify(pathNameList:list[str])->list[str]:
    """
    Convert Windows standard path with backslashes to Linux standard path with forward slashes.
    """
    return list(map(lambda pathName: pathName.replace('\\', '/'), pathNameList))

def custom_sort_key(path):
    """
    Organize files and directories in ascending order based on a hierarchical structure, ensuring a clean and orderly arrangement:
        Example of sorted list:
            ./1_text
            ./1_text/1_text
            ./1_text/1_text/1_text
            ./1_text/2_text
            ./1_text/3_text`
    """
    parts = path.split('/')
    numbers = [int(part.split('_')[0]) for part in parts if part.split('_')[0].isdigit()]
    return numbers, path

def sort_data(pathNameList:list[str])->list[str]:
    """
    Apply sort method for whole file list.
    """
    return sorted(pathNameList, key=custom_sort_key)

