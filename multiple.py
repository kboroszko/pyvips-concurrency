import argparse
import multiprocessing
import time
from pathlib import Path

from process import *


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, help="input image")
    parser.add_argument("-n", "--n_proc", type=int, help="number of parallel processes")
    return parser.parse_args()


def main(args, idx, barrier):

    with open(args.input, "rb") as stream:
        buf = stream.read()

    barrier.wait()

    proc_start = time.perf_counter()
    img = read_bytes(buf)
    img_parsed = time.perf_counter()
    output_jpeg = write_bytes_jpeg(img)
    img_saved_jpeg = time.perf_counter()

    print(
        f"{args.n_proc},"
        f"{img_parsed - proc_start},"
        f"{img_saved_jpeg - img_parsed},"
        f"{idx}"
    )


if __name__ == "__main__":
    args = parse_args()

    barrier = multiprocessing.Barrier(args.n_proc)

    processes = []
    for i in range(args.n_proc - 1):
        p = multiprocessing.Process(target=main, args=(args, i + 1, barrier))
        p.start()
        processes.append(p)

    main(args, 0, barrier)

    for p in processes:
        p.join()
