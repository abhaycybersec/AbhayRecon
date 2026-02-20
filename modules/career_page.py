import requests

def detect_career_page(domain):
    print("\n[+] Searching for Career Page...\n")

    career_paths = [
        "/careers",
        "/career",
        "/jobs",
        "/join-us",
        "/work-with-us"
    ]

    for path in career_paths:
        url = f"https://{domain}{path}"  
        try:
            response = requests.get(url, timeout=5)
            if response.status_code == 200:
                print(f"[+] Career Page Found: {url}")
                return  # Exit after first found page

        except requests.exceptions.RequestException:
            continue

    print("[-] No common career page found on this domain.")
