from PyPDF2 import PdfReader
import os
import argparse
from PIL import Image


class ExtractPDF:
    def __init__(self, input_path, output_folder):
        self.pdf = input_path
        self.out = output_folder

    def extract(self):
        self.pdf_reader = PdfReader(self.pdf)

        for self.page_num in range(len(self.pdf_reader.pages)):
            self.convert()

    def convert(self):
        self.page = self.pdf_reader.pages[self.page_num]

        filename = os.path.join(self.out, f"Image {self.page_num + 1}")
        xObject = self.page["/Resources"]["/XObject"].get_object()

        for obj in xObject:
            if xObject[obj]["/Subtype"] == "/Image":
                size = (xObject[obj]["/Width"], xObject[obj]["/Height"])
                data = xObject[obj].get_data()
                if xObject[obj]["/ColorSpace"] == "/DeviceRGB":
                    mode = "RGB"
                else:
                    mode = "P"

                if xObject[obj]["/Filter"] == "/FlateDecode":
                    img = Image.frombytes(mode, size, data)
                    img.save(f"{filename}.png")
                elif xObject[obj]["/Filter"] == "/DCTDecode":
                    with open(f"{filename}.jpg", "wb") as img:
                        img.write(data)
                elif xObject[obj]["/Filter"] == "/JPXDecode":
                    img = open(obj[1:] + ".jp2", "wb")
                    img.write(data)
                    img.close()


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", dest="input_path", required=True)
    parser.add_argument(
        "--output",
        "-o",
        action="store",
        dest="output_folder",
        required=True,
    )

    args = parser.parse_args()

    if not (os.path.exists(args.input_path)):
        parser.error("[-] Input file does not exist.")

    if not (os.path.exists(args.output_folder)):
        parser.error("[-] Output folder does not exist.")

    return (args.input_path, args.output_folder)


def main():
    args = parse_args()
    pdf = ExtractPDF(*args)
    pdf.extract()


if __name__ == "__main__":
    main()
