 
import dns.resolver

def format_records(records):
    return ", ".join(str(r) for r in records) if records else "Not Found"

def get_dns(domain):
    print("\n" + "="*50)
    print("                  DNS RECORDS")
    print("="*50)

    try:
        resolver = dns.resolver.Resolver()

        try:
            a_records = resolver.resolve(domain, 'A')
            a_result = [r.to_text() for r in a_records]
        except:
            a_result = []

        try:
            mx_records = resolver.resolve(domain, 'MX')
            mx_result = [r.to_text() for r in mx_records]
        except:
            mx_result = []

        try:
            ns_records = resolver.resolve(domain, 'NS')
            ns_result = [r.to_text() for r in ns_records]
        except:
            ns_result = []

        print(f"{'A Records':20}: {format_records(a_result)}")
        print(f"{'MX Records':20}: {format_records(mx_result)}")
        print(f"{'NS Records':20}: {format_records(ns_result)}")

    except Exception as e:
        print("Error fetching DNS records:", e)