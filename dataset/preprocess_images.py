# coding: utf-8

from os import listdir
from os.path import basename, join 
import argparse
import cv2

def save_img(output_path, filename):
    desired_size = 400
    im = cv2.imread(filename)
    old_size = im.shape[:2] # old_size is in (height, width) format

    ratio = float(desired_size)/max(old_size)
    new_size = tuple([int(x*ratio) for x in old_size])

    # new_size should be in (width, height) format

    im = cv2.resize(im, (new_size[1], new_size[0]))

    delta_w = desired_size - new_size[1]
    delta_h = desired_size - new_size[0]
    top, bottom = delta_h//2, delta_h-(delta_h//2)
    left, right = delta_w//2, delta_w-(delta_w//2)

    color = [0, 0, 0]
    new_im = cv2.copyMakeBorder(im, top, bottom, left, right, cv2.BORDER_CONSTANT,
        value=color)

    cv2.imwrite(join(output_path, basename(filename)), new_im)


def main(dataset_path, output_path):
    for filename in listdir(dataset_path):
        print("processing: " + join(dataset_path, filename))
        save_img(output_path, join(dataset_path, filename))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Preprocess Dataset')

    parser.add_argument("-d", "--dataset", type=str, required=True,
                        dest="dataset_path", help="Dataset path")
    parser.add_argument("-o", "--output", type=str, required=True,
                        dest="output_path", help="Dataset path")

    args = parser.parse_args()
    main(args.dataset_path, args.output_path)
