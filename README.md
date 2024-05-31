# PDF Merger Script

This script merges all PDF files in a given directory into a single PDF file named `MergedPDF.pdf`. The order of merging is based on the alphabetical order of the file names. 

## Features

- Merges all PDF files in a specified directory.
- If no directory is specified, it uses the current directory.
- The merged PDF is saved as `MergedPDF.pdf` in the same directory.

## Requirements

- Python 3.x
- Virtual environment (venv)
- `requirements.txt` file with necessary dependencies

## Setup Instructions

### Step 1: Clone the Repository

Clone this repository to your local machine using:
```bash
git clone <repository-url>
```

### Step 2: Create a Virtual Environment

Navigate to the project directory and create a virtual environment:
```bash
cd <project-directory>
python3 -m venv venv
```

### Step 3: Activate the Virtual Environment

```bash
  source venv/bin/activate
```

### Step 4: Install Dependencies

Install the required dependencies using `requirements.txt`:
```bash
pip install -r requirements.txt
```

## Running the Script

### Basic Usage

To run the script, navigate to the project directory and execute:
```bash
python MergePdf.py
```

### Specifying a Directory

To merge PDF files from a specific directory, use the `--path` option:
```bash
python MergePdf.py --path /path/to/directory
```

If no directory is specified, the script will use the current working directory.

## Code Explanation

### Imports

- `os`: Provides a way to interact with the operating system, such as reading files in a directory.
- `click`: A package for creating command-line interfaces.
- `PyPDF2`: A library for working with PDF files.

### Functions

- `merge_pdf(path)`: 
  - Reads all PDF files from the specified directory.
  - Sorts the files alphabetically.
  - Merges the files using `PdfMerger` from `PyPDF2`.
  - Saves the merged PDF as `MergedPDF.pdf` in the same directory.

- `main(path)`:
  - Uses the `click` library to handle command-line options.
  - Calls the `merge_pdf` function with the specified path.

### Script Execution

- The script uses a `click.command` decorator to define the command-line interface.
- The `main` function is executed if the script is run as the main module.

## Example

To merge PDF files in the directory `/home/user/pdf_files`, run:
```bash
python mergePdf.py --path /home/user/pdf_files
```

## Authors

- Your Name - [Your GitHub](https://github.com/simo-corbo)