import requests

def get_wayback_urls(domain):
    url = "https://web.archive.org/cdx/search/cdx"
    params = {
        "url": f"*.{domain}/*",
        "output": "text",
        "fl": "original",
        "collapse": "urlkey"
    }
    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.text.strip().split("\n")
    return []

if __name__ == "__main__":
    domain = "tata.com"
    urls = get_wayback_urls(domain)
    for url in urls:
        print(url)
