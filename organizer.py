import os
import shutil

#path to your downloads
downloads_path = os.path.expanduser("~/Downloads")

#define where files should go

folders = {
	"Images": [".jpg",".jpeg",".png",".gif"],
	"Documents": [".pdf",".docx",".txt",".xlsx"],
	"Installers": [".dmg",".pkg",".zip"]
	}


def organize():
	for filename in os.listdir(downloads_path):
		name, extension= os.path.splitext(filename)

	for folder, extensions in folder.items():
		if extensions.lower() in extensions:
			dest_folder = os.path.join(downloads_path, folder)
	
			#create folder if it doesn´t exist
			if not os.path.exists(dest_folder):
				os.makedirs(dest_folder)

			#move the file
			shutil.move (os.path.join(downloads_path, filename),
					os.path .join(dest_folder),filename)
			print(f"moved: {filename} to {folder}")

if __name__ == "__main__":
	organize()
