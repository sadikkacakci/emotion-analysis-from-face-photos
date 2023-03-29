from tkinter import *
from tkinter import messagebox
from test import getUrl,downloadImages

def clearEntry():
    entry1.delete(0,"end")

def submit(entry,category):
    if category not in emotion_list:
        messagebox.showwarning(title="Kategori",message="Kaydedilecek klasörü seçiniz.")
        return
    try:
        url = getUrl(entry)
        downloadImages(url,category)
        messagebox.showinfo(title="Başarılı",message="İndirme işlemi başarıyla gerçekleşti.")
    except:
        messagebox.showerror(title="Hata!",message="İndirme işlemi gerçekleştirilemedi.")


root = Tk()
root.geometry("400x400")
root.configure(background="white")
root.resizable(False,False) 
root.title("Image Downloader")

entry1 = Entry(root,width = 50,fg ="black",bg = "white",borderwidth=2,font = ("Arial",10))
entry1.pack(padx=30, pady=40)
entry1.insert(0,"Ara...")
entry1.bind("<FocusIn>", lambda event:clearEntry())

emotion_list = ["Angry","Disgust","Fear","Happiness","Sadness","Surprise"]
value_inside = StringVar(root)
value_inside.set("Kaydedilecek klasörü seç")
question_menu = OptionMenu(root, value_inside, *emotion_list)
question_menu.place(relx=0.5, rely=0.5, anchor=CENTER)


clear_button = Button(root,text= "Temizle",height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10),command = lambda: clearEntry())
clear_button.place(relx=0.4, rely=0.3, anchor=CENTER)


submit_button = Button(root,text= "Kaydet",height = 2, width = 10,fg = "black",bg="white",font = ("Arial",10),command = lambda: submit(entry1.get(),value_inside.get()))
submit_button.place(relx=0.6, rely=0.3, anchor=CENTER)

root.mainloop()