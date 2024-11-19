# Developed by ls.saurabh

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

def scrape_website(url):
    try:
        # Add headers to prevent caching
        headers = {'Cache-Control': 'no-cache'}
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()  # Raise an exception for HTTP errors

        soup = BeautifulSoup(response.content, 'html.parser')
        links = soup.find_all('a', href=True)
        urls = [urljoin(url, link['href']) for link in links]

        return list(set(urls))  # Remove duplicate URLs
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return []
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
        return []

if __name__ == "__main__":
    while True:
        url = input("Enter a URL to scrape (or 'exit' to quit): ").strip()
        if url.lower() == 'exit':
            break

        scraped_urls = scrape_website(url)
        if scraped_urls:
            print("Scraped URLs:")
            for idx, scraped_url in enumerate(scraped_urls, 1):
                print(f"{idx}: {scraped_url}")
        else:
            print("No URLs found or an error occurred.")