import pytest
from utils import create_headings

from docx import Document

#Creating a temporary document.
@pytest.fixture
def temp_document():
    doc = Document()
    yield doc

# Define test cases
@pytest.mark.parametrize("input_report_folder, expected_report_content", [
    (['./1_Heading_first_level/2_Heading_second_level/3_image.jpg', 
      './2_Heading_first_level/1_Heading_second_level/1_text.txt'
      ], 
'''1 Heading first level
1.2 Heading second level
2 Heading first level
2.1 Heading second level'''),
    (['./1_Heading_1_level/2_Heading_2_level/3_image.jpg', 
      './2_Heading_1_level/1_Heading_2_level/1_text.txt'
      ], 
'''1 Heading 1 level
1.2 Heading 2 level
2 Heading 1 level
2.1 Heading 2 level'''),
    (['/1_StrangeUserName/1_Heading_1_level/2_Heading_2_level/3_image.jpg', 
      '/1_StrangeUserName/2_Heading_1_level/1_Heading_2_level/1_text.txt'
      ], 
'''1 Heading 1 level
1.2 Heading 2 level
2 Heading 1 level
2.1 Heading 2 level'''),
    ])



def test_create_headings(temp_document, input_report_folder, expected_report_content)->None:
    """
     create headings from path to file
    './1_Heading_first_level/2_Heading_second_level/3_image.jpg', 
    './2_Heading_first_level/1_Heading_second_level/1_text.txt'
     has to create:
         1 Heading first level
         1.2 Heading second level
         2 Heading first level
         2.1 Heading second level
    """
    created_headings = []
    for i in input_report_folder:
        create_headings.create_headings_for_file(createdHeadings=created_headings ,filePath=i, rootPath='/1_StrangeUserName/', document=temp_document)
    # Extract the text from the document
    doc_text = '\n'.join(paragraph.text for paragraph in temp_document.paragraphs)
    assert doc_text == expected_report_content
