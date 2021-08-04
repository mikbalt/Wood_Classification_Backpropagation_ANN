import os 
import numpy as np

FOLDER = "delapan_watt/sepuluh_centi"
PATH = os.path.join(os.getcwd(), FOLDER)
NAMA_BARU = ["kayu-A", "kayu-B", "kayu-C", "kayu-D", "kayu-E"]
no_id = np.array([1,1,1,1,1])

for nama_file in os.listdir(PATH):

	if "kayu-A" in nama_file:
		os.rename(os.path.join(PATH, nama_file), os.path.join(PATH, NAMA_BARU[0] + str(no_id[0]) + ".jpg"))
		no_id[0] += 1
	elif "kayu-B" in nama_file:
		os.rename(os.path.join(PATH, nama_file), os.path.join(PATH, NAMA_BARU[1] + str(no_id[1]) + ".jpg"))
		no_id[1] += 1
	elif "kayu-C" in nama_file:
		os.rename(os.path.join(PATH, nama_file), os.path.join(PATH, NAMA_BARU[2] + str(no_id[2]) + ".jpg"))
		no_id[2] += 1
	elif "kayu-D" in nama_file:
		os.rename(os.path.join(PATH, nama_file), os.path.join(PATH, NAMA_BARU[3] + str(no_id[3]) + ".jpg"))
		no_id[3] += 1
	elif "kayu-E" in nama_file:
		os.rename(os.path.join(PATH, nama_file), os.path.join(PATH, NAMA_BARU[4] + str(no_id[4]) + ".jpg"))
		no_id[4] += 1