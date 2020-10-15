# sudo apt-get install python3-tk
from tkinter import *
import tkinter as tk
import os
import sys

artemispath = sys.argv[1] # /home/martin/miniconda3/bin

listOfFilesUnsorted = [f for f in os.listdir() if os.path.isfile(f)]
listOfFiles = sorted(listOfFilesUnsorted, key=str.casefold)

window = tk.Tk()

def buttonClick():
    artFiles = ['','','','','']
    for i in range(0,5):
        myIndex = lbs[i].curselection()
        if len(myIndex)>0:
            fileIndex = myIndex[0]-1
            if fileIndex>=0: artFiles[i] = os.getcwd() + '/' + listOfFiles[fileIndex]

    plotFiles=''
    for i in range(1,5):
        if not artFiles[i]=='': plotFiles+= artFiles[i]+','

    os.system("cd " + artemispath + "; ./art -Duserplot=" + plotFiles[:-1] + " " + artFiles[0])
    pass


#5 list boxes in total..
column_names=("Reference","Plot 1","Plot 2","Plot 3","Plot 4");
lbs = list()

for i in range(0,5):
    lbl1 = Label(window, text=column_names[i], fg='black', font=("Helvetica", 12, "bold"))
    lbl1.grid(row=0,column=(i*2))
    
    scrollbar = Scrollbar(window, orient="vertical")
    
    lb = Listbox(window, width=30, height=50, yscrollcommand=scrollbar.set, font=("Helvetica", 12), exportselection=False)
    lb.grid(row=1,column=(i*2))
    lbs.append(lb)
    
    scrollbar.grid(row=1,column=(i*2)+1,sticky=N+S+W)
    
    # lb1 = Listbox(window, width=20, height=50, yscrollcommand=scrollbar.set, font=("Helvetica", 12))

    scrollbar.config(command=lb.yview)
#    scrollbar.grid.pack(side="right", fill="y")

    n=0
    lb.insert(0,"<NONE>")

    for f in listOfFiles:
        lb.insert(n+1,listOfFiles[n])
        n+=1

    #lb1.pack()

btnsubmit = Button(window, command=buttonClick, text="Submit", font=("Helvetica", 12, "bold"))
btnsubmit.grid(row=2,columnspan=10)

#

#on click then run artemis with the art command...
# gunzip
# Rename the plot to something that Artemis will like
# convert plots to +ve/-ve format
# Check the plot is not longer than the reference


tk.mainloop()
