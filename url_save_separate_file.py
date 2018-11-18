import requests


def save_separate_url(url, file_name):

    response = requests.get(url)

    with open(file_name, "w") as file:
        file.write(response.text)
        print("Successful!!!")

# Test cases

# Successful
save_separate_url('https://google.com', 'request.html')
