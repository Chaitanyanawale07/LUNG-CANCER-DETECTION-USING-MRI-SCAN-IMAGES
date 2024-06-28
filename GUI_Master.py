
import tkinter as tk
from tkinter import ttk, LEFT, END
from PIL import Image, ImageTk

global fn
fn = ""
##############################################+=============================================================
root = tk.Tk()
root.configure(background="brown")
# root.geometry("1300x700")


w, h = root.winfo_screenwidth(), root.winfo_screenheight()
root.geometry("%dx%d+0+0" % (w, h))
root.title( "Lung Cancer Disease detection")

# 43

# ++++++++++++++++++++++++++++++++++++++++++++
# #####For background Image
# image2 = Image.open('A1.jpg')
# image2 = image2.resize((1530, 900), Image.ANTIALIAS)

# background_image = ImageTk.PhotoImage(image2)

# background_label = tk.Label(root, image=background_image)

# background_label.image = background_image

# background_label.place(x=0, y=0)  # , relwidth=1, relheight=1)

img=ImageTk.PhotoImage(Image.open("s3.jpg"))

img2=ImageTk.PhotoImage(Image.open("33.jpg"))

img3=ImageTk.PhotoImage(Image.open("11.jpg"))


logo_label=tk.Label()
logo_label.place(x=0,y=115)

x = 1

# function to change to next image
def move():
	global x
	if x == 4:
		x = 1
	if x == 1:
		logo_label.config(image=img)
	elif x == 2:
		logo_label.config(image=img2)
	elif x == 3:
		logo_label.config(image=img3)
	x = x+1
	root.after(2000, move)

# calling the function
move()



#
label_l1 = tk.Label(root, text="Lung Cancer Disease Detection",font=("Times New Roman", 35, 'bold'),
                    background="#152238", fg="white", width=55, height=2)
label_l1.place(x=0, y=0)

#T1.tag_configure("center", justify='center')
#T1.tag_add("center", 1.0, "end")

################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#def clear_img():
#    img11 = tk.Label(root, background='bisque2')
#    img11.place(x=0, y=0)


#################################################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%


################################$%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

# def cap_video():
    
#     video1.upload()
#     #from subprocess import call
#     #call(['python','video_second.py'])



# def log():
#     from subprocess import call
#     call(["python","GUI_Master_old.py"])
    
def reg():
    from subprocess import call
    call(["python","GUI_Master_old1.py"])    
    
def window():
  root.destroy()


button1 = tk.Button(root, text="Lung Cancer Detection", command=reg, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
button1.place(x=100, y=160)
# button2 = tk.Button(root, text="Alzheimer Disease detection", command=log, height=1,font=('times', 20, ' bold '), bg="#152238", fg="white")
# button2.place(x=100, y=230)



button3 = tk.Button(root, text="Exit",command=window,width=14, height=1,font=('times', 20, ' bold '), bg="red", fg="white")
button3.place(x=100, y=290)

root.mainloop()