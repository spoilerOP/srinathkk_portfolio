import requests

def get_wayback_urls(domain):
    url = "https://web.archive.org/cdx/search/cdx"
    params = {
        "url": f"*.{domain}/*",
        "output": "text",
        "fl": "original",
        "collapse": "urlkey"
    }
    
    try:
        # Send GET request to Wayback Machine API
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx and 5xx)
        
        # Process the response
        urls = response.text.strip().split("\n")
        print(f"Found {len(urls)} URLs for domain '{domain}':")
        for i, link in enumerate(urls, 1):
            print(f"{i}: {link}")
        
        return urls
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []

if __name__ == "__main__":
    domain = "innspark.in"
    wayback_urls = get_wayback_urls(domain)
