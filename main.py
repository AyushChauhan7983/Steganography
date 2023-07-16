from tkinter import *
from tkinter import filedialog
from PIL import Image,ImageTk
import os
from stegano import lsb

root=Tk()
root.title("Steganography - Hide a secret text message in an image")
root.geometry("700x500+150+180")
root.resizable(False,False)
root.configure(bg="#2f4155")

def showimage():
    global filename
    filename=filedialog.askopenfilename(initialdir=os.getcwd(),title='Select an image file',filetypes=(("PNG file","*.png"),("JPG file","*.jpg"),("All file","*.txt")))
    img=Image.open(filename)
    img=ImageTk.PhotoImage(img)
    lbl.configure(image=img,width=250,height=250)
    lbl.image = img

def hide():
    global secret
    message=text1.get(1.0,END)
    secret=lsb.hide(str(filename),message) #Hide a message (string) in an image with the LSB (Least Significant Bit) technique.

def show():
    clear_message=lsb.reveal(filename) #Find a message in an image (with the LSB technique).
    text1.delete(1.0,END)
    text1.insert(END,clear_message)

def save():
    secret.save("hidden.png")

Label(root,text="CYBER SCIENCE",bg="#2d4155",fg="white",font=("arial 25 bold")).place(x=10,y=20)

#first frame

f=Frame(root,bd=3,bg="black",width=340,height=280,relief=GROOVE)
f.place(x=10,y=80)

lbl=Label(f,bg="black")
lbl.place(x=40,y=10)

#second frame

frame2=Frame(root,bd=3,width=340,height=280,bg="white",relief=GROOVE)
frame2.place(x=350,y=80)

text1=Text(frame2,font="Robote 20",bg="white",fg="black",relief=GROOVE,wrap=WORD)
text1.place(x=0,y=0,width=320,height=295)

scrollbar1 = Scrollbar(frame2)
scrollbar1.place(x=320,y=0,height=300)

scrollbar1.configure(command=text1.yview)
text1.configure(yscrollcommand=scrollbar1.set)

#third frame

frame3=Frame(root,bd=3,width=330,height=100,bg="#2f4155",relief=GROOVE)
frame3.place(x=10,y=370)

Button(frame3,text="Open Image",width=10,height=2,font=("arial 14 bold"),command=showimage).place(x=20,y=30)
Button(frame3,text="Save Image",width=10,height=2,font=("arial 14 bold"),command=save).place(x=180,y=30)
Label(frame3,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)


#fourth frame

frame4=Frame(root,bd=3,width=330,height=100,bg="#2f4155",relief=GROOVE)
frame4.place(x=360,y=370)

Button(frame4,text="Hide Data",width=10,height=2,font=("arial 14 bold"),command=hide).place(x=20,y=30)
Button(frame4,text="Show Data",width=10,height=2,font=("arial 14 bold"),command=show).place(x=180,y=30)
Label(frame4,text="Picture, Image, Photo File",bg="#2f4155",fg="yellow").place(x=20,y=5)

root.mainloop()


