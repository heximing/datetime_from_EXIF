import datetime
import os
import subprocess

if __name__ == '__main__':

    dt_string_2 = "2020:07:30 21:46:21"
    # Considering date is in yyyy:mm:dd format
    dt_object2 = datetime.datetime.strptime(dt_string_2, "%Y:%m:%d %H:%M:%S")
    print("dt_object2 =", dt_object2)
    print("dt_object2 - 4 hours =", (dt_object2 + datetime.datetime.timedelta(hours=-4)).strftime('%Y-%m-%d_%H-%M-%S'))

    # file name with extension
    path = 'C:/Users/Administrator/Downloads/2023-04-19_backup/back/'
    onlyfiles = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    print(type(onlyfiles), onlyfiles)
    for file_name in onlyfiles:
        print("")
        split_tup = os.path.splitext(file_name)
        print(type(split_tup), "split_tup =", split_tup)
        # write the complete path of your video file along with its type for example mp4
        input_file = path + file_name
        # write the complete path of the ExifTool in your device along with .exe at last
        exe = "C:/Users/Administrator/Downloads/exiftool.exe"
        # Download EXIFtool from https://exiftool.org/
        # process is a variable
        process = subprocess.Popen([exe, input_file], stdout=subprocess.PIPE, stderr=subprocess.STDOUT,
                                   universal_newlines=True)
        # For the output
        for output in process.stdout:
            if output[0:17] == "Track Create Date":
                print(type(output), len(output), output.strip())  # strip is used to remove unwanted spaces
                print("datetime string =", output[-20:-1])
                datetime_name = datetime.datetime.strptime(output[-20:-1], "%Y:%m:%d %H:%M:%S")
                datetime_name = (datetime_name + datetime.datetime.timedelta(hours=-4)).strftime('%Y-%m-%d_%H-%M-%S')
                print("datetime_name =", datetime_name + "-back" + split_tup[-1])
                my_source = path + split_tup[0] + split_tup[-1]
                my_dest = path + datetime_name + "-back" + split_tup[-1]
                try:
                    os.rename(my_source, my_dest)
                except FileExistsError:
                    print("[WinError 183] Cannot create a file when that file already exists")
                    print("skipped")
            else:
                pass
