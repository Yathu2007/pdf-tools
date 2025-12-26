# This application is meant to rotate the pages in a pdf

from PyPDF2 import PdfReader, PdfWriter
import argparse


class RotatePDF:
    def __init__(self, pdf, rotation_angle, output_filename):
        self.pdf = pdf
        self.output_filename = output_filename
        self.rotation_angle = int(rotation_angle)

        self.pdf_reader = PdfReader(self.pdf)
        self.pdf_writer = PdfWriter()

        for page in self.pdf_reader.pages:
            page.rotate(self.rotation_angle)
            self.pdf_writer.add_page(page)

        self.pdf_writer.add_metadata(self.pdf_reader.metadata)

        with open(f"{self.output_filename}.pdf", "wb") as self.out:
            self.pdf_writer.write(self.out)

    @classmethod
    def from_argv(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "--output",
            "-o",
            action="store",
            dest="output_filename",
            default="document",
        )
        parser.add_argument("-i", "--input", dest="input_path", required=True)
        parser.add_argument(
            "-r",
            "--rotate",
            dest="rotation_angle",
            required=True,
            help="Rotate clockwise by n° (angle n Must be an increment of 90 deg)",
        )

        args = parser.parse_args()

        return cls(args.input_path, args.rotation_angle, args.output_filename)


if __name__ == "__main__":
    pdf_rotator = RotatePDF.from_argv()
