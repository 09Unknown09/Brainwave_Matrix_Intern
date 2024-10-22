import requests
from bs4 import BeautifulSoup

# List of common phishing indicators
PHISHING_INDICATORS = [
    'login', 'account', 'sign-in', 'secure', 'confirm', 'verify', 'update',
    'reset', 'password', 'email', 'username', 'bank', 'paypal', 'facebook',
    'apple', 'google', 'microsoft', 'amazon'
]

# List of common suspicious TLDs
SUSPICIOUS_TLDS = [
    'com.br', 'com.cn', 'com.co', 'com.hk', 'com.tw', 'com.vn', 'co.cc',
    'co.kr', 'co.uk', 'co.jp', 'co.in', 'co.id', 'co.th', 'co.za', 'co.kr'
]

def check_phishing_indicators(url):
    for indicator in PHISHING_INDICATORS:
        if indicator in url.lower():
            return True
    return False

def check_suspicious_tld(url):
    domain = url.split('.')[-2]
    if domain in SUSPICIOUS_TLDS:
        return True
    return False

def check_suspicious_content(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')
        forms = soup.find_all('form')
        for form in forms:
            if 'action' in form.attrs and 'login' in form['action'].lower():
                return True
            if 'input' in form.attrs and any(input.get('type') == 'password' for input in form.find_all('input')):
                return True
    except requests.RequestException:
        return False
    return False

def is_phishing_link(url):
    if check_phishing_indicators(url):
        print(f"URL contains phishing indicators: {url}")
        return True
    if check_suspicious_tld(url):
        print(f"URL has a suspicious TLD: {url}")
        return True
    if check_suspicious_content(url):
        print(f"URL contains suspicious content: {url}")
        return True
    print(f"URL is likely safe: {url}")
    return False

# Example usage
if __name__ == "__main__":
    url = input("Enter the URL to check: ")
    is_phishing_link(url)