import requests
import re
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def scrape_emails(domain):
    print("\n[+] Searching for public email addresses...\n")

    if not domain.startswith("http"):
        url = "https://" + domain
    else:
        url = domain

    try:
        response = requests.get(url, timeout=5, verify=False)

        email_pattern = r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}"

        found_emails = re.findall(email_pattern, response.text)
        unique_emails = set(found_emails)

        if unique_emails:
            print("[+] Public Emails Found:\n")
            for email in unique_emails:
                print("   -", email)
        else:
            print("[-] No public emails found on homepage.")

    except requests.exceptions.RequestException as err:
        print("[-] Unable to connect to the website.")
        print("Error:", err)


if __name__ == "__main__":
    domain_input = input("Enter domain name (example.com): ")
    scrape_emails(domain_input)
