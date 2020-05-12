from tkinter import *
from pygame import mixer
import time
import os
import random
from PIL import Image, ImageTk

print(os.getcwd())
songs= os.listdir("C://Users/Sritiman Adak/Desktop/songs")
New= True
pause = False
mixer.init()
index = 0
mixer.music.set_volume(0.5)
print(len(songs))
def stopMusic():
	global pause
	if not New:
		if pause:
			mixer.music.unpause()
		else:
			mixer.music.pause()
		pause = not pause	
def playMusic():
	global New
	global pause
	mixer.music.load("C://Users/Sritiman Adak/Desktop/songs/"+str(songs[index]))
	mixer.music.play()
	New = False
	pause=False
	
def nextMusic():
	global index
	global new
	if index<37:
		New = True
		index+=1
		l2  = Label(f,text = songs[index],bg ="gray" , fg= "yellow", font = ("lucida",12), anchor = "w")
		l2.text =songs[index]
		l2.place(relx =0.2,rely =0.2, relwidth =0.75, relheight=0.1)
	
def prevMusic():
	global index
	global new
	if index>0:
		new = True
		index-=1
		l2  = Label(f,text= songs[index],bg ="gray" , fg= "yellow", font = ("lucida",12), anchor = "w")
		l2.text = songs[index]
		l2.place(relx =0.2,rely =0.2, relwidth =0.75, relheight=0.1)

def setVol(val):	
	volume = int(val)/100
	mixer.music.set_volume(volume)

root =Tk()
root.title("Music Player")
root.geometry("600x460")
f = Frame(root,bg = "gray",padx = 5, pady = 5)
f.place(relx = 0, rely= 0, relwidth=1 ,relheight = 1)

pic1 = Image.open("pause.png")
dim1 =(int(pic1.size[0]/3),int(pic1.size[1]/3))
newpic1 = pic1.resize(dim1)
img1 = ImageTk.PhotoImage(newpic1)
pic2 = Image.open("play.png")
dim2 =(int(pic2.size[0]/3),int(pic2.size[1]/3))
newpic2 = pic2.resize(dim2)
img2 = ImageTk.PhotoImage(newpic2)

pic4 = Image.open("prev.png")
dim4 =(int(pic4.size[0]/6),int(pic4.size[1]/6))
newpic4 = pic4.resize(dim4)
img4 = ImageTk.PhotoImage(newpic4)
pic3 = Image.open("next.png")
dim3 =(int(pic3.size[0]/6),int(pic3.size[1]/6))
newpic3 = pic3.resize(dim3)
img3 = ImageTk.PhotoImage(newpic3)

l1  = Label(f,text = "Now Playing",bg ="gray" , fg= "white",font = ("lucida",25,"bold"))
l1.place(relx =0.2,rely =0.05, relwidth =0.6, relheight=0.1)

l2  = Label(f,text = songs[index],bg ="gray" , fg= "yellow", font = ("lucida",12), anchor = "w")
l2.place(relx =0.2,rely =0.2, relwidth =0.75, relheight=0.1)

vol  = Label(f,text = "VOLUME",bg ="gray" , fg= "black", font = ("arial",13,"bold"))
vol.place(relx =0.4,rely =0.5, relwidth =0.2, relheight=0.1)

scale = Scale(root, bg  = "gray",from_=0, to = 100 ,orient =HORIZONTAL,tickinterval =20, borderwidth =5,command = setVol)
scale.set(50)
scale.place(relx =0.3,rely =0.35, relwidth =0.4, relheight=0.15)

Button(root,image = img2, command = playMusic, borderwidth = 5).place(relx =0.3,rely =0.6, relwidth =0.2, relheight=0.2)
Label(text = "Play from\nbeginning",bg = "gray", anchor = "nw").place(relx =0.3,rely =0.8, relwidth =0.2, relheight=0.1)
Button(root,image = img1, command = stopMusic, borderwidth = 5).place(relx =0.5,rely =0.6, relwidth =0.2, relheight=0.2)
Label(text = "Pause / Unpause",bg = "gray", anchor = "nw").place(relx =0.5,rely =0.8, relwidth =0.2, relheight=0.1)
Button(root,image = img4, command = prevMusic, borderwidth = 8).place(relx =0.1,rely =0.4, relwidth =0.15, relheight=0.2)
Label(text = "Previous",bg = "gray", anchor = "w").place(relx =0.1,rely =0.34, relwidth =0.15, relheight=0.06)
Button(root,image = img3, command = nextMusic, borderwidth = 8).place(relx =0.75,rely =0.4, relwidth =0.15, relheight=0.2)
Label(text = "Next",bg = "gray", anchor = "e").place(relx =0.75,rely =0.34, relwidth =0.15, relheight=0.06)

root.mainloop()