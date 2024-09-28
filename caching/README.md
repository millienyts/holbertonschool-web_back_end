# Caching - README

## Project Overview
This project explores different caching algorithms to enhance the performance of software applications. Caching systems are essential for optimizing data retrieval times by storing frequently accessed data in a faster storage layer. In this project, you will implement and compare several caching algorithms, including FIFO, LIFO, LRU, MRU, and LFU.

**By**: Millieny Torres

## Background
A caching system is designed to store a subset of data, enabling faster access and reducing the need for fetching the data from slower storage every time it’s needed. Caching systems have limitations like capacity and complexity in deciding which data to evict when the cache is full. 

In this project, you will work with different caching policies to understand their use cases and limitations.

## Learning Objectives
By the end of this project, you should be able to explain:
- What a caching system is.
- The concepts of FIFO, LIFO, LRU, MRU, and LFU caching.
- The purpose of a caching system.
- The limitations of a caching system.

## Resources
Read or watch the following to understand the concepts better:
- [Cache replacement policies - FIFO](#)
- [Cache replacement policies - LIFO](#)
- [Cache replacement policies - LRU](#)
- [Cache replacement policies - MRU](#)
- [Cache replacement policies - LFU](#)

## Requirements
### Python Scripts
- All scripts will be interpreted/compiled on Ubuntu 20.04 LTS using Python 3.9.
- Ensure all files end with a new line.
- The first line of all Python files should be: `#!/usr/bin/env python3`.
- Adhere to the pycodestyle style guide (version 2.5).
- All files must be executable.
- All modules and functions must have proper documentation.
- Use `wc` to test the length of your files.

### Repository
- **GitHub repository**: `holbertonschool-web_back_end`
- **Directory**: `caching`

## Caching System Classes

### 0. BasicCache
- **File**: `0-basic_cache.py`
- Implements a basic caching system without limits using a Python dictionary.  
- Methods:  
  - `put(self, key, item)`: Adds an item to the cache.
  - `get(self, key)`: Retrieves an item from the cache.

### 1. FIFOCache
- **File**: `1-fifo_cache.py`
- Implements a caching system with a First In, First Out (FIFO) policy.  
- If the cache exceeds the `MAX_ITEMS` limit, the first item added is discarded.
- Methods:  
  - `put(self, key, item)`
  - `get(self, key)`

### 2. LIFOCache
- **File**: `2-lifo_cache.py`
- Implements a caching system with a Last In, First Out (LIFO) policy.  
- If the cache exceeds the `MAX_ITEMS` limit, the last item added is discarded.
- Methods:  
  - `put(self, key, item)`
  - `get(self, key)`

### 3. LRUCache
- **File**: `3-lru_cache.py`
- Implements a Least Recently Used (LRU) caching policy.  
- If the cache exceeds the `MAX_ITEMS` limit, the least recently used item is discarded.
- Methods:  
  - `put(self, key, item)`
  - `get(self, key)`

### 4. MRUCache
- **File**: `4-mru_cache.py`
- Implements a Most Recently Used (MRU) caching policy.  
- If the cache exceeds the `MAX_ITEMS` limit, the most recently used item is discarded.
- Methods:  
  - `put(self, key, item)`
  - `get(self, key)`

## More Information
- **Parent class `BaseCaching`**: All classes must inherit from `BaseCaching`, which defines constants for the caching system and stores the cache data in a dictionari.
