import os
from openpyxl import Workbook
from PIL import Image
from typing import List

def create_test_dir_with_test_data(root_dir: str, structure: List[str])->None:
    """
    Create folders naming them as Headings in Report.
Inside directory create:
	.txt files, containing sample text information.
	.jpg files, containing sample image.	
	.xlsx fles, containing sample table
each file and direcory have index number at the beggining of name.
    """
    # Create the root directory if it doesn't exist
    os.makedirs(root_dir, exist_ok=True)
    
    # Define the directory structure based on the diagram
    directories: List[str] = structure
    
    # Create directories
    for directory in directories:
        dir_path: str = os.path.join(root_dir, directory)
        os.makedirs(os.path.dirname(dir_path), exist_ok=True)
        if dir_path.endswith('.txt'):
            with open(dir_path, "w") as file:
                file.write(f"This is {directory} content.")
        if dir_path.endswith('.xlsx'):
            wb = Workbook()
            ws = wb.active
            ws.title = 'aaa'
            ws.append(['Name', 'Age'])
            ws.append(['Alice', 28])
            ws.append(['Bob', 32])
            wb.save(dir_path)
        if dir_path.endswith('.jpg'):
            img: Image.Image = Image.new('RGB', (100, 100), color='red')
            img.save(dir_path)
    print("Directory structure and files created successfully.")


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
