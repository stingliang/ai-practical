# -*- coding: utf-8 -*-

# @File        : helloworld.py
# @CreateDate  : 2021-10-19
# @Author      : stingliang
# @Github      : https://github.com/stingliang

import cv2 as cv
import sys
import os
from loguru import logger


def save_image(img_path):
    dir_path = os.path.split(img_path)[0]
    raw_name = os.path.basename(img_path)
    processed_name = str(raw_name).split('.')[0] + '.png'
    img = cv.imread(cv.samples.findFile(img_path))
    if img is None:
        sys.exit("Could not read the image.")
    logger.info('read the image: {}'.format(img_path))
    cv.imshow(raw_name, img)

    k = cv.waitKey(0)

    if k == ord("s"):
        cv.imwrite(os.path.join(dir_path, processed_name), img)
        logger.info('Picture {} was stored {}.'.format(processed_name, dir_path))


if __name__ == '__main__':
    image_path = R"C:\Users\liangrui\Pictures\Saved Pictures\starry_night.jpg"
    save_image(image_path)
