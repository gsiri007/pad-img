import argparse
from PIL import Image, ImageOps
import os

def main():
    # command line argument parsing
    HELP_MESSAGE = '''
                      bg-wall is a utility that converts your portrait 
                      images to a wallpaper with a specific background color.
                   '''

    parser = argparse.ArgumentParser(description=HELP_MESSAGE)

    # required argument -> image file to edit
    parser.add_argument('image')

    # optional arguments
    parser.add_argument('-o', '--output', type=str, default='output', help='output path/filename')
    parser.add_argument('-p', '--pad-color', type=str, default='black', help='background color')
    parser.add_argument('-f', '--format', type=str, default=None, help='output format [png, jpeg]')

    args = parser.parse_args()


    INPUT_IMAGE = args.image
    OUTPUT_IMAGE = args.output
    PAD_COLOR = args.background
    OUTPUT_FORMAT = args.format

    # checking if inside a docker container and setting the paths
    if os.environ.get("AM_I_IN_A_DOCKER_CONTAINER") == 'YES':
        INPUT_IMAGE = f"/tmp/{args.image}"
        OUTPUT_IMAGE = f"/tmp/{args.output}"

    # creating the wallpaper
    try:
        img = Image.open(INPUT_IMAGE)

        pad_size = (6000, 3000)
        final_image = ImageOps.pad(img, pad_size, color=PAD_COLOR)


        if OUTPUT_FORMAT is None:
            final_image.save(f"{OUTPUT_IMAGE}.{str(img.format).lower()}", img.format)
        else:
            final_image.save(f"{OUTPUT_IMAGE}.{OUTPUT_FORMAT.lower()}", OUTPUT_FORMAT)

    except OSError as e:
        print(str(e))

if __name__ == "__main__":
    main()
