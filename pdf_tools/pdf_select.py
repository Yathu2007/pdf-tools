from PyPDF2 import PdfReader, PdfWriter
import argparse


class SelectPDFPages:
    def __init__(self, input_filename, page_range, output_filename):
        self.input_filename = input_filename
        self.page_range = page_range
        self.output_filename = output_filename

    def select(self):
        pdf_reader = PdfReader(self.input_filename)
        pdf_writer = PdfWriter()
        page_nums = self.get_page_nums(self.page_range)

        for page_num in page_nums:
            pdf_writer.add_page(pdf_reader.pages[page_num])

        with open(f"{self.output_filename}.pdf", "wb") as out:
            pdf_writer.write(out)

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


def parse_args():
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

    return args


def main():
    args = parse_args()
    pdf = SelectPDFPages(*args)
    pdf.select()


if __name__ == "__main__":
    main()
