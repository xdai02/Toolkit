import os

path = "./"
files = os.listdir(path)
cnt = 1
for file in files:
    if ".py" in file:
        continue
    os.rename(path + file, path + str(cnt) + ".jpg")
    cnt += 1