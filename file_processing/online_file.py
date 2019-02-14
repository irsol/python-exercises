import urllib.request

url = "https://github.com/irsol"
web_page = urllib.request.urlopen(url)
for line in web_page:
    line = line.strip()
    print(line)
web_page.close()
