import sys, os, re, cairo, codecs
import numpy as np

folder_name = "data_40x40_noisy"
#folder_name = sys.argv[1]

print("Looking into: ", folder_name)


path_to_img =  os.getcwd() + "/" + folder_name + "/"
filelist = os.listdir(folder_name + "/")
print ("found: ", len(filelist), " files ")

file_indices = []
labels = []
sizes = []
datas = []

def get_rgb(i):
  return (i / 256 / 256, ((i / 256) % 256), i % 256)

def grey_scale(mat):
  for i in range(0, len(mat)):
    for j in range(0, len(mat[i])):
      (r, g, b) = get_rgb(mat[i][j])
      mat[i][j] = (r + g + b) / 3

for filename in filelist:
  file_indices.append(int(re.findall(r'\d+', filename)[0]))
  labels.append("R" if filename[0] == "r" else "C")
  img = cairo.ImageSurface.create_from_png(path_to_img + filename)
  buf = img.get_data()
  width = img.get_width()
  height = img.get_height()
  sizes.append((width, height))
  data = np.ndarray(shape=(width, height),
                       dtype=np.uint32,
                       buffer=buf)
  data = grey_scale(data)
  data = data.astype(np.uint8)
  datas.append(data)

labels = np.array(labels)
indices = np.array(file_indices)
sizes = np.array(sizes)
raw_data = np.array(datas)

np.savez(folder_name + ".npz",
    labels=labels,
    indices=indices,
    sizes=sizes,
    raw_data=raw_data)
