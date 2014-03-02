#!/usr/bin/env python3

import PIL.Image as Img
import numpy as np
#import colorsys
import colortools
import sys
import os

def rainbow(imgary):
    width = len(imgary)
    dhue = 360 / width
    for (i, line) in enumerate(imgary):
        hue = dhue*i
        #print(hue)
        print(i)
        for (j, pixel) in enumerate(line):
            (h,s,v) = colortools.rgb_to_hsv(*pixel)
            (r,g,b) = colortools.hsv_to_rgb(hue,s,v)
            imgary[i,j] = (int(r),int(g),int(b))
    return imgary

def main():
    if len(sys.argv) == 2:
        filename = sys.argv[1]
        if os.path.isfile(filename):
            imgary = np.array(Img.open(filename), dtype=np.uint8)
            imgary = rainbow(imgary)
            rainb = Img.fromarray(imgary)
            rainb.show()
            rainb.save("{}.rainbow.png".format(filename))

if __name__ == "__main__":
    main()
