import argparse
from PIL import Image, ImageOps

def main():
    # command line argument parsing
    HELP_MESSAGE = '--- USAGE DETAILS ---'

    parser = argparse.ArgumentParser(description=HELP_MESSAGE)

    # required argument -> image file to edit
    parser.add_argument('image')

    # optional argumentsg
    parser.add_argument('-o', '--output', type=str, default='output')
    parser.add_argument('-b', '--background', type=str, default='black')
    parser.add_argument('-f', '--format', type=str, default=None)

    args = parser.parse_args()

    INPUT_IMAGE = args.image
    OUTPUT_IMAGE = args.output
    BACKGROUND_COLOR = args.background
    OUTPUT_FORMAT = args.format

    # creating the wallpaper
    try:
        img = Image.open(INPUT_IMAGE)

        pad_size = (6000, 3000)
        final_image = ImageOps.pad(img, pad_size, color=BACKGROUND_COLOR)

        if OUTPUT_FORMAT is None:
            final_image.save(f"{OUTPUT_IMAGE}.{str(img.format).lower()}", img.format)
        else:
            final_image.save(f"{OUTPUT_IMAGE}.{OUTPUT_FORMAT.lower()}", OUTPUT_FORMAT)

    except OSError as e:
        print(str(e))

if __name__ == "__main__":
    main()
