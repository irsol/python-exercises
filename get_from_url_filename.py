

url = "https://docs.python.org/3/library/urllib.request.html#request-objects"

if url.find("/"):
    # fetches the last string after a backslash
    print(url.split("/")[-1])
