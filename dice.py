import tkinter as tk
from PIL import Image,ImageTk 
import random

window = tk.Tk()
window.geometry("500x500")
window.configure(background='beige')
window.title("Dice")


#button = tk.Button(window,text=a).pack()

dice = ["dice1.png","dice2.png","dice3.png","dice4.png","dice5.png","dice6.png"]
image1 = ImageTk.PhotoImage(Image.open(random.choice(dice)))
image2 = ImageTk.PhotoImage(Image.open(random.choice(dice)))

label1= tk.Label(window,image=image1)
label2= tk.Label(window,image=image2)

label1.image= image1
label2.image= image2

label1.place(x=16,y=100)
label2.place(x=300,y=100)

def dice_roll():
    image1 =ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label1.configure(image = image1)
    label1.image = image1
    
    image2 =ImageTk.PhotoImage(Image.open(random.choice(dice)))
    label2.configure(image = image2)
    label2.image = image2

  
button =tk.Button(window,width=10,height=3,text="ROLL THE DICE" , bg="brown"  ,fg="pink" ,command=dice_roll)
button.place(x=230 , y=0)
window.mainloop()