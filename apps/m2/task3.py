import sys
import os
import warnings
import time
import re  # Import regex
from urllib.request import urlopen, Request
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning, SoupStrainer

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

def get_soup(source: str, strainer: SoupStrainer = None) -> BeautifulSoup:
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
    
    return BeautifulSoup(content, 'html.parser', parse_only=strainer)

def main():
    if len(sys.argv) != 2:
        print(f"usage: python3 {sys.argv[0]} <URL or local file path>")
        sys.exit(1)

    source = sys.argv[1]

    # create a SoupStrainer to parse any tag
    all_tags_strainer = SoupStrainer(name=re.compile(r'.+'))

    soup = get_soup(source, strainer=all_tags_strainer)
    
    all_tags = [tag.name for tag in soup.find_all(True)]
    unique_tags = sorted(set(all_tags))

    if not all_tags:
        print("no tags found")
    else:
        print(f"all tags (count: {len(all_tags)}):")
        for idx, tag_name in enumerate(all_tags, start=1):
            print(f"{idx: >5}. <{tag_name}>")

    print("\n" * 3)

    if not unique_tags:
        print("no unique tags found")
    else:
        print(f"all unique tags (count: {len(unique_tags)}):", unique_tags)
        for idx, tag_name in enumerate(unique_tags, start=1):
            print(f"{idx: >5}. <{tag_name}>")

if __name__ == "__main__":
    start_time = time.time()
    main()
    end_time = time.time()
    print(f"main() executed in {end_time - start_time:.4f} seconds")
