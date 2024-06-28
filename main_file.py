import tkinter as tk
#from tkinter import ttk, LEFT, END
from PIL import Image , ImageTk 
#from tkinter.filedialog import askopenfilename
#import cv2
#qlite3
#import tfModel_test as tf_test
# global fn
# fn=""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="seashell2")
#root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title("Lung Cancer Disease detection")


#430
#++++++++++++++++++++++++++++++++++++++++++++
#####For background Image
image2 =Image.open('a1.jpg')
image2 =image2.resize((720,800), Image.ANTIALIAS)

background_image=ImageTk.PhotoImage(image2)
background_label = tk.Label(root, image=background_image,bd=5)

background_label.image = background_image

background_label.place(x=0, y=0) #, relwidth=1, relheight=1)
#


frame_alpr = tk.LabelFrame(root, text="  ", width=640, height=700, bd=5, font=('times', 14, ' bold '),bg="#271983")
frame_alpr.grid(row=0, column=0)
frame_alpr.place(x=720, y=30)

lbl = tk.Label(root, text="Lung Cancer Disease detection", font=('Elephant', 20,' bold '),width=33, height=2,bg="black",fg="red")
lbl.place(x=720, y=10)

lbl = tk.Label(frame_alpr, text='Thought those with ', font=('Lucida Calligraphy', 15,' bold '),bg="#271983",fg="white")
lbl.place(x=170, y=100)

lbl = tk.Label(frame_alpr, text="Lung's might forgot", font=('Lucida Calligraphy', 15,' bold '),bg="#271983",fg="white")
lbl.place(x=270, y=140)

lbl = tk.Label(frame_alpr, text="us,We as a society ", font=('Lucida Calligraphy', 15,' bold '),bg="#271983",fg="white")
lbl.place(x=140, y=180)

lbl = tk.Label(frame_alpr, text=" must remember them", font=('Lucida Calligraphy', 15,' bold '),bg="#271983",fg="white")
lbl.place(x=190, y=220)




def login():

    from subprocess import call
    call(["python", "login.py"])  

def register():

    from subprocess import call
    call(["python", "registration.py"])  
   
def window():
    root.destroy()

button1 = tk.Button(frame_alpr, text=" SIGN UP ",command=register,width=15, height=1, font=('times', 15, ' bold '),bg="#3BB9FF",fg="white")
button1.place(x=200, y=350)

button2 = tk.Button(frame_alpr, text="LOGIN",command=login,width=15, height=1, font=('times', 15, ' bold '),bg="#3BB9FF",fg="white")
button2.place(x=200, y=450)




root.mainloop()