from html.parser import HTMLParser
from urllib.request import urlopen
from urllib import parse

def extract_links(url, max_pages):
    links = []
    pages_to_visit = [url]
    visited_pages = 0
    found_word = False

    while visited_pages < max_pages and pages_to_visit and not found_word:
        visited_pages += 1
        current_url = pages_to_visit.pop(0)

        try:
            html_content = fetch_html_content(current_url)
            extracted_links = parse_links(html_content)
        except Exception as e:
            print(f"Error fetching or parsing URL: {current_url}")
            print(e)
            continue

        links.extend(extracted_links)
        pages_to_visit.extend(extracted_links)

    return links

def fetch_html_content(url):
    response = urlopen(url)
    if response.getheader('Content-Type') != 'text/html':
        return None

    html_bytes = response.read()
    html_string = html_bytes.decode("utf-8")
    return html_string

def parse_links(html_content):
    parser = HTMLParser()
    parser.feed(html_content)
    return parser.links

if __name__ == "__main__":
    starting_url = "http://vulnweb.com"
    max_pages = 10

    extracted_links = extract_links(starting_url, max_pages)
    print(extracted_links)
