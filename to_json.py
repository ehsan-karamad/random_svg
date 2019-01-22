import sys, os, re, cairo, numpy, codecs, json

folder_name = "data_40x40_noisy"
folder_name = sys.argv[1]

print("Looking into: ", folder_name)


path_to_img =  os.getcwd() + "/" + folder_name + "/"
filelist = os.listdir(folder_name + "/")
print ("found: ", len(filelist), " files ")

raw_data = []
for filename in filelist:
  index = int(re.findall(r'\d+', filename)[0])
  label = "R" if filename[0] == "r" else "C"
  img = cairo.ImageSurface.create_from_png(path_to_img + filename)
  buf = img.get_data()
  width = img.get_width()
  height = img.get_height()
  data = numpy.ndarray(shape=(width, height),
                       dtype=numpy.uint32,
                       buffer=buf)
  raw_data.append({
    'index': index,
    'label': label,
    'shape': (width, height),
    'data': data.tolist() # np.array(foo) then reshape
    })

json.dump(raw_data, codecs.open("./" + folder_name + ".json", "w", encoding="utf-8"), separators=(",", ":"), indent=4)


