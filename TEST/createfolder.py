import os
folderidx = 1
for folder in range(47):
    foldernum = str(folderidx).zfill(3)
    directory = f"NITROHCS-{foldernum}"
    parent_dir = "D:\\PNGTOJPG\\OUTDATA"
    path = os.path.join(parent_dir, directory)
    os.mkdir(path)
    folderidx += 1