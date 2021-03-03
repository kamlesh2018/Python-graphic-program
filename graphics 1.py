from tkinter import*
graph=Tk()
graph.geometry("500x500")
graph.title("Graphics 1")
def l_save():
    ln=Label(graph,text="bye")
    ln.pack();
l1=Label(graph,text="Graphics 1",bg="red",font='ariel 50')
l1.pack()
b1=Button(graph,text="like it")
b2=Button(graph,text="did not like")
b1.pack()
b2.pack()
e1=Entry(graph,width="50")
e1.pack()
savebutton=Button(graph,text="Save",command=l_save)
savebutton.pack()
savebutton.pack()
c1=Checkbutton(graph,text="yes");
c2=Checkbutton(graph,text="no");
c1.pack();
c2.pack();
l3=Button(graph,text="FACEBOOK",font="ariel 50",bg="blue")
l3.pack()
r1=Radiobutton(graph,text="new",width="50");
r1.pack()
graph.mainloop()    
    
    
