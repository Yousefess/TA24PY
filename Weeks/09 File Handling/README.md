# File Handling

## [**`Introduction to File Handling and IO`**](https://github.com/Yousefess/TA24PY/blob/main/Weeks/09%20File%20Handling/Notebooks/01%20Introduction%20to%20File%20Handling%20and%20IO.ipynb)

- What are files?
  - Text Files
  - Binary Files
- Why is file handling important?
- Basic file handling operations
  - Open
  - Read
  - Write
  - Close
  - Demonstration of opening a file in Python
- The `open()` function and its modes
  - Description of different modes
  - Code examples showing how to open files in different modes
- Text files vs. binary files
  - Distinctions between handling text and binary files
  - Use cases for each type
- The importance of closing files and using `with` statements for safety
  - Explanation of why files need to be closed
  - Introduction to the `with` statement and context managers

## [**`Reading from Files`**](https://github.com/Yousefess/TA24PY/blob/main/Weeks/09%20File%20Handling/Notebooks/02%20Reading%20from%20Files.ipynb)

- Opening Files for Reading ('r' mode)
  - How to Open a File Using `open()`
- The `read()`, `readline()`, and `readlines()` Methods
  - The `read()` Method
  - The `readline()` Method
  - The `readlines()` Method
- Iterating Over File Objects Line by Line
  - Efficiency Benefits
- Working with File Paths (Absolute vs. Relative)
  - Understanding File Paths
  - Platform-Independent File Paths


## [**`Writing to Files`**](https://github.com/Yousefess/TA24PY/blob/main/Weeks/09%20File%20Handling/Notebooks/03%20Writing%20to%20Files.ipynb)

- Opening Files for Writing
  - Using `open()` to Create File Objects for Writing
  - The Difference Between Writing to a New File vs. an Existing File
- The `write()` Method
  - The Concept of Strings and How They Are Written to Files
- The `writelines()` Method
  - The Difference between `write()` and `writelines()`
- Truncating and Overwriting vs. Appending
  - Append to the End of a File with Mode `'a'`
  - Potential Risks of Overwriting Data and How to Prevent It
- File Buffering and Flushing
- Practical Examples
  - Example: Writing Log Data to a File
  - Example: Generating and Saving a Report
