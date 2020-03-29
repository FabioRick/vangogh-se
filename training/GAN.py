# coding: utf-8

import argparse


def main(dataset):
    pass


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='GAN Trainning')

    parser.add_argument("-d", "--dataset", type=str, required=True,
                        dest="dataset", help="Dataset filename")

    args = parser.parse_args()
    main(args.dataset)
