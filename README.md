# webcrawl

## Web Crawler

This is a simple web crawler implemented in Python using requests and BeautifulSoup. It recursively follows links from a given starting URL and prints out all the unique HTTP links it encounters.

**Features**

Recursively crawls websites to discover links.Avoids revisiting URLs to prevent infinite loops.Handles HTTP request errors gracefully.Supports configurable depth to limit crawling depth.

**Requirements**

Python 3.x
requests
beautifulsoup4


Install the dependencies using:

```
pip install requests beautifulsoup4
```

**Usage**

Clone the repository:
```
git clone https://github.com/ls-saurabh/webcrawl.git
```

```
cd webcrawl
```

Run the script:
 ```
python crawl.py
```