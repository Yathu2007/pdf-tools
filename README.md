# PDF Tools

A collection of Python utilities for common PDF operations, including creating PDFs from images, extracting pages to images, merging, encrypting, decrypting, rotating, and selecting pages.

## Included Tools

| Tool           | Description                           |
| -------------- | ------------------------------------- |
| pdf_create.py  | Create a PDF from a set of images     |
| pdf_extract.py | Convert PDF pages into images         |
| pdf_merge.py   | Merge multiple PDF files              |
| pdf_encrypt.py | Encrypt a PDF with a password         |
| pdf_decrypt.py | Remove PDF password protection        |
| pdf_rotate.py  | Rotate PDF pages                      |
| pdf_select.py  | Extract selected pages into a new PDF |

## Setup

1. Clone this repository

```bash
git clone https://github.com/Yathu2007/pdf-tools.git
```

2.  Change the working directory

```bash
cd .\pdf-tools\
```

3.  Install the package and dependencies

```bash
pip install .
```

## Usage

After installation, you can run the tools from the command line:

```bash
pdf-merge -o output.pdf file1.pdf file2.pdf
pdf-decrypt -i protected.pdf -o decrypted -p password123
```
