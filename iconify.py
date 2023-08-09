#!/bin/env python

import argparse
import os
from PIL import Image

if os.name != "nt":
	print("This script is meant to be used on windows.")
	exit(1)

# Argument stuff #################################################
parser = argparse.ArgumentParser()
parser.add_argument('-d', '--directory', type=str, default="./", 
					help='Directory to run the script on.')
args = parser.parse_args()
##################################################################

# Find all folders in the given directory.
folders = filter(lambda x: os.path.isdir(x),
            	map(lambda x: os.path.join(args.directory, x),
					os.listdir(args.directory)))

# Find a .jpg/.jpeg/.png in each folder and make an .ico with it.
# Then we use Desktop.ini to set up the icon on the folder
im_extensions = (".jpg", ".jpeg", ".png", ".webp") # Supported formats here, check python3 -m PIL.
im_formats = tuple(map(lambda x: x.replace('.','',1), filter(lambda x: x != ".jpg", im_extensions)))
for folder in folders:
	images = list(filter(lambda x: os.path.splitext(x)[1].lower() in im_extensions,
            			map(lambda x: os.path.join(folder, x),
							os.listdir(folder))))
	if images:
		outfile = os.path.join(folder, "cover.ico")
		if not os.path.exists(outfile): # If cover.ico doesn't already exist
			with Image.open(images[0], formats=im_formats) as im: 
				im = im.resize((256, 256))
				im = im.convert("RGBA") # Needed for ICOs to work properly on Windows 10
				im.save(os.path.join(folder, "cover.ico"), format="ICO", sizes=[(256,256)]) # Make icon
			
			# Create Desktop.ini with the icon information.
			with open(os.path.join(folder, "Desktop.ini"), "w") as dfile:
				dfile.writelines([	"[.ShellClassInfo]\n",
									"ConfirmFileOp=0\n",
									"IconFile=cover.ico\n",
									"IconIndex=0\n"])

			# Setting attributes to hide Desktop.ini, this marks it as a system file, if you
			# ever want to delete it, it will show a scary message, you can ignore it, I do
			# this so it doesn't show when "show hidden files" option is enabled.
			os.system("attrib +s +h \"{}\"".format(os.path.join(folder, "Desktop.ini")))

			# Giving the folder a system attribute too, needed for it to show a custom ICO
			# properly.
			os.system("attrib +s \"{}\"".format(folder))

print("Done! you may need to clear your thumbnail cache if some icons don't show (main drive disk cleanup)")