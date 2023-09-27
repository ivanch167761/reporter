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
    Replace windows standard type path with back slash to Linux standard type with normal slash
    """
    return list(map(lambda pathName: pathName.replace('\\', '/'), pathNameList))
