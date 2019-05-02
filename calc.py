from tkinter import *
class MyWindow:
    def __init__(self, win):
        self.lbl1=Label(win, text='First number',bg="yellow")
        self.t3 = Entry()
        self.lbl2 = Label(win, text='Second number',bg="yellow")
        self.t2= Entry()
        self.lbl3=Label(win, text='Result',bg="red")
        self.t4 = Entry()
        self.t5 = Entry()

        self.b11 = Button(win,fg="blue", text='9', command=lambda:self.action(9))
        self.b12 = Button(win,fg="blue",text='8', command=lambda:self.action(8))
        self.b13 = Button(win,fg="blue", text='7', command=lambda:self.action(7))
        self.b14 = Button(win,fg="blue", text='6', command=lambda:self.action(6))
        self.b15 = Button(win,fg="blue", text='5', command=lambda:self.action(5))
        self.b16 = Button(win,fg="blue", text='4', command=lambda:self.action(4))
        self.b17 = Button(win,fg="blue", text='3', command=lambda:self.action(3))
        self.b18 = Button(win,fg="blue", text='2', command=lambda:self.action(2))
        self.b19 = Button(win,fg="blue", text='1', command=lambda:self.action(1))
        self.b10 = Button(win,fg="blue", text='0', command=lambda:self.action(0))
        self.bmul = Button(win,fg="blue", text='*', command=lambda :self.operator('*'))
        self.bdiv = Button(win,fg="blue", text='/', command=lambda :self.operator('/'))
        self.badd = Button(win,fg="blue", text='+',command=lambda :self.operator('+'))
        self.bsub = Button(win,fg="blue", text='-',command = lambda :self.operator('-'))
        self.bclr = Button(win,fg="blue", text='CLR',command = self.clear)
        self.bres = Button(win,fg="blue", text='=', command=self.result)



        self.lbl1.place(x=50, y=20)
        self.lbl2.place(x=50, y=50)
        self.t3.place(x=200, y=20)

        self.t2.place(x=200, y=50)

        self.b11.place(x=75, y=90)
        self.b12.place(x=125, y=90)
        self.b13.place(x=175, y=90)
        self.bmul.place(x=225, y=90)
        self.b14.place(x=75, y=120)
        self.b15.place(x=125, y=120)
        self.b16.place(x=175, y=120)
        self.bdiv.place(x=225,y=120)
        self.b17.place(x=75, y=150)
        self.b18.place(x=125, y=150)
        self.b19.place(x=175, y=150)
        self.bsub.place(x=225, y=150)
        self.b10.place(x=75, y=180)
        self.badd.place(x=125, y=180)
        self.bres.place(x=175, y=180)
        self.bclr.place(x=225, y=180)

        self.lbl3.place(x=50, y=225)
        self.t4.place(x=200,y=225)


    def clear(self):
        self.t3.delete(0,'end')
        self.t2.delete(0,'end')
        self.t4.delete(0,'end')
        global res
        res = 0
        global fn
        fn = 0

    def result(self):
        number1 = int(self.t3.get())
        number2 = int(self.t2.get())
        if op=='+':
            result = number1+number2
            self.t4.insert(END,result)

        elif op=='-':
            result = number1-number2
            self.t4.insert(END,result)

        elif op=='*':
            result = number1*number2
            self.t4.insert(END,result)

        elif op=='/':
            result = number1/number2
            self.t4.insert(END,result)

        global res
        res = 1


    def operator(self,operator):
        if res == 1:
            value = self.num1=int(self.t4.get())
            self.t3.delete(0,'end')
            self.t3.insert(END,str(value))
            self.t2.delete(0,'end')
            self.t4.delete(0,'end')
        global fn
        global op
        op = operator
        print(op)
        fn = 1
        print(str(fn))

    def action(self,value):
        if fn==0:
            print("hi"+str(value)+str(fn))
            self.t3.insert(END,str(value))
        elif fn==1:
            self.t2.insert(END,str(value))

    def ins(self):
        print('hi')

    def add(self):
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1+num2
        self.t3.insert(END, str(result))
    def sub(self, event):
        num1=int(self.t1.get())
        num2=int(self.t2.get())
        result=num1-num2
        self.t3.insert(END, str(result))

window=Tk()
fn=0
op = 'null'
res = 0
mywin=MyWindow(window)
window.title('Calculator')
window.geometry("400x300+10+10")
window.mainloop()
