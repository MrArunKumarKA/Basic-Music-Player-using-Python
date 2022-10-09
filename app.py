from pygame import mixer
import tkinter as tk
import fnmatch
import os

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x400")
canvas.config(bg='black')

mixer.init()

musicPath = "" # enter the path of songs present in your system
pattern = "*.mp3"
play_pause = "Play"

def onSelect(e):
    playButton["text"] = "Play"
    
def select():
    if (playButton["text"] == "Play"):
        label.config(text=listBox.get("anchor"))
        mixer.music.load(musicPath + "\\" + listBox.get("anchor"))
        playButton["text"] = "Pause"
        mixer.music.play()
        print('play working')
    elif (playButton["text"] == "Resume"):
        playButton['text'] = "Pause"
        mixer.music.unpause()
        print('resume working')
    else:
        playButton["text"] = "Resume"
        print('pause working')
        mixer.music.pause()


def stop():
    playButton["text"] = "Play"
    listBox.select_clear('active')
    mixer.music.stop()

def next():
    playButton["text"] = "Pause"
    print(listBox)
    # mixer.music.play()

def prev():
    playButton["text"] = "Pause"
         

listBox = tk.Listbox(canvas, fg='cyan', bg='black',
                     width=100, font=('poppins', 14))
listBox.pack(padx=15, pady=15)
listBox.bind('<<ListboxSelect>>', onSelect)

label = tk.Label(canvas, bg='black', fg='cyan', font=('poppins', 14))
label.pack(pady=15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=10, anchor='center')

prevButton = tk.Button(canvas, text="Prev", command=prev)
prevButton.pack(pady=15, padx=5, in_=top, side='left')

playButton = tk.Button(canvas, text=play_pause, command=select)
playButton.pack(pady=15, padx=5, in_=top, side='left')

stopButton = tk.Button(canvas, text="Stop", command=stop)
stopButton.pack(pady=15, padx=5, in_=top, side='left')

nextButton = tk.Button(canvas, text="Next", command=next)
nextButton.pack(pady=15, padx=5, in_=top, side='left')

for root, dirs, files in os.walk(musicPath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
