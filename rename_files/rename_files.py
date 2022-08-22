import os

path = "./"

files = os.listdir(path)
cnt = 1

for file in files:
    if ".py" in file:
        continue
        
    filename = os.path.splitext(file)[0]
    suffix = os.path.splitext(file)[1]
    os.rename(path + filename + suffix, path + str(cnt) + suffix)
    
    cnt += 1