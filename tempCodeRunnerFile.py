from tkinter import* #->saare functions and classes are imported from tkinter library * means all.
from PIL import Image , ImageTk
root = Tk() #->t(k) create a blank main window of the appn(root window)
root.title("AI assistant") #->naam dedia
root.geometry("550x675") #->fixed dimensions dedi
root.resizable(False,False) #->resize nahi kr skte
root.config(bg="#6F8FAF") #->bg colour dedia


#frame label
frame=LabelFrame(root, padx=50 , pady=7 , borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=20, pady=10)

#text label
text_label=Label(frame,text="AI Assistant",font=("comic sans ms",14,"bold"),bg="#356696")
text_label.grid(row=0,column=0,padx=10  ,pady=10)



#image label
image=ImageTk.PhotoImage(Image.open("image/assistant.png"))
image_label = Label(frame, image=image)
image_label.grid(row=1, column=0,padx=20, pady=10)

root.mainloop() #prog remains until we close