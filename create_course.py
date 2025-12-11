import xml.etree.ElementTree as ET
import requests
import os
from dotenv import load_dotenv
import base64

def create_course(title, displayName, description):

    load_dotenv()
    username = os.getenv('OLAT_USER')
    password = os.getenv('PASSWD')
    url = os.getenv('URL')

    querystring = {"title":title,"displayName":displayName,"description":description,
        "publicVisible":"true",
        "membersOnly":"false",
        "setAuthor":"true",
        "repoEntryStatus":"published"}

    payload = ""
    response = requests.put( url, data=payload, auth=(username, password), params=querystring)

    return extract_course_info(response.text)

def extract_course_info(xml_string):
    """
    Extracts the <key> and <editorRootNodeId> values from the given course XML string.

    Args:
        xml_string (str): The XML content as a string.

    Returns:
        dict: {"key": str, "editorRootNodeId": str}
    """
    root = ET.fromstring(xml_string)
    
    key = root.findtext("key")
    editor_root_node_id = root.findtext("editorRootNodeId")
    
    return {
        "key": key,
        "editorRootNodeId": editor_root_node_id
    }

if __name__ == "__main__":
    
    response = create_course("M 007", "Demo-Modul 007", "Demo Course Description")
    print(response.text)
