import argparse
import time
from pathlib import Path

from process import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, help="input image")
    return parser.parse_args()


def main(args):
    start = time.perf_counter()
    with open(args.input, "rb") as stream:
        buf = stream.read()
    img = read_bytes(buf)
    img_parsed = time.perf_counter()
    output_jpeg = write_bytes_jpeg(img)
    img_saved_jpeg = time.perf_counter()

    print(
        f"1,"
        f"{img_parsed - start},"
        f"{img_saved_jpeg-img_parsed},"
    )


if __name__ == "__main__":
    args = parse_args()
    main(args)
