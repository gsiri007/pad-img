import argparse
from PIL import Image, ImageOps

def main():

    # command line argument parsing
    HELP_MESSAGE = '--- USAGE DETAILS ---'

    parser = argparse.ArgumentParser(description=HELP_MESSAGE)

    # required argument -> image file to edit
    parser.add_argument('image')

    # optional argumentsg
    parser.add_argument('-o', '--output', type=str, default=None)
    parser.add_argument('-b', '--background', type=str, default='black')

    args = parser.parse_args()

    INPUT_IMAGE = args.image
    OUTPUT_IMAGE = args.output
    IMAGE_BACKGROUND = args.background

    image_to_wallpaper(INPUT_IMAGE, IMAGE_BACKGROUND)

def image_to_wallpaper(image: str, bg_color: str):

    try:
        img = Image.open(image)
        scaled_width = img.size[0]
        scaled_height = 3000
        scaled_size = (scaled_width, scaled_height)
        scaled_img = img.resize(scaled_size, Image.Resampling.LANCZOS)

        pad_size = (6000, scaled_height)
        final_image = ImageOps.pad(scaled_img, pad_size, color=bg_color)

        final_image.show()

    except OSError as e:
        print(str(e))

if __name__ == "__main__":
    main()
