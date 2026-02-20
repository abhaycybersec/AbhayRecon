import whois

def format_single(value):
    if isinstance(value, list):
        return value[0]
    return value

def format_date(value):
    value = format_single(value)
    if hasattr(value, "strftime"):
        return value.strftime("%Y-%m-%d %H:%M:%S")
    return value

def format_list_inline(value):
    if isinstance(value, list):
        return ", ".join(str(v) for v in value)
    return value

def get_whois(domain):
    print("\n" + "="*50)
    print("                WHOIS INFORMATION")
    print("="*50)

    try:
        info = whois.whois(domain)

        print(f"{'Domain Name':20}: {format_single(info.domain_name)}")
        print(f"{'Registrar':20}: {format_single(info.registrar)}")
        print(f"{'Creation Date':20}: {format_date(info.creation_date)}")
        print(f"{'Expiration Date':20}: {format_date(info.expiration_date)}")
        print(f"{'Updated Date':20}: {format_date(info.updated_date)}")
        print(f"{'Organization':20}: {format_single(info.org)}")
        print(f"{'Country':20}: {format_single(info.country)}")
        print(f"{'Name Servers':20}: {format_list_inline(info.name_servers)}")
        print(f"{'Status':20}: {format_list_inline(info.status)}")

    except Exception as e:
        print("Error fetching WHOIS:", e)