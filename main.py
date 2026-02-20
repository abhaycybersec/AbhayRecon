import argparse
import os

os.system("")

from utils.helper import success, error, info, warning

from modules.whois_lookup import get_whois
from modules.dns_lookup import get_dns
from modules.website_info import get_website_info
from modules.subdomain_finder import find_subdomains
from modules.linkedin_search import get_linkedin_search
from modules.career_page import detect_career_page
from modules.email_scraper import scrape_emails


def banner():
    print("\033[91m")
    print("     _    _     _                 ")
    print("    / \\  | |__  | |__   __ _ _   _ ")
    print("   / _ \\ | '_ \\ | '_ \\ / _` | | | |")
    print("  / ___ \\| |_) || | | | (_| | |_| |")
    print(" /_/   \\_\\_.__/ |_| |_|\\__,_|\\__, |")
    print("                               |___/")

    print("\033[94m")
    print("  ____                               ")
    print(" |  _ \\ ___  ___ ___  _ __           ")
    print(" | |_) / _ \\/ __/ _ \\| '_ \\          ")
    print(" |  _ <  __/ (_| (_) | | | |         ")
    print(" |_| \\_\\___|\\___\\___/|_| |_|         ")

    print("\033[0m")
    print(info("\n        Automated OSINT & Recon Toolkit\n"))
    print(warning("        Author: Abhay Pratap Singh Yadav\n"))


def main():
    parser = argparse.ArgumentParser(
        description="AbhayRecon - Automated OSINT & Recon Toolkit"
    )

    parser.add_argument(
        "target",
        nargs="?",
        help="Target domain or IP address (example: google.com)"
    )

    args = parser.parse_args()

    banner()

    if args.target:
        target = args.target.strip()
    else:
        target = input("Enter Domain or IP Address: ").strip()

    if not target:
        print(error("[-] Please provide a valid target."))
        return

    print(info("\n[+] Running WHOIS Lookup...\n"))
    get_whois(target)

    print(info("\n[+] Running DNS Lookup...\n"))
    get_dns(target)

    print(info("\n[+] Running Website Info...\n"))
    get_website_info(target)

    print(info("\n[+] Running Subdomain Enumeration...\n"))
    find_subdomains(target)

    print(info("\n[+] Running LinkedIn Company Search...\n"))
    get_linkedin_search(target)

    print(info("\n[+] Running Career Page Detection...\n"))
    detect_career_page(target)

    print(info("\n[+] Running Public Email Scraper...\n"))
    scrape_emails(target)

    print(success("\n[✓] Scan Completed Successfully!\n"))


if __name__ == "__main__":
    main()