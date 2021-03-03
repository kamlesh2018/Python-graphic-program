from tkinter import *
cal=Tk()
eq=""
def press(num):
    global eq
    eq=eq+str(num)
    equation.set(eq)
def equalpress():
    try:
        global eq
        total=str(eval(eq))
        equation.set(total)
        eq=""
    except:
        equation.set("error")
        eq=""
def clearpress():
    global eq
    eq=""
    equation.set("")
cal.geometry("500x500")
cal.title("Calculator")
cal.configure(background="navy blue")
intro=Label(cal,text="CALCULATOR",font="ariel 10",bg="green").grid(column=10,row=1)
equation= StringVar() 
b1=Button(cal,text="1",width="10",command=lambda:press(1)).grid(column=6,row=3) 
b2=Button(cal,text="2",width="10",command=lambda:press(2)).grid(column=7,row=3) 
b3=Button(cal,text="3",width="10",command=lambda:press(3)).grid(column=8,row=3) 
b4=Button(cal,text="4",width="10",command=lambda:press(4)).grid(column=6,row=4) 
b5=Button(cal,text="5",width="10",command=lambda:press(5)).grid(column=7,row=4)
b6=Button(cal,text="6",width="10",command=lambda:press(6)).grid(column=8,row=4) 
b7=Button(cal,text="7",width="10",command=lambda:press(7)).grid(column=6,row=5) 
b8=Button(cal,text="8",width="10",command=lambda:press(8)).grid(column=7,row=5) 
b9=Button(cal,text="9",width="10",command=lambda:press(9)).grid(column=8,row=5) 
b0=Button(cal,text="0",width="10",command=lambda:press(0)).grid(column=6,row=6) 
bp=Button(cal,text="+",width="10",command=lambda:press("+")).grid(column=7,row=6) 
bs=Button(cal,text="-",width="10",command=lambda:press("-")).grid(column=8,row=6) 
bdiv=Button(cal,text="/",width="10",command=lambda:press("/")).grid(column=6,row=7) 
bmul=Button(cal,text="*",width="10",command=lambda:press("*")).grid(column=7,row=7)
clear=Button(cal,text="clear",width="10",command=clearpress()).grid(column=8,row=7)
bequation=Button(cal,text="=",width="10",command=equalpress()).grid(column=8,row=7)
display=Entry(cal,width="20",textvariable=equation).grid(column=10,row=7)
equation.set('enter your expression') 

    
cal.mainloop()
