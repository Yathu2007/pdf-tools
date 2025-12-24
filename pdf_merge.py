# This application is meant to merge multiple pdfs

from PyPDF2 import PdfWriter, PdfReader
import sys
import argparse
import os


class MergePDF:
    def __init__(self, pdf_array, filename):
        self.filename = filename
        self.pdf_array = pdf_array
        self.pdf_writer = PdfWriter()

        for self.pdf in self.pdf_array:
            self.pdf_reader = PdfReader(self.pdf)

            for self.page_num in range(len(self.pdf_reader.pages)):
                self.pdf_writer.add_page(self.pdf_reader.pages[self.page_num])

        with open(f"{self.filename}.pdf", "wb") as self.out:
            self.pdf_writer.write(self.out)

    @classmethod
    def from_argv(cls, argv_array):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--output", "-o", action="store", dest="filename", default="output"
        )
        parser.add_argument("pdf_array", nargs="*", action="store")
        args = parser.parse_args(argv_array)

        if (args.pdf_array[0] == ".") or (args.pdf_array[0] == "*"):
            args.pdf_array = os.listdir(path=".")
        elif not (len(args.pdf_array) >= 2):
            print("[-] Need at least two pdfs as argument...")
            exit()

        return cls(args.pdf_array, args.filename)


if __name__ == "__main__":
    pdf_merger = MergePDF.from_argv(sys.argv[1:])
