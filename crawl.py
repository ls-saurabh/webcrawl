import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import time

visited_urls = set()

def crawl_website(url, depth=2):
    if depth == 0:
        return
    
    if url in visited_urls:
        return

    visited_urls.add(url)
    
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"Failed to retrieve {url}: {e}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')

    links = soup.find_all('a', href=True)
    for link in links:
        href = link.get('href')
        full_url = urljoin(url, href)
        if full_url.startswith('http'):
            print(full_url)
            # Delay to avoid overwhelming the server
            time.sleep(1)
            crawl_website(full_url, depth - 1)

# Example usage
url = input("Enter URL: ")
crawl_website(url)