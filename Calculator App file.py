#Calculator app

from tkinter import *
from PIL import Image, ImageTk
#pip install pillow


root=Tk()
root.title('Calculator App')
ico = Image.open('calculator.webp')
photo = ImageTk.PhotoImage(ico)
root.wm_iconphoto(False, photo)


#def btn_click(value):
#    print(value)


def btn_click(value):
    global data
    data=data+str(value)
    input_text.set(data)

def btn_equal():
    global data
    result=str(eval(data))
    input_text.set(result)

def btn_clear():
    global data
    data=" "
    input_text.set(' ')
    

data=" "
input_text=StringVar()

input_frame=Frame(root,width=300,height=20,highlightbackground='black',highlightthickness=1)
input_frame.pack(side=TOP)

input_field=Entry(input_frame,justify=RIGHT,width=22,textvariable=input_text,bg='#eee',font=('times',20,'bold'))
input_field.grid(row=0,column=0)
input_field.pack(ipady=10)

btn_frame=Frame(root,width=300,height=220,bg='lightgreen')
btn_frame.pack()


#first row

clear=Button(btn_frame,text='C',command=lambda:btn_clear(),width=33,height=3,bd=0).grid(row=0,columnspan=3,padx=1,pady=1)
devide=Button(btn_frame,text='/',command=lambda:btn_click('/'),width=10,height=3,bd=0).grid(row=0,column=3,padx=1,pady=1)

#second row

seven=Button(btn_frame,text=7,command=lambda:btn_click(7),width=10,height=3,bd=0).grid(row=1,column=0,padx=1,pady=1)
eight=Button(btn_frame,text=8,command=lambda:btn_click(8),width=10,height=3,bd=0).grid(row=1,column=1,padx=1,pady=1)
nine=Button(btn_frame,text=9,command=lambda:btn_click(9),width=10,height=3,bd=0).grid(row=1,column=2,padx=1,pady=1)
multiply=Button(btn_frame,command=lambda:btn_click('*'),text='*',width=10,height=3,bd=0).grid(row=1,column=3,padx=1,pady=1)

#third row

four=Button(btn_frame,text=4,command=lambda:btn_click(4),width=10,height=3,bd=0).grid(row=2,column=0,padx=1,pady=1)
five=Button(btn_frame,text=5,command=lambda:btn_click(5),width=10,height=3,bd=0).grid(row=2,column=1,padx=1,pady=1)
six=Button(btn_frame,text=6,command=lambda:btn_click(6),width=10,height=3,bd=0).grid(row=2,column=2,padx=1,pady=1)
plus=Button(btn_frame,text='+',command=lambda:btn_click('+'),width=10,height=3,bd=0).grid(row=2,column=3,padx=1,pady=1)

#fourth row

one=Button(btn_frame,text=1,command=lambda:btn_click(1),width=10,height=3,bd=0).grid(row=3,column=0,padx=1,pady=1)
two=Button(btn_frame,text=2,command=lambda:btn_click(2),width=10,height=3,bd=0).grid(row=3,column=1,padx=1,pady=1)
Three=Button(btn_frame,text=3,command=lambda:btn_click(3),width=10,height=3,bd=0).grid(row=3,column=2,padx=1,pady=1)
minus=Button(btn_frame,text='-',command=lambda:btn_click('-'),width=10,height=3,bd=0).grid(row=3,column=3,padx=1,pady=1)

#fifth row

zero=Button(btn_frame,text=0,command=lambda:btn_click(0),width=21,height=3,bd=0).grid(row=4,columnspan=2,padx=1,pady=1)
dot=Button(btn_frame,text='.',command=lambda:btn_click('.'),width=10,height=3,bd=0).grid(row=4,column=2,padx=1,pady=1)
equal=Button(btn_frame,text='=',command=lambda:btn_equal(),width=10,height=3,bd=0).grid(row=4,column=3,padx=1,pady=1)


root.mainloop()
