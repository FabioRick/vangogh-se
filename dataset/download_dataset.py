# coding: utf-8

import argparse
import numpy as np
import pandas as pd
import urllib.request
from os.path import join


def main(dataset):
    data = pd.read_csv(dataset)
    for index, row in data.iterrows():
        if "Gogh" in row['Artist']:
            text = str(index) + "\t" + row['ImageURL'] + "\t"
            try:
                urllib.request.urlretrieve(row['ImageURL'], join("images", row['ImageSHA1'] + ".jpg"))
                text += "OK"
            except Exception:
                text += "FAIL"
            print(text)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Download Dataset')

    parser.add_argument("-d", "--dataset", type=str, required=True,
                        dest="dataset", help="Dataset filename")

    args = parser.parse_args()
    main(args.dataset)
