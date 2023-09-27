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
 

