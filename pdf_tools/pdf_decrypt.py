# This application is meant to decrypt pdfs

from PyPDF2 import PdfWriter, PdfReader
import argparse
import os


class DecryptPDF:
    def __init__(self, input_path, output, password):
        self.file = PdfReader(input_path)
        self.pdf_writer = PdfWriter()

        if not self.file.is_encrypted:
            return

        self.file.decrypt(password)

        for page in self.file.pages:
            self.pdf_writer.add_page(page)

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
    pdf_decrypter = DecryptPDF.from_argv()
