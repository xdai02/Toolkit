import os
import moviepy.editor as mp
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

def divest() -> None:
    try:
        filePath = select_single_file()
        my_clip = mp.VideoFileClip(filePath)
        fileName = os.path.basename(filePath).split('.')[0]
        if os.path.exists(f'{fileName}.mp3'):
            print("文件已存在于当前目录，请重新选择！")
            divest()
        else:
            my_clip.audio.write_audiofile(f'{fileName}.mp3')
    except Exception as e:
        print(e)

def select_single_file() -> str:
    filePath = filedialog.askopenfilename()
    return filePath

if __name__ == '__main__':
    divest()