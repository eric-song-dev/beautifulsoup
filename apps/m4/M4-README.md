# Milestone-4

## Part-1: Git Diff

```git

```

## Part-2: Technical Implementation

### The Problem with List Collection
Traditionally, to process every node in a tree, a developer might perform a recursive search or use `find_all()`. `find_all()` traverses the entire tree and collects matching nodes into a standard Python `list` before returning.

For very large files (e.g., gigabyte-scale XML), creating a list of all nodes consumes a significant amount of memory ($O(N)$ space complexity, where $N$ is the number of nodes).

### The Generator Solution
I implemented `__iter__` in the `BeautifulSoup` class to return a **generator** (specifically, by aliasing the existing `descendants` property).

```python
# In bs4/__init__.py
def __iter__(self):
    return self.descendants
```

This leverages the linked-list structure (`next_element`) maintained by BeautifulSoup during parsing. The iteration logic moves from one node to the next in real-time without pre-calculating or storing a separate collection of nodes.

### Benefits

1.  **Memory Efficiency**: The memory footprint for iteration is now $O(1)$ (constant space), regardless of the file size.
2.  **Performance**: Processing can begin immediately. There is no initial delay waiting for a full list to be constructed.
3.  **Clean API**: The user interface is simplified to a standard Python idiom:
    ```python
    for node in soup:
        process(node)
    ```

## Comparison: Method 1 vs. Method 2

### Method 1: Manual Traversal

```python
def __iter__(self):
    yield self
    node = self.next_element
    while node:
        yield node
        node = node.next_element
```

  * **Pros:** Includes the root `soup` object in the iteration loop.
  * **Cons:** Duplicates existing traversal logic and violates standard Python container semantics (iterating a container typically yields its contents, not the container itself).

### Method 2: Delegation

```python
def __iter__(self):
    return self.descendants
```

  * **Pros:** Clean implementation, follows the DRY (Don't Repeat Yourself) principle, and reuses the robust `Tag.descendants` logic.

**Decision:** I chose **Method 2** to maintain consistency with the library's design and ensure better maintainability.

## Comparison: Milestone 1 vs. Milestone 4

### Milestone 1 Style (List-based)

```python
all_tags = soup.find_all(True) 
for tag in all_tags:
    print(tag)
```

  * **Cons:** High memory usage, must wait for list creation

### Milestone 4 Style (Stream-based)

```python
for node in soup:
    print(node)
```

  * **Pros:** Low memory usage, immediate execution

## Conclusion

This enhancement aligns BeautifulSoup with modern Pythonic standards for handling large datasets, promoting "lazy evaluation" and efficient resource management.

## Part-3: Demo

### Files

- `iteration_demo.py`: Iterate over all children of this `Tag` in a breadth-first sequence.

### Run

1.  Install BeautifulSoup as instructed in the `README.md`

2.  Run a Task:
    ```bash
    python3 iteration_demo.py <URL or local file path> # it can be a HTML or XML file
    
    # example
    python3 iteration_demo.py https://www.example.com/
    ```