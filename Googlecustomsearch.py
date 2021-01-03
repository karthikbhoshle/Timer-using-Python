from tkinter import *
###########################
w = '#FFFFFF'
g = '#07ba1f'
gr='#607b96'
r = '#d40f0f'
t='#635a8a'
b='#01020d'
y='#f7f74a'
#############
root=Tk()
root.geometry('600x600')
root.title('Timer')
root.config(bg=w)

###################33
m=IntVar()
m.set(0)
mt=IntVar()
mt.set(0)
###########################3
def Run():
    global l11

    nt = mt.get()
    #print(nt)
    if nt >0:
        mt.set(nt-1)
        l11.config(text=str(mt.get()))
        l11.after(1000, Run)
def Runn():
    p=m.get()
    #print(p)
    mt.set(p)
    #print(mt.get())
    l11.config(text=str(mt.get()+1))
    Run()

##################################33
l1=Label(root,bg=w,text='SET TIME',fg=gr,font=('Consolas',22),justify='center')
l1.grid(row=0,padx=5,pady=5)
l2=Label(root,text='',width=90,bg=g,font=('Consolas',10),justify='center')
l2.grid(row=1,padx=5,pady=5)
f2=Frame(root,bg=w)
f2.grid(row=2,padx=5,pady=5)
e1=Entry(f2,text=m,fg=t,bg=g,font='courier 15',justify='center',relief=FLAT )
e1.pack(padx=5,pady=5)
b1=Button(f2,text='Submit',fg=r,bg=gr,font='courier 13',justify='center',relief=FLAT,command=Runn)
b1.pack(padx=5,pady=5)
l11=Label(f2,bg=w,text=mt.get(),fg=gr,font=('Consolas',22),justify='center')
l11.pack(padx=5,pady=5)
####################################
root.mainloop()