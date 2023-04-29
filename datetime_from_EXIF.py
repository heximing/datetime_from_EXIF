from datetime import datetime, timedelta
import os
from os.path import isfile, join, splitext

# import the preinstalled module
import subprocess
# file name with extension
path = 'C:/Users/Administrator/Downloads/2023-04-19_backup/back/'
onlyfiles = [f for f in os.listdir(path) if isfile(join(path, f))]
print(type(onlyfiles), onlyfiles)
for file_name in onlyfiles:
    print("")
    split_tup = os.path.splitext(file_name)
    print(type(split_tup ), "split_tup =", split_tup )
    # write the complete path of your video file along with its type for example mp4
    input_file = path + file_name
    # write the complete path of the ExifTool in your device along with .exe at last
    exe="C:/Users/Administrator/Downloads/exiftool.exe"
    # process is a variable
    process=subprocess.Popen([exe,input_file],stdout=subprocess.PIPE,stderr=subprocess.STDOUT,universal_newlines=True)
    # For the output
    for output in process.stdout:
        if output[0:17] == "Track Create Date":
            print(type(output), len(output), output.strip()) # strip is used to remove unwanted spaces
            print("datetime string =", output[-20:-1])
            datetime_name = datetime.strptime(output[-20:-1], "%Y:%m:%d %H:%M:%S")
            datetime_name = (datetime_name + timedelta(hours=-4)).strftime('%Y-%m-%d_%H-%M-%S')
            print("datetime_name =", datetime_name+"-back"+split_tup[-1])
            my_source = path + split_tup[0] + split_tup[-1]
            my_dest = path + datetime_name + "-back" + split_tup[-1]
            try:
                os.rename(my_source, my_dest)
            except FileExistsError:
                print("[WinError 183] Cannot create a file when that file already exists")
                print("skipped")
        else:
            pass
