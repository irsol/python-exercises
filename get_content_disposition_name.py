import requests
import re
# name extracted from the string with regular expression or re module


def get_filename(content_disposition):
    '''
    Get file name from content-disposition
    '''

    if not content_disposition:
        return None
    fname = re.findall("filename=(.+)", content_disposition)
    return fname[0]


url = "https://github.com/irsol"
r = requests.get(url, allow_redirects=True)
filename = get_filename(r.headers.get("content-disposition"))
    
with open(filename, "w") as file:
    file.write(r.content)
    print("ok")