from tkinter import *
import random as r
import pandas as p
import time

BACKGROUND_COLOR = "#B1DDC6"
current_card={}
w={}

# ---------------------------- Flip card ------------------------------- #
def flip():
    canva.itemconfigure(ct,text="English",fill="white")
    canva.itemconfig(cw,text=current_card['English'],fill="white")
    canva.itemconfig(cb,image=backimg)


# ---------------------------- Words ------------------------------- #
try:
    data=p.read_csv("words_to_learn.csv")
except FileNotFoundError:
    orgdata=p.read_csv(r"french_words.csv")
    w=orgdata.to_dict(orient="records")
else:
    w=data.to_dict(orient="records")

def words():
    global current_card,fliptim
    win.after_cancel(fliptim)
    current_card=r.choice(w)
    canva.itemconfig(ct,text="French",fill="black")
    canva.itemconfig(cw,text=f"{current_card['French']}",fill="black")
    canva.itemconfig(cb,image=fimg)
    fliptim=win.after(3000,func=flip)




# ---------------------------- Known Words ------------------------------- #
def knownwords():
    w.remove(current_card)
    da=p.DataFrame(w)
    da.to_csv("words_to_learn.csv",index=False)
    words()
        


# ---------------------------- UI SETUP ------------------------------- #
win = Tk()
win.title("Flash Cards")
win.config(padx=50,pady=50,bg=BACKGROUND_COLOR)
# win.after(3000,func=flip)
# win.minsize(900,900)

fliptim=win.after(3000,func=flip)

fimg=PhotoImage(file=r"card_front.png")
rimg=PhotoImage(file=r"right.png")
wimg=PhotoImage(file=r"wrong.png")
backimg=PhotoImage(file=r"card_back.png")

canva=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
cb=canva.create_image(400,263,image=fimg)
ct=canva.create_text(400,150, font=('ariel',40,"italic"))
cw=canva.create_text(400,263,font=('ariel',60,'bold'))
canva.config(bg=BACKGROUND_COLOR)
canva.grid(row=0,column=0,columnspan=2)

wb=Button(image=wimg,highlightthickness=0,bg=BACKGROUND_COLOR,command=words)
wb.grid(row=1,column=0)

rgb=Button(image=rimg,highlightthickness=0,bg=BACKGROUND_COLOR,command=knownwords)
rgb.grid(row=1,column=1)


words()

win.mainloop()
