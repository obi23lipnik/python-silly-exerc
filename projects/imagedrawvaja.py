__author__ = 'obi'
import Image, ImageDraw, sys

im = Image.open("mapchunk.png")
draw = ImageDraw.Draw(im)
draw.line((0, 0) + im.size, fill=128)
draw.line((0, im.size[1], im.size[0], 0), fill=128)
del draw
im.save(sys.stdout, "PNG")