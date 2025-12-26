from PIL import Image, ImageOps
import argparse
import os

SUPPORTED_EXTENSIONS = (".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tiff")


class CreatePDF:
    def __init__(self, images, output_filename):
        self.images = images
        self.output_filename = output_filename

    def fix_orientation(self, image):
        """Fix the orientation of images to keep to the defaults"""
        return ImageOps.exif_transpose(image)

    def create(self):
        if not self.images:
            raise ValueError("No images provided")

        # Open the images, convert to RGB, and fix its orientation
        images_rgb = [
            self.fix_orientation(Image.open(image).convert("RGB"))
            for image in self.images
        ]

        # Get the first image
        image1 = images_rgb.pop(0)

        # Save the first image as the pdf and append all other images to the pdf
        image1.save(
            f"{self.output_filename}.pdf",
            save_all=True,
            append_images=images_rgb,
        )


def parse_args():
    parser = argparse.ArgumentParser(
        description="Create a PDF from one or more images"
    )
    parser.add_argument(
        "images",
        nargs="*",
        action="store",
        help="Image files to include in the PDF",
    )
    parser.add_argument(
        "--output",
        "-o",
        action="store",
        dest="output",
        default="document",
        help="Output PDF filename (without .pdf)",
    )

    args = parser.parse_args()

    if not args.images:
        parser.error("At least one image must be provided")

    if args.images[0] in [".", "*"]:
        args.images = [
            f
            for f in os.listdir(".")
            if f.lower().endswith(SUPPORTED_EXTENSIONS)
        ]

    return args


def main():
    args = parse_args()
    pdf = CreatePDF(args.images, args.output)
    pdf.create()


if __name__ == "__main__":
    main()
