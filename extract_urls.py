#import requests
import re


with open("url.txt") as file:
    '''
    Print clean links from the url.txt folder.
    '''
    for line in file:
        urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
        print(urls)
    print("\n")

with open("url.txt", "r") as f:
    '''
    Print all content from the url.txt folder.
    '''

    # Set a max capacity to print at once.
    size_to_read = 1000
    f_content = f.read(size_to_read)

    while len(f_content) > 0:
        print(f_content)
        f_content = f.read(size_to_read)