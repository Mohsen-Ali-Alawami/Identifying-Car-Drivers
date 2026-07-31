import os
import re
import shutil
##################################################################################################################

# source = r"D:\Sejong_Univ\research\Driver_authentication\Capstone2023-master\Capstone2023-master\Data\csv_data - Copy\U12-1\Belt1"
# source = r"D:\Sejong_Univ\research\Driver_authentication\Capstone2023-master\Capstone2023-master\Data\csv_data - Copy\U12-1\Belt2"
source = r"D:\Sejong_Univ\research\Driver_authentication\Capstone2023-master\Capstone2023-master\Data\csv_data - Copy\U2\Seat"

# destination = r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U12-1\Belt1"
# destination = r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U12-1\Belt2"
destination = r"D:\Sejong_Univ\research\Driver_authentication\datasets\5_seconds\U2\Seat"
for root, dirs, files in os.walk(source):
    for name in files:
        if name.endswith((".csv")) and name.startswith(("1")):
            src_path = os.path.join(source, name)
            dst_path = os.path.join(destination, name)
            os.rename(src_path, dst_path)


# # iterate on all files to move them to destination folder
# for f in allfiles:
#     src_path = os.path.join(source, f)
#     dst_path = os.path.join(destination, f)
#     os.rename(src_path, dst_path)