import sys
import os
import warnings
import time
from urllib.request import urlopen, Request
from urllib.parse import urlparse
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

def get_base_name(source: str) -> str:
    if source.startswith('http'):
        path = urlparse(source).path
        base = os.path.basename(path)
        if not base and urlparse(source).netloc: return urlparse(source).netloc
        return os.path.splitext(base)[0]
    else:
        return os.path.splitext(os.path.basename(source))[0]

def main():
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} <URL or local file path>")
        sys.exit(1)

    source = sys.argv[1]
    soup = get_soup(source)
    
    b_tags = soup.find_all('b')
    count = len(b_tags)
    
    if not b_tags:
        print("no <b> tags found")
    else:
        for tag in b_tags:
            tag.name = 'blockquote'

        print("result: ", str(soup.prettify()))
        print("\n" * 3)
        
        base_name = get_base_name(source)
        out_path = f"{base_name}.blockquote.html"
        
        try:
            with open(out_path, 'w', encoding='utf-8') as f:
                f.write(str(soup.prettify()))
            print(f"write to: {out_path}")  
        except Exception as e:
            print(f"[error] failed to write: {e}")
            sys.exit(1)
        
if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"main() executed in {end_time - start_time:.4f} seconds")