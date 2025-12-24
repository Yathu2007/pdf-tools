# This application is meant to encrypt pdfs

from PyPDF2 import PdfWriter, PdfReader
import argparse
import os


class EncryptPDF:
    def __init__(self, input_path, output, password):
        self.file = PdfReader(input_path)
        self.pdf_writer = PdfWriter()

        if self.file.is_encrypted:
            return

        for page in self.file.pages:
            self.pdf_writer.add_page(page)

        self.pdf_writer.encrypt(password)

        with open(f"{output}.pdf", "wb") as f:
            self.pdf_writer.write(f)

    @classmethod
    def from_argv(cls):
        parser = argparse.ArgumentParser()
        parser.add_argument("-i", "--input", dest="input_path", required=True)
        parser.add_argument("-o", "--output", dest="output", required=True)
        parser.add_argument("-p", "--password", dest="password", required=True)

        args = parser.parse_args()

        input_path = os.path.expanduser(args.input_path)

        if not (os.path.exists(input_path)):
            parser.error("[-] Input file does not exist.")

        return cls(input_path, args.output, args.password)


if __name__ == "__main__":
    pdf_decrypter = EncryptPDF.from_argv()
