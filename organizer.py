import os
import shutil

#path to your downloads
downloads_path = os.path.expanduser("~/Downloads")

#define where files should go

folders = {
	"Images": [".jpg",".jpeg",".png",".gif"],
	"Documents": [".pdf",".docx",".txt",".xlsx",".epub"],
	"Installers": [".dmg",".pkg",".zip"],
	"Code": [".py",".js",".html",".css"],
	"Anky": [".anki",".apkg"],
	"fonts": [".ttf",".otf"]
	}


def organize():
	for filename in os.listdir(downloads_path):
		# skip directories
		if os.path.isdir(os.path.join(downloads_path, filename)):
			continue
		name, extension = os.path.splitext(filename)
		extension = extension.lower()

		for folder, extensions in folders.items():
			if extension in extensions:
				dest_folder = os.path.join(downloads_path, folder)

				# create folder if it doesn't exist
				if not os.path.exists(dest_folder):
					os.makedirs(dest_folder)

				# move the file
				src = os.path.join(downloads_path, filename)
				dst = os.path.join(dest_folder, filename)
				try:
					shutil.move(src, dst)
					print(f"moved: {filename} to {folder}")
				except Exception as e:
					print(f"failed to move {filename}: {e}")
				break

if __name__ == "__main__":
	organize()
