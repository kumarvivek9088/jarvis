# importing required module
from tkinter import *
from PIL import ImageTk,Image
from random import randint

#defining functions
# 0->rock 1->paper 2->scissor
def hoverrock(e):             
    b1.config(bg="green")
def hoverpaper(e):
    b2.config(bg="green")
def hoverscissor(e):
    b3.config(bg="green")

def leaverock(p):
    b1.config(bg="white")
def leavepaper(p):
    b2.config(bg="white")
def leavescissor(p):
    b3.config(bg="white")
def win(u,j):
    global jpoint,upoint
    if u==0 and j==0:
        print("it's tie")
        whowin.config(text="it's tie",bg="green")
    elif u==0 and j==1:
        print("Jarvis win")
        whowin.config(text="Jarvis win",bg="green")
        jpoint+=1
        label4.config(text=jpoint)

    elif u==0 and j==2:
        print("User win")
        whowin.config(text="User win",bg="green")
        upoint+=1
        label5.config(text=upoint)
    elif u==1 and j==0:
        print("User win")
        whowin.config(text="User win",bg="green")
        upoint+=1
        label5.config(text=upoint)
    elif u==1 and j==1:
        print("tie")
        whowin.config(text="it's tie",bg="green")
    elif u==1 and j==2:
        print("jarvis win")
        whowin.config(text="Jarvis win",bg="green")
        jpoint+=1
        label4.config(text=jpoint)
    elif u==2 and j==0:
        print("jarvis win")
        whowin.config(text="Jarvis win",bg="green")
        jpoint+=1
        label4.config(text=jpoint)
    elif u==2 and j==1:
        print("user win")
        whowin.config(text="User win",bg="green")
        upoint+=1
        label5.config(text=upoint)
    else:
        print("its tie")
        whowin.config(text="it's tie",bg="green")

def pressrock():
    u=0
    label3.config(image=rock)
    d=randint(0,2)
    if d==0:
        label2.config(image=rock)
    elif d==1:
        label2.config(image=paper)
    else:
        label2.config(image=scissor)
    win(u,d)
def presspaper():
    u=1
    label3.config(image=paper)
    d=randint(0,2)
    if d==0:
        label2.config(image=rock)
    elif d==1:
        label2.config(image=paper)
    else:
        label2.config(image=scissor)
    win(u,d)
def pressscissor():
    u=2
    label3.config(image=scissor)
    d=randint(0,2)
    if d==0:
        label2.config(image=rock)
    elif d==1:
        label2.config(image=paper)
    else:
        label2.config(image=scissor)
    win(u,d)

# creating root window
root=Tk()
#images
rock=ImageTk.PhotoImage(Image.open("images/rock.png"))
paper=ImageTk.PhotoImage(Image.open("images/paper.png"))
scissor=ImageTk.PhotoImage(Image.open("images/scissor.png"))
root.geometry("800x600")
root.title("Rock paper scissor game")
label1=Label(root,text="Welcome to Rock Paper Scissor Game",font=("calibri",28,"bold"),fg="green")
label1.pack()
jarvis=Label(root,text="Jarvis: -",font=("calibri",18,"bold"))
jarvis.pack()
user=Label(root,text="User: -",font=("calibri",18,"bold"))
user.pack()
jarvis.place(x=50,y=100)
user.place(x=600,y=100)
label2=Label(root,image=rock,width=259,height=230)
label2.pack()
label3=Label(root,image=rock,width=259,height=230)
label3.pack()
label2.place(x=25,y=150)
label3.place(x=500,y=150)
vs=Label(root,text="V/s",font=("calibri",82,"bold","italic"))
vs.pack()
vs.place(x=325,y=175)
smallrock=ImageTk.PhotoImage(Image.open("images/smallrock.png"))
smallpaper=ImageTk.PhotoImage(Image.open("images/smallpaper.png"))
smallscissor=ImageTk.PhotoImage(Image.open("images/smallscissor.png"))

b1=Button(root,image=smallrock,width=120,height=100,command=pressrock)
b2=Button(root,image=smallpaper,width=120,height=100,command=presspaper)
b3=Button(root,image=smallscissor,width=120,height=100,command=pressscissor)
b1.pack()
b2.pack()
b3.pack()
b1.place(x=350,y=475)
b2.place(x=500,y=475)
b3.place(x=650,y=475)
b1.bind('<Enter>',hoverrock)
b2.bind('<Enter>',hoverpaper)
b3.bind('<Enter>',hoverscissor)
b1.bind('<Leave>',leaverock)
b2.bind('<Leave>',leavepaper)
b3.bind('<Leave>',leavescissor)
ch=Label(root,text="Chose your move:-",font=("calibri",20,"bold"))
ch.pack()
ch.place(x=350,y=430)
score=Label(root,text="Scorecard",font=("calibri",18,"bold"))
score.pack()
score.place(x=70,y=425)
jscore=Label(root,text="Jarvis: ",font=("calibri",16,"bold"))
uscore=Label(root,text="User: ",font=("calibri",16,"bold"))
jscore.pack()
uscore.pack()
jscore.place(x=70,y=460)
uscore.place(x=70,y=495)
jpoint=0
upoint=0
label4=Label(root,text=jpoint,font=("calibri",14,"bold"))
label5=Label(root,text=upoint,font=("calibri",14,"bold"))
label4.pack()
label5.pack()
label4.place(x=210,y=460)
label5.place(x=210,y=495)
whowin=Label(root,font=("calibri",20,"bold"),fg="white")
whowin.pack()
whowin.place(x=325,y=100)

root.mainloop()