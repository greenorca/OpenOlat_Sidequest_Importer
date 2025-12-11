import requests
from dotenv import load_dotenv
import os

def upload_single_page(course_id, parent_node_id, file_path):
    """
    Upload a singlepage HTML file to an OpenOLAT course.

    Parameters:
        course_id (int or str): The course ID in OpenOLAT.
        parent_node_id (int): The parent node ID where the page should be added.
        file_path (str): Full path to the HTML file.

    Returns:
        requests.Response: The HTTP response from the server.
    """
    # Load environment variables for authentication
    load_dotenv()
    username = os.getenv('OLAT_USER')
    password = os.getenv('PASSWD')
    url=os.getenv('URL')

    if not username or not password:
        raise ValueError("Missing OLAT_USER or PASSWD in environment variables.")

    # Prepare the URL
    url = f"{url}{course_id}/elements/singlepage"

    # Extract titles from file path
    filename = os.path.basename(file_path)
    short_title = os.path.splitext(filename)[0].replace("_", " ")
    long_title = os.path.splitext(filename)[0]

    data = {
        "shortTitle": short_title,
        "longTitle": long_title,
        "filename": filename,
        "parentNodeId": parent_node_id,
    }

    try:
        with open(file_path, 'rb') as file:
            print(f"Sending request to {url}")
            response = requests.put(
                url,
                data=data,
                files={'path': (filename, file, "text/html")},
                auth=(username, password)
            )

        # Debug output
        print(f"Status Code: {response.status_code}")
        print(f"Request Headers: {response.request.headers}")
        print(f"Response Body: {response.text}")

        return response

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except Exception as e:
        print(f"An error occurred: {e}")
