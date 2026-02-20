import dns.resolver

def find_subdomains(domain):
    print("\n" + "="*50)
    print("              SUBDOMAIN ENUMERATION")
    print("="*50)

    # Common subdomains list
    common_subdomains = [
        "www", "mail", "ftp", "webmail", "admin",
        "blog", "dev", "test", "api", "portal"
    ]

    found_subdomains = []

    for sub in common_subdomains:
        subdomain = f"{sub}.{domain}"
        try:
            dns.resolver.resolve(subdomain, 'A')
            found_subdomains.append(subdomain)
        except:
            pass

    if found_subdomains:
        print(f"{'Found Subdomains':20}: {', '.join(found_subdomains)}")
    else:
        print("No common subdomains found.")