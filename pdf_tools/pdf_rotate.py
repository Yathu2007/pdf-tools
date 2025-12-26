from PyPDF2 import PdfReader, PdfWriter
import argparse


class RotatePDF:
    def __init__(self, pdf, rotation_angle, output_filename):
        self.pdf = pdf
        self.output_filename = output_filename
        self.rotation_angle = int(rotation_angle)

    def rotate(self):
        pdf_reader = PdfReader(self.pdf)
        pdf_writer = PdfWriter()

        for page in pdf_reader.pages:
            page.rotate(self.rotation_angle)
            pdf_writer.add_page(page)

        pdf_writer.add_metadata(pdf_reader.metadata)

        with open(f"{self.output_filename}.pdf", "wb") as out:
            pdf_writer.write(out)


def parse_args():
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

    return args


def main():
    args = parse_args()
    pdf = RotatePDF(*args)
    pdf.rotate()


if __name__ == "__main__":
    main()
