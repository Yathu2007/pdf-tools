# This application is meant to create a pdf from
# the images provided as arguments into this script

from PIL import Image, ImageOps
import argparse
import os


class CreatePDF:
    def __init__(self, images_array, output_filename):
        self.output_filename = output_filename
        # Open the images, convert to RGB, and fix its orientation
        self.images_array = [
            self.fix_orientation(Image.open(image).convert("RGB"))
            for image in images_array
        ]

        # Get the first image
        self.image1 = self.images_array.pop(0)

        # Save the first image as the pdf and append all other images to the pdf
        self.image1.save(
            f"{self.output_filename}.pdf",
            save_all=True,
            append_images=self.images_array,
        )

    def fix_orientation(self, image):
        """Fix the orientation of images to keep to the defaults"""
        return ImageOps.exif_transpose(image)

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
        parser.add_argument("images_array", nargs="*", action="store")
        args = parser.parse_args()

        if len(args.images_array) >= 1:
            if (args.images_array[0] == ".") or (args.images_array[0] == "*"):
                args.images_array = os.listdir(path=".")
        else:
            print("[-] Need at least one image as argument...")
            exit()

        return cls(args.images_array, args.output_filename)


if __name__ == "__main__":
    pdf_maker = CreatePDF.from_argv()
