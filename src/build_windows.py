import os
import sys
from shutil import rmtree
from glob import glob

if 'win32' not in sys.platform:
    print("this script is for windows only!")
    exit()


# Cleanup
rmtree('./__pycache__', ignore_errors=True)
rmtree('./build', ignore_errors=True)
rmtree('./dist', ignore_errors=True)
for path in glob('./*.spec'):
	os.remove(path)

THIS_VERSION = None
try:
	mainfile = open('duckypad_autoprofile.py')
	for line in mainfile:
		if "THIS_VERSION_NUMBER =" in line:
			THIS_VERSION = line.replace('\n', '').replace('\r', '').split("'")[-2]
	mainfile.close()
except Exception as e:
	print('build_windows exception:', e)
	exit()

if THIS_VERSION is None:
	print('could not find version number!')
	exit()

os.system("pyinstaller.exe --noconsole --icon=icon.ico duckypad_autoprofile.py")

output_folder_path = os.path.join('.', "dist")
original_name = os.path.join(output_folder_path, "duckypad_autoprofile")
new_name = os.path.join(output_folder_path, "duckypad_autoprofile_" + THIS_VERSION + "_win10_x64")

print(original_name)
print(new_name)

os.rename(original_name, new_name)
zip_file_name = "duckypad_autoprofile_" + THIS_VERSION + "_win10_x64.zip"
os.system('7z.exe a ' + zip_file_name + ' -r ' + new_name)

# Cleanup
rmtree('./__pycache__', ignore_errors=True)
rmtree('./build', ignore_errors=True)
rmtree('./dist', ignore_errors=True)
for path in glob('./*.spec'):
	os.remove(path)
