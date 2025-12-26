# This application is meant to select pages from a pdf

from PyPDF2 import PdfReader, PdfWriter
import argparse


class SelectPDFPages:
    def __init__(self, input_filename, page_range, output_filename):
        self.pdf_reader = PdfReader(input_filename)
        self.pdf_writer = PdfWriter()
        self.page_nums = self.get_page_nums(page_range)

        for page_num in self.page_nums:
            self.pdf_writer.add_page(self.pdf_reader.pages[page_num])

        with open(f"{output_filename}.pdf", "wb") as self.out:
            self.pdf_writer.write(self.out)

    def get_page_nums(self, page_range: str):
        """
        Return the indices of the pages to select using the string page_range
        """

        temp = page_range.split(",")
        nums = []

        for item in temp:
            if "-" in item:
                start, end = item.split("-")
                nums.extend([i - 1 for i in range(int(start), int(end) + 1)])
            else:
                nums.append(int(item) - 1)

        return nums

    @classmethod
    def from_argv(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--input",
            "-i",
            action="store",
            dest="input_filename",
            required=True,
        )
        parser.add_argument(
            "--pages",
            "-p",
            action="store",
            dest="pages",
            required=True,
            help="As a range, comma separated page numbers, or single page number",
        )
        parser.add_argument(
            "--output",
            "-o",
            action="store",
            dest="output_filename",
            default="output",
        )

        args = parser.parse_args()

        return cls(args.input_filename, args.pages, args.output_filename)


if __name__ == "__main__":
    pdf_extracter = SelectPDFPages.from_argv()
