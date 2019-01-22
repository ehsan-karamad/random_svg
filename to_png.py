import cairo
import rsvg
import os
import numpy
import random

width = 40
height = width

filelist = os.listdir('.');

noise_max = 20

def get_rgb(u32):
  b = u32 % 256
  g = (u32 / 256) % 256
  r = (u32 / 256 / 256) % 256
  return (r, g, b)

def color_of(r, g, b):
  return b + g * 256 + r * 256 * 256

def add_noise(color_value):
  (r, g, b) = get_rgb(color_value)
  x = min(255, (r + random.randint(0, noise_max)))
  return color_of(x, x, x)

def invert(color_value):
  (r, g, b) = get_rgb(color_value)
  return color_of(255 - r, 255 - g, 255 - b)

index = 1.0
for filename in filelist:
  print index/len(filelist)
  index = index + 1
  name, extension = os.path.splitext(filename)
  if extension != '.svg':
    continue
  # read the file and save as png
  with open(filename, 'r') as svg_file:
    svg_str = svg_file.read()
    img = cairo.ImageSurface(cairo.FORMAT_RGB24, width, height)
    context = cairo.Context(img)
    svg_image = rsvg.Handle(None, svg_str)
    svg_image.render_cairo(context)
    buf = img.get_data()
    data = numpy.ndarray(shape=(width, height), dtype=numpy.uint32, buffer=buf)
    for i in range(0, width):
      for j in range(0, height):
        #data[i][j] = invert(data[i][j])
        data[i][j] = add_noise(data[i][j])
        x = 1
    new_img = cairo.ImageSurface.create_for_data(data, cairo.FORMAT_RGB24, width, height)
    new_img.write_to_png(name + '.png')