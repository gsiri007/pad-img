import sys
import argparse

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

    print(INPUT_IMAGE, OUTPUT_IMAGE, IMAGE_BACKGROUND)

if __name__ == "__main__":
    main()
