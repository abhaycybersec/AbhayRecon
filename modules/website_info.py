import requests
from bs4 import BeautifulSoup


def get_website_info(domain):
    print("\n[+] Collecting Website Information...\n")

    if not domain.startswith(("http://", "https://")):
        domain = "http://" + domain

    try:
        response = requests.get(domain, timeout=5)

        print(f"Status Code : {response.status_code}")
        print(f"Server      : {response.headers.get('Server', 'Not Available')}")

        soup = BeautifulSoup(response.text, "html.parser")

        if soup.title and soup.title.string:
            page_title = soup.title.string.strip()
        else:
            page_title = "No Title Found"

        print(f"Page Title  : {page_title}")

    except requests.exceptions.Timeout:
        print("Request timed out. Website may be slow or unreachable.")

    except requests.exceptions.ConnectionError:
        print("Failed to connect to the website.")

    except Exception as error:
        print(f"Something went wrong: {error}")
