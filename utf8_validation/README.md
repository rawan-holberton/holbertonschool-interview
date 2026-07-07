# UTF-8 Validation

## Description

This project implements a method to determine whether a given dataset represents a valid UTF-8 encoding.

UTF-8 is a variable-length character encoding standard where each character can be represented using **1 to 4 bytes**. The goal of this project is to analyze a list of integers, where each integer represents one byte of data, and verify if the sequence follows the UTF-8 encoding rules.

## Requirements

- All files are interpreted/compiled on **Ubuntu 14.04 LTS** using **Python 3.4.3**
- All files must:
  - Start with the shebang:
    ```python
    #!/usr/bin/python3
    ```
  - End with a new line
  - Be executable
  - Follow **PEP 8** style guidelines (version 1.7.x)
- A `README.md` file is required at the root of the project

## Project Structure
utf8_validation/
│
├── 0-validate_utf8.py # UTF-8 validation algorithm
├── 0-main.py # Test file
└── README.md # Project documentation

## Task

### 0. UTF-8 Validation

Implement the function:

```python
def validUTF8(data)

### Parameters
data:
A list of integers
Each integer represents one byte of UTF-8 data
Only the 8 least significant bits of each integer should be considered
Return
True if data represents a valid UTF-8 encoding
False otherwise
UTF-8 Encoding Rules

A UTF-8 character can be encoded using:

Number of bytes	Format
1 byte	0xxxxxxx
2 bytes	110xxxxx 10xxxxxx
3 bytes	1110xxxx 10xxxxxx 10xxxxxx
4 bytes	11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Continuation bytes must always start with:

10xxxxxx

The algorithm checks that every byte sequence respects these encoding rules.

## Usage

Run the test file:

./0-main.py

Example:

data = [65]
print(validUTF8(data))

Output:

True

Another example:

data = [229, 65, 127, 256]
print(validUTF8(data))

Output:

False

#Author
Made by Rawan for Holberton School project UTF-8 Validation
