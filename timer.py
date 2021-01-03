from tkinter import *
import sys
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
l1=Label(root,bg=w,text='TIMER',fg=gr,font=('Consolas',22),justify='center')
l1.grid(row=1,padx=5,pady=5)
l2=Label(root,text='',width=90,bg=g,font=('Consolas',10),justify='center')
l2.grid(row=0,padx=5,pady=5)
###
###############################global

st=0
check=1
clear=True
cl=0
#####################functions


def Clear():
    global e1,cl,st,check
    e1.config(text='00:00:00')
    print(st)
    st=0
    check=1
    #print(st)

def Pause():
    global check
    check=1
def Resume():
    global check,clear
    check=0
    clear=False
    Startt()


def Start():
    global st,check,e1
    print(st)
    if check==0:
        st += 1
        h, m = divmod(st, 3600)
        m, s = divmod(st - h * 3600, 60)
        h = str(h).rjust(2, '0')
        m = str(m).rjust(2, '0')
        s = str(s).rjust(2, '0')
        sm = ':'.join([h, m, s])


        e1.config(text=sm)
        e1.after(1000, Start)




def Startt():
    global check,st,clear,cl

    if check:
        check=0
        set()
    Start()


##################################main
e1 = Label(root, text='00:00:00', fg=b, bg=w, font='Consolas 25', justify='center', relief=FLAT)
e1.grid(row=3, padx=5, pady=5)

f1=Frame(root,bg=w)
f1.grid(row=4,padx=5,pady=5)

b1=Button(f1,text='Start',fg=r,bg=gr,font='courier 13',width=15,justify='center',relief=FLAT,command=Startt )
b1.grid(row=2,column=0,padx=5,pady=5)
b1=Button(f1,text='Clear',fg=r,bg=gr,font='courier 13',width=15,justify='center',relief=FLAT,command=Clear)
b1.grid(row=2,column=1,padx=5,pady=5)

b1=Button(f1,text='Resume',fg=r,bg=gr,font='courier 13',width=15,justify='center',relief=FLAT,command=Resume)
b1.grid(row=3,column=0,padx=5,pady=5)
b1=Button(f1,text='Pause',fg=r,bg=gr,font='courier 13',width=15,justify='center',relief=FLAT,command=Pause)
b1.grid(row=3,column=1,padx=5,pady=5)
###################################
root.mainloop()