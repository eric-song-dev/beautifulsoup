# SWE262P-project

## Milestone 1

### Files

- `task1.py`: Reads an HTML file and saves a "prettified" version.
- `task2.py`: Prints all hyperlinks (`<a>` tags) from a file.
- `task3.py`: Prints all unique tags used in a document.
- `task4.py`: Prints all tags that have an `id` attribute.
- `task5.py`: Demonstrates a use case for the `find_parent()` method.
- `task6.py`: Replaces all `<b>` tags with `<blockquote>` tags and saves the result.
- `task7.py`: Adds `class="test"` to all `<p>` tags and saves the result.
- `task8.py`: Exercises the `.select()` method, which uses CSS selectors.

### Run

1.  Install BeautifulSoup:
    ```bash
    pip3 install beautifulsoup4
    ```

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
| task1.py | 95.6746 |
| task2.py | 65.8200 |
| task3.py | 55.3143 |
| task4.py | 70.9631 |
| task5.py | 55.2323 |
| task6.py | 53.2054 |
| task7.py | 53.5772 |
| task8.py | 52.1575 |

```bash
~/Courses/SWE262P/SWE262P-project (main*) » python3 task1.py Posts.xml                                                                ericsong@ERICS-MACBOOK-PRO
prettified HTML saved to: Posts.prettified.html
main() executed in 95.6746 seconds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/SWE262P-project (main*) » python3 task2.py Posts.xml                                                            1 ↵ ericsong@ERICS-MACBOOK-PRO
no hyperlinks found
main() executed in 65.8200 seconds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/SWE262P-project (main*) » python3 task3.py Posts.xml                                                            1 ↵ ericsong@ERICS-MACBOOK-PRO
...
main() executed in 55.3143 seconds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/SWE262P-project (main*) » python3 task4.py Posts.xml                                                            1 ↵ ericsong@ERICS-MACBOOK-PRO
...
main() executed in 70.9631 seconds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/SWE262P-project (main*) » python3 task5.py Posts.xml                                                                ericsong@ERICS-MACBOOK-PRO
no <body> tags found
main() executed in 55.2323 seconds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/SWE262P-project (main*) » python3 task6.py Posts.xml                                                                ericsong@ERICS-MACBOOK-PRO
no <b> tags found
main() executed in 53.2054 seconds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/SWE262P-project (main*) » python3 task7.py Posts.xml                                                                ericsong@ERICS-MACBOOK-PRO
no <p> tags found
main() executed in 53.5772 seconds
-----------------------------------------------------------------------------------------------------------------------------------------------------------------
~/Courses/SWE262P/SWE262P-project (main*) » python3 task8.py Posts.xml                                                                ericsong@ERICS-MACBOOK-PRO
no elements found for selector 'p a'
main() executed in 52.1575 seconds
```
