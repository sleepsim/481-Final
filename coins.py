import tkinter as tk
from tkinter import ttk

main = tk.Tk()



main.geometry("1000x600")
main.title("Coin Counter")

titleM = tk.Label(main, text="Coin Counter", font=('Arial', 24))
titleM.place(x=30, y =30)

uploadT = tk.Label(main, text="Upload files:", font=('Arial',  16))
uploadT.place(x=30, y=80)

button = tk.Button(main, text="Run", font=('Arial',16))
button.place(x= 450, y=400,height=50, width=100)

def display_text():
   global entry
   string= entry.get()
   label.configure(text=string)

#label that displays input
label= tk.Label(main, text="", font=('Arial',18))
label.place(x=30, y =200)

#entry widget for uploads
entry= tk.Entry(main, width= 40)
entry.focus_set()
entry.place(x= 155, y= 85)

#button to log entries
ttk.Button(main, text= "Add to List",width= 30, command= display_text).place(x=30, y =130)




main.mainloop()