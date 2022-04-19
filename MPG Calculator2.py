from tkinter import *

root=Tk()
root.title("Some GUI")
root.geometry("400x700")
CheckVar1=IntVar()
CheckVar2=IntVar()
CheckVar3=IntVar()
CheckVar4=IntVar()
CheckVar5=IntVar()
CheckVar6=IntVar()
CheckVar7=IntVar()
totalvalue=0


Oil=Checkbutton(root,text="Oil Change 20.00",variable=CheckVar1,onvalue=20\
                ,offvalue=0,height=5,width=20)
Lube=Checkbutton(root,text="Lube Job 18.00",variable=CheckVar2,onvalue=18\
                ,offvalue=0,height=5,width=20)
RadiatorFlush=Checkbutton(root,text="Radiator Flush--$30.00",variable=CheckVar3,onvalue=30\
                ,offvalue=0,height=5,width=20)
Transmission=Checkbutton(root,text="Transmission Flush--80.00",variable=CheckVar4,onvalue=80\
                ,offvalue=0,height=5,width=20)
Inspection=Checkbutton(root,text="Inspection--15.00",variable=CheckVar5,onvalue=15\
                ,offvalue=0,height=5,width=20)
Muffler=Checkbutton(root,text="Muffler replacement--100.00",variable=CheckVar6,onvalue=100\
                ,offvalue=0,height=5,width=20)
Tire=Checkbutton(root,text="Tire Rotation--20.00",variable=CheckVar7,onvalue=20\
                ,offvalue=0,height=5,width=20)


total_lbl = Label(root)
def click():
    total = 0
    for var in (CheckVar1, CheckVar2, CheckVar3, CheckVar4, CheckVar5, CheckVar6, CheckVar7):
        total += var.get()
    total_lbl.config(text="${}.00".format(total))
somebutton=Button(root, text="Total", command=click)

Oil.pack()
Lube.pack()
RadiatorFlush.pack()
Transmission.pack()
Inspection.pack()
Muffler.pack()
Tire.pack()
somebutton.pack()

total_lbl.pack()


root.mainloop()
