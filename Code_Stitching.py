#####################################################################################################################################
#	PROGRAM BY : MC IATRIDES
#	LAST UPDATE : 12-05-2022
#	TITLE : Exercise #4 - (12-05-2022)
#   SUBTITLE : Image stiching
#	REDACTED FOR : COMPUTER VISION
#####################################################################################################################################

'''
Stitching sample
================

Show how to use Stitcher API from python in a simple way to stitch panoramas
or scans.
'''

##### PACKAGES ######################################################################################################################
from __future__ import print_function
from numpy import *
import cv2 as cv
import argparse
import sys
#####################################################################################################################################

###### ANALYSIS PART ################################################################################################################
print('START TESTS')

modes = (cv.Stitcher_PANORAMA, cv.Stitcher_SCANS)

parser = argparse.ArgumentParser(prog='Code_Stitching.py', description='Stitching sample.')
parser.add_argument('--mode',
    type = int, choices = modes, default = cv.Stitcher_PANORAMA,
    help = 'Determines configuration of stitcher. The default is `PANORAMA` (%d), '
         'mode suitable for creating photo panoramas. Option `SCANS` (%d) is suitable '
         'for stitching materials under affine transformation, such as scans.' % modes)
parser.add_argument('--output', default = 'output.jpg',
    help = 'Resulting image. The default is `output.jpg`.')
parser.add_argument('img', nargs='+', help = 'input images')

__doc__ += '\n' + parser.format_help()


def main():
    args = parser.parse_args() #selects images given in command line

    # read input images
    imgs = [] #array of img
    for img_name in args.img:
        img = cv.imread(cv.samples.findFile(img_name))
        if img is None:
            print("can't read image " + img_name)
            sys.exit(-1)
        imgs.append(img) #add img to list of img

    stitcher = cv.Stitcher.create(args.mode)
    status, pano = stitcher.stitch(imgs)

    if status != cv.Stitcher_OK:
        print("Can't stitch images, error code = %d" % status)
        sys.exit(-1)

    cv.imwrite(args.output, pano)
    print("stitching completed successfully. %s saved!" % args.output)


if __name__ == '__main__':
    print(__doc__)
    main()
    cv.destroyAllWindows()

print('END TESTS')
#####################################################################################################################################