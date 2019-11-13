#author:wr786
import os

os.system("attrib /s /d -s -h *") #解除隐藏
files = os.listdir()
for file in files:
    filename = file + ".exe" #删除以.exe为后缀的“文件夹”
    print(filename)
    if os.path.exists(filename):
        os.remove(filename)
