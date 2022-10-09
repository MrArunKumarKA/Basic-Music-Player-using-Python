from pygame import mixer
import tkinter as tk
import fnmatch
import os

canvas = tk.Tk()
canvas.title("Music Player")
canvas.geometry("600x700")
canvas.config(bg='black')

mixer.init()

musicPath = "E:\Music"
pattern = "*.mp3"
play_pause = "Play"


def select():
    label.config(text= listBox.get("anchor"))
    mixer.music.load( musicPath + "\\" + listBox.get("anchor"))
    print(mixer.music.get_pos())
    if (playButton.cget('text') == "Play") and (mixer.music.get_busy() == False):
        playButton.configure(text= "Pause")
        mixer.music.play()
    elif (playButton.cget('text') == "Play") and (mixer.music.get_busy() == True): 
        playButton.configure(text= "Pause")
        mixer.music.unpause()
    else:
        playButton.configure(text= "Play")
        mixer.music.pause()
# def play():
    

listBox = tk.Listbox(canvas, fg='cyan', bg='black',
                     width=100, font=('poppins', 14))
listBox.pack(padx=15, pady=15)

label = tk.Label(canvas, bg= 'black', fg= 'cyan', font= ('poppins', 14))
label.pack(pady=15)

top = tk.Frame(canvas, bg='black')
top.pack(padx=10, pady=10, anchor='center')

prevButton = tk.Button(canvas, text= "Prev")
prevButton.pack(pady= 15, padx= 5, in_= top, side= 'left')

playButton = tk.Button(canvas, text= play_pause, command= select)
playButton.pack(pady= 15, padx= 5, in_= top, side= 'left')

stopButton = tk.Button(canvas, text= "Stop")
stopButton.pack(pady= 15, padx= 5, in_= top, side= 'left')

nextButton = tk.Button(canvas, text= "Next")
nextButton.pack(pady= 15, padx= 5, in_= top, side= 'left')

for root, dirs, files in os.walk(musicPath):
    for filename in fnmatch.filter(files, pattern):
        listBox.insert('end', filename)

canvas.mainloop()
