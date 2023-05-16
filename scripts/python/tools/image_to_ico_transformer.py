from PIL import Image
import os


def convert_to_ico(image_path):
    image = Image.open(image_path)

    # Calculate the output path by replacing the file extension
    base_path, extension = os.path.splitext(image_path)
    output_path = base_path + ".ico"

    image.save(output_path, format="ICO", quality=100, bitdepth=32)


if __name__ == "__main__":
    image_path = input("Enter the path of the image file: ")
    convert_to_ico(image_path)
    print("Conversion complete!")
