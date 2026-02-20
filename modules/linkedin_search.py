import urllib.parse


def get_linkedin_search(domain):
    print("\n[+] Preparing LinkedIn Company Search...\n")

    query = f'site:linkedin.com/company "{domain}"'

    encoded_query = urllib.parse.quote(query)

    search_url = f"https://www.google.com/search?q={encoded_query}"

    print("LinkedIn Company Search Link:")
    print(search_url)
