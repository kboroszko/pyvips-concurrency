import pandas as pd
import argparse
from pathlib import Path



def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--input", type=Path, help="results csv")
    return parser.parse_args()


def main(args):

    df = pd.read_csv(str(args.input), names=["n_proc", "reading", "writing", "idx"])

    print("1 proc")
    data = df.query("n_proc == 1")
    print(f"reading {data.reading.mean()} +/- {data.reading.std()}")
    print(f"writing {data.writing.mean()} +/- {data.writing.std()}")

    print("2 proc")
    data = df.query("n_proc == 2")
    print(f"reading {data.reading.mean()} +/- {data.reading.std()}")
    print(f"writing {data.writing.mean()} +/- {data.writing.std()}")


if __name__ == "__main__":
    args = parse_args()
    main(args)
