from PyPDF2 import PdfWriter, PdfReader
import argparse
import os


class MergePDF:
    def __init__(self, pdf_array, filename):
        self.filename = filename
        self.pdf_array = pdf_array

    def merge(self):
        pdf_writer = PdfWriter()

        for pdf in self.pdf_array:
            pdf_reader = PdfReader(pdf)

            for page in pdf_reader.pages:
                pdf_writer.add_page(page)

        with open(f"{self.filename}.pdf", "wb") as out:
            pdf_writer.write(out)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--output", "-o", action="store", dest="filename", default="output"
    )
    parser.add_argument("pdf_array", nargs="*", action="store")
    args = parser.parse_args()

    if args.pdf_array[0] and args.pdf_array[0] in [".", "*"]:
        args.pdf_array = [
            f for f in os.listdir(".") if f.lower().endswith(".pdf")
        ]

    if not (len(args.pdf_array) >= 2):
        parser.error("[-] Need at least two pdfs as argument...")

    return args


def main():
    args = parse_args()
    pdf = MergePDF(args.pdf_array, args.filename)
    pdf.merge()


if __name__ == "__main__":
    main()
