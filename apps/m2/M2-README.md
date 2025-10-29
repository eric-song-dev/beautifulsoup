# Milestone-2

### Files

- `task2.py`: Prints all hyperlinks (`<a>` tags) from a file.
- `task3.py`: Prints all unique tags used in a document.
- `task4.py`: Prints all tags that have an `id` attribute.

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

```bash
~/Courses/SWE262P/beautifulsoup/apps/m2 (main*) » python3 task2.py Posts.xml
no hyperlinks found
main() executed in 32.9881 seconds
(bs4) ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/beautifulsoup/apps/m2 (main*) » python3 task3.py Posts.xml
...
all unique tags (count: 2): ['posts', 'row']
    1. <posts>
    2. <row>
main() executed in 48.1168 seconds
(bs4) ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/beautifulsoup/apps/m2 (main*) » python3 task4.py Posts.xml
...
main() executed in 43.4722 seconds
(bs4) ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
```
