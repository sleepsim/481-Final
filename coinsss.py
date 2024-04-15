import tkinter as tk
from tkinter import ttk, filedialog;

global filenamesHolder, uniqueFiles, totalAmount
global pennyCount, nickelCount, dimeCount, quarterCount, loonieCount, toonieCount

pennyCount = 0
nickelCount = 0
dimeCount = 0
quarterCount = 0
loonieCount = 0
toonieCount = 0

uniqueFiles = ()

filenamesHolder = ()

totalAmount = 0;

# The function for uploading new files
def UploadAction(event=None):
   filename = filedialog.askopenfilenames()
   if not filename:
      print("empty var")
   else:
      global filenamesHolder, uniqueFiles
      filenamesHolder += filename
      uniqueFiles = list(set(filenamesHolder))
      UpdateListBox()

#Function for updating the items in the listbox
def UpdateListBox():
   my_listbox.delete(0, 'end')
   for item in uniqueFiles:
      my_listbox.insert('end', item)
   print(my_listbox.get(0, 'end'))

#Deletes items from the list
def delete():
   selected_checkboxs = my_listbox.curselection() 
  
   for selected_checkbox in selected_checkboxs[::-1]: 
        my_listbox.delete(selected_checkbox) 

def Reset():
   global totalAmount;
   global pennyCount, nickelCount, dimeCount, quarterCount, loonieCount, toonieCount
   
   totalAmount = 0;
   pennyCount = 0
   nickelCount = 0
   dimeCount = 0
   quarterCount = 0
   loonieCount = 0
   toonieCount = 0

#Gets the value of the coin depending on their class
def GetCoinValue(input):
   global totalAmount
   global pennyCount, nickelCount, dimeCount, quarterCount, loonieCount, toonieCount
   match input:
      case "Penny":
         totalAmount += 0.01;
         pennyCount += 1;
      case "Nickel":
         totalAmount += 0.05;
         nickelCount += 1;
      case "Dime":
         totalAmount += 0.1;
         dimeCount += 1;
      case "Quarter":
         totalAmount += 0.25;
         quarterCount += 1;
      case "Loonie":
         totalAmount += 1;
         loonieCount += 1;
      case "Toonie":
         totalAmount += 2;
         toonieCount += 1;
      case _:
         totalAmount += 0;
         
def Run():
   global totalAmount;
   global pennyCount, nickelCount, dimeCount, quarterCount, loonieCount, toonieCount
   
   totalAmount = 0;
   pennyCount = 0
   nickelCount = 0
   dimeCount = 0
   quarterCount = 0
   loonieCount = 0
   toonieCount = 0
   
   if not my_listbox.get(0, 'end'):
      totalAmount = 0;
   else:
      results = model(my_listbox.get(0, 'end'))
      for result in results:
         boxes = result.boxes  # Boxes object for bbox outputs
         class_indices = boxes.cls  # Class indices of the detections
         class_names = [result.names[int(cls)] for cls in class_indices]  # Map indices to names
         for item in class_names:
            GetCoinValue(item)
            print("after addition: " + str(totalAmount))
   
def display_text():
   global totalAmount
   string= totalAmount
   label.configure(text=string)

#_______________MAIN__________________

main = tk.Tk()
main.geometry("1000x600")
main.title("Coin Counter")

titleM = tk.Label(main, text="Coin Counter", font=('Arial', 24))
titleM.place(x=30, y =30)

uploadT = tk.Label(main, text="Uploaded files:", font=('Arial',  16))
uploadT.place(x=30, y=150)

button = tk.Button(main, text="Run", font=('Arial',16), command=lambda: [Run(), display_text()] )
button.place(x= 450, y=400,height=50, width=100)

#button to log entries
ttk.Button(main, text= "Upload Images",width= 30, command= UploadAction).place(x=30, y = 80)

listVar = tk.StringVar(value = filenamesHolder)
my_listbox = tk.Listbox(main, listvariable=listVar, width = 80, selectmode= "extended")
my_listbox.place(x= 30, y=200)

my_button = tk.Button(main, text ="Delete", command= delete)
my_button.place(x= 30, y= 400)

#label that displays input
label= tk.Label(main, text="", font=('Arial',18))
label.place(x=30, y =450) 

#_________AI MODEL_________
from ultralytics import YOLO
import sys, os

print('My nested folder : ', os.getcwd()+"\Model\\best.pt")
print('File name : ', os.path.basename(__file__))
print('Root path:', sys.path[1])

#Get the pretrained model ready
modelLocation = os.getcwd() + "\Model\\best.pt"
model = YOLO(modelLocation)

link = "C:\\Users\\Pocholo\\Desktop\\481\\CV_Project\\images\\train\\23-P.jpg"
link2 = "C:\\Users\\Pocholo\\Desktop\\481\\CV_Project\\images\\train\\29-P.jpg"

#Predict with the model with any image from internet
# results = model((link2, link))

# for result in results:
#    boxes = result.boxes  # Boxes object for bbox outputs
#    class_indices = boxes.cls  # Class indices of the detections
#    class_names = [result.names[int(cls)] for cls in class_indices]  # Map indices to names
   
#    for item in class_names:
#       GetCoinValue(item)
#       print("after addition: " + str(totalAmount))



main.mainloop()