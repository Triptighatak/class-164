from tkinter import *
root=Tk()
root.geometry("900x500")
from PIL import ImageTk, Image
from tkinter import filedialog
root.configure(background="pink")
a=Label(root, bg="gold2", highlightthickness=8)
label.place(relx=0.5,rely=0.5,anchor=CENTER)
img_path=""
def openFile():
    global img_path
    img_path=filedialog.askopenfilename(title="open Text file",filestypes=[("image files","*.jpg *.gif *.png *.jpeg")])
    im=Image.open(img_path)
    img=ImageTk.PhotoImage(im)
    a["image"]=img
    img.close()
btn = Button(root, text="Open image", command=openFile)
btn.place(relx=0.5,rely=0.1,anchor=CENTER)     
root.mainloop()