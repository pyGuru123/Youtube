# Remove image background
# pip install rembg

import rembg
import os


for index, file in enumerate(os.listdir()):  
	if file.endswith('.jpg'):
		name, ext = os.path.splitext(file)
		with open(file, "rb") as inp:
			with open(f"{name}-rem.png", "wb") as out:
				input = inp.read()
				output = rembg.remove(input)
				out.write(output)
		print(f'done {index+1}')
