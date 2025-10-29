import sys
import warnings
import time
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def get_soup(source: str) -> BeautifulSoup:
    content = ""
    try:
        if source.startswith('http'):
            req = Request(source, headers={'User-Agent': 'Mozilla/5.0'})
            with urlopen(req) as response: content = response.read()
        else:
            with open(source, 'r', encoding='utf-8') as f: content = f.read()
    except Exception as e:
        print(f"[error] could not read source '{source}'.\n{e}", file=sys.stderr)
        sys.exit(1)
    return BeautifulSoup(content, 'html.parser')

def main():
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} <URL or local file path>")
        sys.exit(1)

    source = sys.argv[1]
    soup = get_soup(source)
    
    first_body = soup.find('body')
    
    if first_body:
        print("found first body")

        parent_html = first_body.find_parent('html')
        if parent_html:
            parent_id = parent_html.get('id', 'N/A')
            parent_class = parent_html.get('class', ['N/A'])
            print(f"found its parent <html> tag: name: <{parent_html.name}>, id: {parent_id}, class: {parent_class}")
        else:
            print("could not find a <html> parent for the first <body> tag")
    else:
        print("no <body> tags found")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"main() executed in {end_time - start_time:.4f} seconds")