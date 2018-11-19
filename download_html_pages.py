from url_input import fetch_save_url


def download_urls(file_name):

    with open(file_name) as file:

        count = 1
        for url in file:

            url = url.strip("\n")
            print("Fetching", url)

            f_name = f"output{count}.html"
            fetch_save_url(url, f_name)

            print("Saved to", f_name)
        
            count += 1

download_urls("url.txt")