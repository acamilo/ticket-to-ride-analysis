from PIL import Image
import sys
import os

scan = ""

try:
    scan = sys.argv[1]
except IndexError:
    print("No filename provided")
    exit(-1)

print("Opening '%s'"%(scan))

im_scan = Image.open(scan)

col_px = 2030
row_px = 1320

for x in range(0,2):
    for y in range(0,5):
        
        left = x*col_px
        right = left+col_px
        top = y*row_px
        bottom = top+row_px
        print("%d,%d,%d,%d"%(left,right,top,bottom))
        im_card = im_scan.crop((left,top,right,bottom))
        im_card = im_card.transpose(Image.ROTATE_180)
        im_card_name = os.path.basename(scan).split('.')[0] + "-%d-%d"%(x,y)+".jpg"
        im_card.save(im_card_name)