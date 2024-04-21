from tkinter import *
root = Tk()
root.title("SADIA_Calculator")
root.geometry("310x460")

# Create a frame for the display (likely for the result display)
display = Frame(root, height=110)
display.pack(fill=X, pady=10)
countertext = StringVar()
counter = Entry(display ,bg="lightgreen", textvariable=countertext , font=("digital-7",20, "bold"),width=13)
counter.pack(fill=X,ipady=5)

def click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            if countertext.get().isdigit():
                value = int(countertext.get())
            else:
                value = eval(countertext.get())

            countertext.set(value)
            counter.update()
        except ZeroDivisionError:
            countertext.set("Error: Division by zero")
            counter.update()
    elif text == "clear":
        countertext.set("")
        counter.update()
    else:
        countertext.set(countertext.get()+text)

# Create a frame for the keypad (likely for buttons)
keypad = Frame(root, height=350)
keypad.pack(fill="both", expand=True)

# Load the image
background_image = PhotoImage(file="Untitled-1787.png")
# Create a label to display the background image
background_label = Label(keypad, image=background_image)
background_label.place(relwidth=1, relheight=1)  # Cover the entire frame

clear_img = PhotoImage(file="pictures\\clear.png")

zero_img = PhotoImage(file= "pictures\\0.png")
one_img = PhotoImage(file="pictures\\1.png")
two_img = PhotoImage(file="pictures\\2.png")
three_img = PhotoImage(file="pictures\\3.png")
four_img = PhotoImage(file="pictures\\4.png")
five_img = PhotoImage(file="pictures\\5.png")
six_img = PhotoImage(file="pictures\\6.png")
seven_img = PhotoImage(file="pictures\\7.png")
eight_img = PhotoImage(file="pictures\\8.png")
nine_img = PhotoImage(file="pictures\\9.png")

dot_img = PhotoImage(file="pictures\\dot.png")
devide_img = PhotoImage(file="pictures\\devide.png")
multiply_img = PhotoImage(file="pictures\\x.png")
plus_img = PhotoImage(file="pictures\\+.png")
minus_img = PhotoImage(file="pictures\\-.png")
equall_img = PhotoImage(file="pictures\\=.png")

# Create a "clear" button within the keypad frame
clear = Button(keypad, text="clear", image=clear_img)
clear.bind("<Button-1>",click)
clear.grid(row=0, columnspan=4, pady=4 , padx=4)

######### ROW 1 #########

Seven = Button(keypad, text="7",bd=0 , image=seven_img)
Seven.bind("<Button-1>",click)
Seven.grid(row=1, column=0, pady=4 , padx=4)

Eight = Button(keypad, text="8",bd=0, image=eight_img)
Eight.bind("<Button-1>",click)
Eight.grid(row=1, column=1, pady=4 , padx=4)

Nine = Button(keypad, text="9",bd=0, image=nine_img)
Nine.bind("<Button-1>",click)
Nine.grid(row=1, column=2, pady=4 , padx=4)

Multiply = Button(keypad, text="*" ,bd=0, image=multiply_img)
Multiply.bind("<Button-1>",click)
Multiply.grid(row=1, column=3, pady=4 , padx=4)

######### ROW 2 #########

Four = Button(keypad, text="4",bd=0 , image=four_img)
Four.bind("<Button-1>",click)
Four.grid(row=2, column=0, pady=4 , padx=4)

Five = Button(keypad, text="5",bd=0 , image=five_img)
Five.bind("<Button-1>",click)
Five.grid(row=2, column=1, pady=4 , padx=4)

Six = Button(keypad, text="6" ,bd=0, image=six_img)
Six.bind("<Button-1>",click)
Six.grid(row=2, column=2, pady=4 , padx=4)

Minus = Button(keypad, text="-" ,bd=0, image=minus_img)
Minus.bind("<Button-1>",click)
Minus.grid(row=2, column=3, pady=4 , padx=4)

######### ROW 3 #########

One = Button(keypad, text="1",bd=0, image=one_img)
One.bind("<Button-1>",click)
One.grid(row=3, column=0, pady=4 , padx=4)

Two = Button(keypad, text="2",bd=0, image=two_img)
Two.bind("<Button-1>",click)
Two.grid(row=3, column=1, pady=4 , padx=4)

Three = Button(keypad, text="3",bd=0, image=three_img)
Three.bind("<Button-1>",click)
Three.grid(row=3, column=2, pady=4 , padx=4)

Plus = Button(keypad, text="+" ,bd=0, image=plus_img)
Plus.bind("<Button-1>",click)
Plus.grid(row=3, column=3, pady=4 , padx=4)

######### ROW 4 #########

DOT = Button(keypad, text="." ,bd=0, image=dot_img)
DOT.bind("<Button-1>",click)
DOT.grid(row=4, column=0, pady=4 , padx=4)

Zero = Button(keypad, text="0",bd=0 , image=zero_img)
Zero.bind("<Button-1>",click)
Zero.grid(row=4, column=1, pady=4 , padx=4)

Equall = Button(keypad, text="=" ,bd=0, image=equall_img)
Equall.bind("<Button-1>",click)
Equall.grid(row=4, column=2, pady=4 , padx=4)

Devide = Button(keypad, text="/",bd=0 , image=devide_img)
Devide.bind("<Button-1>",click)
Devide.grid(row=4, column=3, pady=4 , padx=4)

root.mainloop()
