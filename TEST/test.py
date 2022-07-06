from PIL import Image
folderidx = 1
for folder in range(47):
    foldernum = str(folderidx).zfill(3)
    pngidx = 1
    for images in range(320):
        num = str(pngidx).zfill(3)
        img_png = Image.open(f"D:\\PNGTOJPG\\INDATA\\NITROHCS-{foldernum}\\OHCS{num}.png")
        print(num)
        img_png.save(f"D:\\PNGTOJPG\\OUTDATA\\NITROHCS-{foldernum}\\OHCS{num}.jpg")
        pngidx += 1
    folderidx += 1