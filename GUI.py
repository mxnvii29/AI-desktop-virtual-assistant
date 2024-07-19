from tkinter import* #->saare functions and classes are imported from tkinter library * means all.
from PIL import Image , ImageTk #->pil used for images,ImageTk is a module from PIL that provides support for working with images in tkinter
import speech2text
import action


def resize_image(image_path, width, height):
    original_image = Image.open(image_path) #->opens the image file
    resized_image = original_image.resize((width, height))
    return ImageTk.PhotoImage(resized_image)


root = Tk() #->t(k) create a blank main window of the appn(root window)
root.title("AI assistant") #->naam dedia
root.geometry("550x675") #->fixed dimensions dedi
root.resizable(False,False) #->resize nahi kr skte
root.config(bg="#6F8FAF") #->bg colour dedia

#ask fun
def ask():
    user_val = speech2text.speech_to_text()
    bot_val=action.action(user_val)
    text.insert(END,'User--->'+user_val+"\n")
    if bot_val != None:
        text.insert(END,"BOT<---"+str(bot_val)+"\n")
    if bot_val=="ok sir":
        root.destroy()

#send fun
def send():
    send=entry.get()
    bot=action.action(send)
    text.insert(END,'User--->'+send+"\n")
    if bot != None:
        text.insert(END,"BOT<---"+str(bot)+"\n")
    if bot=="ok sir":
        root.destroy()


#delete fun
def del_text():
    text.delete('1.0',"end")


#frame label
frame=LabelFrame(root, padx=120 , pady=15 , borderwidth=3, relief="raised")
frame.config(bg="#6F8FAF")
frame.grid(row=0, column=1, padx=20, pady=10)

#text label
text_label=Label(frame,text="AI Assistant",font=("comic sans ms",14,"bold"),bg="#356696")
text_label.grid(row=0,column=0,padx=10  ,pady=10)

image_path = "image/assistant.png"
resized_image = resize_image(image_path, 200, 200)

#image label
image=ImageTk.PhotoImage(Image.open("image/assistant.png"))
image_label = Label(frame, image=resized_image)
image_label.grid(row=1, column=0,padx=20, pady=10)


#adding text widget
text=Text(root,font=('courier 10 bold '),bg="#356696")
text.grid(row=2,column=0)
text.place(x=100,y=375,width=375,height=100)

#entry widget
entry=Entry(root,justify=CENTER)
entry.place(x=100,y=500,width=350,height=30)

#button1
button1=Button(root,text="ASK",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=ask)
button1.place(x=70,y=575)

#button2
button2=Button(root,text="SEND",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=send)
button2.place(x=400,y=575)

#button3
button3=Button(root,text="DELETE",bg="#356696",pady=16,padx=40,borderwidth=3,relief=SOLID,command=del_text)
button3.place(x=225,y=575)




root.mainloop() #prog remains until we close