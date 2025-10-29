# Milestone-2

## Part-1

### Files

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

## Part-2

### m1 task1
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.prettify | bs4/element.py | L2601 |

### m1 task2
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.find_all | bs4/element.py | L2715 |

### m1 task3
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.find_all | bs4/element.py | L2715 |
| Tag.name | bs4/element.py | L1648 |

### m1 task4
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.find_all | bs4/element.py | L2715 |
| Tag.name | bs4/element.py | L1648 |

### m1 task5
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.find_parent | bs4/element.py | L992 |
| Tag.get | bs4/element.py | L2160 |

### m1 task6
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.find_all | bs4/element.py | L2715 |
| Tag.name | bs4/element.py | L1648 |
| Tag.prettify | bs4/element.py | L2601 |

### m1 task7
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.find_all | bs4/element.py | L2715 |
| Tag.prettify | bs4/element.py | L2601 |

### m1 task8
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| Tag.select | bs4/element.py | L2799 |
| Tag.name | bs4/element.py | L1648 |
| Tag.get | bs4/element.py | L2160 |
| Tag.get_text | bs4/element.py | L524 |

### m2 task2
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| SoupStrainer | bs4/filter.py | L313 |
| Tag.find_all | bs4/element.py | L2715 |

### m2 task3
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| SoupStrainer | bs4/filter.py | L313 |
| Tag.find_all | bs4/element.py | L2715 |
| Tag.name | bs4/element.py | L1648 |

### m2 task4
| API | Source File | Line |
|---------------|--------------|------|
| BeautifulSoup.\_\_init\_\_ | bs4/\_\_init\_\_.py | L133 |
| SoupStrainer | bs4/filter.py | L313 |
| Tag.find_all | bs4/element.py | L2715 |
| Tag.name | bs4/element.py | L1648 |

## Part-3

### Files

- `task6.py`: Replaces all `<b>` tags with `<blockquote>` tags and saves the result.

### Run

1.  Install BeautifulSoup as instructed in the `README.md`

2.  Run a Task:
    ```bash
    python3 taskx.py <URL or local file path> # it can be a HTML or XML file
    
    # example
    python3 task6.py https://www.w3schools.com/tags/tag_b.asp
    ```