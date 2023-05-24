from Tkinter import *

root=Tk()
root.title("Grocery Price Calculator")
root.geometry("300x230")
root.resizable(width=False,height=False)
root.configure(bg='gray77')
label=Label(root,text="Choose An Item...")
label.place(x=100,y=5)
label.configure(bg="gray77")
v=IntVar()

res=IntVar()
def cal_price():
    value=int(v.get())
    if value==0:
        res.set(int(entry2.get())*4)
    elif value==1:
        res.set(int(entry2.get())*6)
    elif value==2:
        res.set(int(entry2.get())*10)
    elif value==3:
        res.set(int(entry2.get())*12)
             

r_btn=Radiobutton(root,text="Banana",variable=v,value=0)
r_btn.place(x=100,y=30)
r_btn.configure(bg="gray77")

r_btn2=Radiobutton(root,text="Apples",variable=v,value=1)
r_btn2.place(x=100,y=60)
r_btn2.configure(bg="gray77")

r_btn3=Radiobutton(root,text="Grapes",variable=v,value=2)
r_btn3.place(x=100,y=90)
r_btn3.configure(bg="gray77")

r_btn3=Radiobutton(root,text="Strawberry",variable=v,value=3)
r_btn3.place(x=100,y=120)
r_btn3.configure(bg="gray77")

entry=Entry(root,width=25,textvariable=res)
entry.place(x=80,y=150)

label2=Label(root,text="Price: ")
label2.place(x=5,y=150)
label2.configure(bg="gray77")

entry2=Entry(root,width=25)
entry2.place(x=80,y=180)

btn=Button(root,text="Calculate",highlightbackground="gray",command=lambda : cal_price())
btn.place(x=5,y=178)




root.mainloop()
