import requests


def fetch_save_url(url, file_name):
    '''
    Takes an url as an input, downloads a page and stores it in the file.
    '''

    try:
        response = requests.get(url, timeout=1)

    except Exception as e:

        print('Error!', e)
        return

    if response.status_code == 200:

        with open(file_name, 'w') as file:
            file.write(response.text)
        print('ok!')
    else:
        print('Error, status code =', response.status_code)


# Test cases

# Successful
fetch_save_url('https://github.com/requests/requests', 'request.html')

# Non URL
fetch_save_url('lll', 'request.html')

# Wrong URL
fetch_save_url('https://github.co/requests/requests', 'request.html')

# Non existing page
fetch_save_url('https://github.com/aj3,o', 'request.html')