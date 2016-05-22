import time
tnull = time.time()

import Adafruit_ILI9341 as TFT
import Adafruit_GPIO.SPI as SPI
from Adafruit_ILI9341 import ILI9341_18BIT
import struct
import cairo

DC = 25
RST = 24
SPI_PORT = 0
SPI_DEVICE = 0

WIDTH = 240
HEIGHT = 320

t0 = time.time()

disp = TFT.ILI9341(DC, rst=RST, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE, max_speed_hz=64000000), bgr=True, bit_depth=ILI9341_18BIT)

disp.begin()

t1 = time.time()

s = cairo.ImageSurface(cairo.FORMAT_RGB24, WIDTH, HEIGHT)
c = cairo.Context(s)

c.rectangle(0,0,WIDTH/2,HEIGHT/2)
c.set_source_rgb(1.0, 0.0, 0.0)
c.fill()

c.rectangle(WIDTH/2,0,WIDTH/2,HEIGHT/2)
c.set_source_rgb(0.0, 1.0, 0.0)
c.fill()

c.rectangle(WIDTH/2,HEIGHT/2,WIDTH/2,HEIGHT/2)
c.set_source_rgb(0.0, 0.0, 1.0)
c.fill()

t2 = time.time()
disp.set_window()

fmt = "BBBx" * (s.get_width() * s.get_height())
img = list(struct.unpack(fmt, s.get_data()))

t3 = time.time()
disp.data(img)
t4 = time.time()

print "importing", t0 - tnull
print "setup", t1 - t0
print "drawing", t2 -t1
print "converting", t3 -t2
print "displaying", t4 -t3
print "total in script", t4 - tnull

