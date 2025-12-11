from create_course import create_course
from upload_single_page import upload_single_page
import os
import re




def process_html_files(course_id, editorRootNodeId, directory):
    """
    Iterate through a directory and print file paths of all .html files.
    """
    pattern = re.compile(r"^\d[a-zA-Z]_")
    for root, dirs, files in os.walk(directory):
        dirs.sort()
        for dir in dirs:
            if not pattern.match(dir):
                continue
            for file in os.listdir(os.path.join(root, dir)): 
                if file.lower().endswith("aufgabe.html"):
                    print(os.path.join(root, dir, file))
                    upload_single_page(course_id=course_id, parent_node_id=editorRootNodeId, file_path = os.path.join(root, dir, file))



directory = "/home/sven/Nextcloud/WISS/Modul_165-NoSQL/M165-NoSQL/sidequests/"
title = "M 165"
displayName = "M 165 NoSQL DBs "
description = "Einführung in MongoDB und Co"

result = create_course(title, displayName, description)

course_id = result["key"]
editorRootNodeId = result["editorRootNodeId"]

print("Course created, ID:", course_id)
print("Editor Root Node ID:", editorRootNodeId ) 

process_html_files(course_id=course_id, editorRootNodeId=editorRootNodeId, directory=directory)



