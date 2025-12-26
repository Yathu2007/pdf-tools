from PyPDF2 import PdfWriter, PdfReader
import argparse
import os


class DecryptPDF:
    def __init__(self, input_path, output, password):
        self.input_path = input_path
        self.output = output
        self.password = password

    def decrypt(self):
        file = PdfReader(self.input_path)
        pdf_writer = PdfWriter()

        if not file.is_encrypted:
            print("[*] File is not encrypted.")
            return

        result = file.decrypt(self.password)

        if result == 0:
            raise ValueError("[-] Incorrect password!")

        for page in file.pages:
            pdf_writer.add_page(page)

        with open(f"{self.output}.pdf", "wb") as f:
            pdf_writer.write(f)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input_path", required=True)
    parser.add_argument("-o", "--output", dest="output", required=True)
    parser.add_argument("-p", "--password", dest="password", required=True)

    args = parser.parse_args()

    input_path = os.path.expanduser(args.input_path)

    if not (os.path.exists(input_path)):
        parser.error("[-] Input file does not exist.")

    return (input_path, args.output, args.password)


def main():
    args = parse_args()
    pdf = DecryptPDF(*args)
    pdf.decrypt()


if __name__ == "__main__":
    main()
