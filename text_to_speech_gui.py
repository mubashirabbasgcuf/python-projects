from tkinter import*
from tkinter import ttk
import win32com.client
speaker = win32com.client.Dispatch("SAPI.SpVoice") 
def speak():
    text=entry.get()
    if text:
        speaker.speak(text)
    else:
        print("please enter some text") 
root=Tk()
root.title("text to speech")
root.geometry("2000x800")
Label(root,text="Text to speech Gui",font=("Calberi",20,"bold"),fg="yellow",bg="green").grid(row=1,column=7,padx=30)
Label(root,text="Enter text:",font=("calberi",15)).grid(row=3,column=7,padx=10)
entry=Entry(root,width=30)
entry.grid(row=3,column=10)
ttk.Button(root,text="Speak",command=speak).grid(row=4,column=10)
root.mainloop()