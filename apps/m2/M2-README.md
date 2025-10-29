# Milestone-2

### Files

- `task2.py`: Prints all hyperlinks (`<a>` tags) from a file.
- `task3.py`: Prints all unique tags used in a document.
- `task4.py`: Prints all tags that have an `id` attribute.
- `task6.py`: Replaces all `<b>` tags with `<blockquote>` tags and saves the result.

### Run

1.  Install BeautifulSoup as instructed in the `README.md`

2.  Run a Task:
    ```bash
    python3 taskx.py <URL or local file path> # it can be a HTML or XML file
    ```

### Large File Performance Test

Test File: `Posts.xml`  
Source: [askubuntu.com.7z](https://archive.org/download/stackexchange/askubuntu.com.7z)  
Size: 1.4 GB (uncompressed)

#### Result

| Filename | Execution Time (seconds) |
|---|---|
| task2.py | 32.9881 |
| task3.py | 48.1168 |
| task4.py | 43.4722 |

### API Modifications & New Files Reference (Original Source Code)

| File Path | Original Line Number | Brief Description of Change |
|-----------|--------------------------------------------------------|-----------------------------------------------|
| `.gitignore` | 122-124                                                | Modified: Added `.idea/` directory (IDE files) to the ignore list. |
| `apps/m2/M2-README.md` | 1                                                      | Modified: Added (`# Milestone-2`) sections. |
| `apps/m2/task2.py` | N/A, New file         | New file: Prints all hyperlinks (`<a>` tags) from a file. |
| `apps/m2/task3.py` | N/A, New file         | New file: Prints all unique tags used in a document. |
| `apps/m2/task4.py` | N/A, New file         | New file: Prints all tags that have an `id` attribute. |
| `apps/m2/task6.py` | N/A, New file         | New file: Replaces `<b>` tags with `<blockquote>` tags using a custom `SoupReplacer`. |
| `bs4/__init__.py` | 48-53, 88-93, 215-220                                  | Modified: 1. Added `'SoupReplacer'` to the `__all__` export list; 2. Imported `SoupReplacer` from `.replacer`; 3. Added `replacer` parameter to the `BeautifulSoup` constructor and assigned it to `self.replacer`. |
| `bs4/builder/_htmlparser.py` | 151-156, 209-214                                        | Modified: Added tag replacement logic using `self.soup.replacer` for both start tags and end tags. |
| `bs4/replacer.py` | N/A, New file         | New file: Defines the `SoupReplacer` class. |
| `bs4/tests/test_replacer.py` | N/A, New file         | New file: Unit tests for `SoupReplacer`. |
