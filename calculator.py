import tkinter
from tkinter import *
import math
var=""
A=0
B=""
operator=""
operationlist=["+","-","x","/","^","!","%","√"] 
def btn_1_isclicked():
     global var
     global B
     B=B+"1"
     data1.set(B)
     var=var+"1"
     data.set(var)     
     
def btn_2_isclicked():
     global var
     global B
     B=B+"2"
     data1.set(B)
     var=var+"2"
     data.set(var)
     
def btn_3_isclicked():
     global var
     global B
     B=B+"3"
     data1.set(B)
     var=var+"3"
     data.set(var)
     
def btn_4_isclicked():
     global var
     global B
     B=B+"4"
     data1.set(B)
     var=var+"4"
     data.set(var)

def btn_5_isclicked():
     global var
     global B
     B=B+"5"
     data1.set(B)
     var=var+"5"
     data.set(var)
     
def btn_6_isclicked():
     global var
     global B
     B=B+"6"
     data1.set(B)
     var=var+"6"
     data.set(var)
    
def btn_7_isclicked():
     global var
     global B
     B=B+"7"
     data1.set(B)
     var=var+"7"
     data.set(var)
     

def btn_8_isclicked():
     global var
     global B
     B=B+"8"
     data1.set(B)
     var=var+"8"
     data.set(var)
     

def btn_9_isclicked():
     global var
     global B
     B=B+"9"
     data1.set(B)
     var=var+"9"
     data.set(var)
    

def btn_0_isclicked():
     global var
     global B
     B=B+"0"
     data1.set(B)
     var=var+"0"
     data.set(var)
   
def btn_e_isclicked():
     global var
     global B
     B="e"
     data1.set(B)
     var="e"
     data.set(var)


def btn_pi_isclicked():
     global var
     global B
     B=B+"π"
     j=var+"π"
     i=math.pi
     if var=="":
          var=str(i)
     else:          
          var=str(int(var)*i)     
     data.set(j)
     data1.set(B)
  
     
def btn_back_isclicked():
     global var
     global B
     d=len(B)
     B=B[0:(d-1)]
     d=len(var)     
     var=var[0:(d-1)]
     data1.set(B)
     data.set(var)
     
     
def btn_dot_isclicked():
     global var
     global B
     B=B+"."
     data1.set(B)
     var=var+"."
     data.set(var)
 
def btn_plus_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"+"
    data1.set(B)
    t=0
    z=var
    for s in operationlist:
         if s in var:
              t=t+1
              command=result()
    A=float(var)
    operator="+"
    var=var+"+"
    data.set(var)
  

def btn_min_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"-"
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=float(var)
    operator="-"
    var=var+"-"
    data.set(var)
  

def btn_pro_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"x"
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=float(var)
    operator="x"
    var=var+"x"
    data.set(var)
  
def btn_div_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"/"
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=float(var)
    operator="/"
    var=var+"/"
    data.set(var)
 
def btn_pow_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"^"
    data1.set(B)
    if var=="e":
         A=0
    else:
         A=float(var)
    operator="^"
    var=var+"^"
    data.set(var)

def btn_per_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"%"
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=float(var)
    operator="%"
    var=var+"%"
    data.set(var)
 

def btn_squareroot_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"√"
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=var
    operator="√"
    var=var+"√"
    data.set(var)
  

def btn_factorial_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"!"
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=int(var)
    operator="!"
    var=var+"!"
    data.set(var)
   

def btn_sin_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"sin("
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=var
    operator="sin"
    var=var+"sin("
    data.set(var)
    

def btn_cos_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"cos("
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=var
    operator="cos"
    var=var+"cos("
    data.set(var)
    

def btn_tan_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"tan("
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=var
    operator="tan"
    var=var+"tan("
    data.set(var)
   

def btn_log_isclicked():
    global var
    global A
    global operator
    global B
    B=B+"log("
    data1.set(B)
    for s in operationlist:
         if s in var:
              command=result()
    A=var
    operator="log"
    var=var+"log("
    data.set(var)
  
def btn_C_isclicked():
    global var
    global A
    global operator
    global B
    B=""
    data1.set(B)
    A=0
    operator=""
    var=""
    data.set(var)
    

def result():
    global var
    global A
    global operator
    var1=var
    if operator=="+":
        if "sin" in var1:
             x=float((var1.split("+sin")[1]))
             c=A+math.sin(x)
        else:
             x=float((var1.split("+")[1]))
             c=A+x
        if c%1==0:
             c=int(c)
        data.set(c)
        var=str(c)
    elif operator=="-":
        x=float((var1.split("-")[1]))
        c=A-x
        if c%1==0:
             c=int(c)
        data.set(c)
        var=str(c)
    elif operator=="x":
        x=float((var1.split("x")[1]))
        c=A*x
        if c%1==0:
             c=int(c)
        data.set(c)
        var=str(c)
    elif operator=="/":
        x=float((var1.split("/")[1]))
        if x==0:
            data.set("Not Defined")
            var=""
            A=""
        else:
            c=round(A/x,10)
            if c%1==0:
                 c=int(c)
            data.set(c)
            var=str(c)
    elif operator=="^":
        x=float((var1.split("^")[1]))
        if var1[0]=="e":
             c=math.exp(x)
        else:
             c=A**x
        data.set(c)
        var=str(c)
    elif operator=="%":
        c=A/100
        if c%1==0:
             c=int(c)
        data.set(c)
        var=str(c)
    elif operator=="√":
        x=float((var1.split("√")[1]))
        c=x**0.5
        if A!="":
             c=c*float(A)
        if c%1==0:
                 c=int(c)     
        data.set(c)
        var=str(c)
    elif operator=="!":
        c=1
        while A>1:
            c=c*A
            A=A-1
        if c%1==0:
                 c=int(c)    
        data.set(c)
        var=str(c)
    elif operator=="sin":
        x=float((var1.split("sin(")[1]))
        k=math.sin(x)
        if A!="":
             c=float(A)*k
        else:
             c=k
        if c%1==0:
                 c=int(c)     
        data.set(c)
        var=str(c)
    elif operator=="cos":
        x=float((var1.split("cos(")[1]))
        k=math.cos(x)
        if A!="":
             c=float(A)*k
        else:
             c=k
        if c%1==0:
                 c=int(c)     
        data.set(c)
        var=str(c)
    elif operator=="tan":
        x=float((var1.split("tan(")[1]))
        k=math.tan(x)
        if A!="":
             c=float(A)*k
        else:
             c=k
        if c%1==0:
                 c=int(c)     
        data.set(c)
        var=str(c)
    elif operator=="log":
        x=float((var1.split("log(")[1]))
        k=math.log10(x)
        if A!="":
             c=float(A)*k
        else:
             c=k
        if c%1==0:
                 c=int(c)     
        data.set(c)
        var=str(c)    
root=tkinter.Tk()
root.geometry("550x400+300+300")
root.resizable(0,0)
root.title("Calculator")
      
data=StringVar()
lb1=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Britannic Bold",20),
    textvariable=data,
    background="#456372",
    fg="#000000",)    
lb1.pack(expand=True, fill="both",)

data1=StringVar()
lb1=Label(
    root,
    text="Label",
    anchor=SE,
    font=("Bahnschrift SemiBold",15),
    textvariable=data1,
    background="#FFE4C4",
    fg="#000000",)    
lb1.pack(expand=True, fill="both",)

btnrow1=Frame(root,bg="#1E1E1E")
btnrow1.pack(expand=True, fill="both",)

btnrow2=Frame(root)
btnrow2.pack(expand=True, fill="both",)

btnrow3=Frame(root)
btnrow3.pack(expand=True, fill="both",)

btnrow4=Frame(root)
btnrow4.pack(expand=True, fill="both",)

btnrow5=Frame(root)
btnrow5.pack(expand=True, fill="both",)

btn1=Button(
    btnrow2,
    text="1",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_1_isclicked,)
btn1.pack(side=LEFT,expand=True,fill="both",)

btn2=Button(
    btnrow2,
    text="2",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_2_isclicked,)
btn2.pack(side=LEFT,expand=True,fill="both",)

btn3=Button(
    btnrow2,
    text="3",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_3_isclicked,)
btn3.pack(side=LEFT,expand=True,fill="both",)

btn11=Button(
    btnrow2,
    text="+",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_plus_isclicked,)
btn11.pack(side=LEFT,expand=True,fill="both",)

btn12=Button(
    btnrow2,
    text="^",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_pow_isclicked,)
btn12.pack(side=LEFT,expand=True,fill="both",)

btn13=Button(
    btnrow2,
    text="<",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_back_isclicked,)
btn13.pack(side=LEFT,expand=True,fill="both",)

btn14=Button(
    btnrow2,
    text="sin",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_sin_isclicked,)
btn14.pack(side=LEFT,expand=True,fill="both",)

btn4=Button(
    btnrow3,
    text="4",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_4_isclicked,)
btn4.pack(side=LEFT,expand=True,fill="both",)

btn5=Button(
    btnrow3,
    text="5",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_5_isclicked,)
btn5.pack(side=LEFT,expand=True,fill="both",)

btn6=Button(
    btnrow3,
    text="6",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_6_isclicked,)
btn6.pack(side=LEFT,expand=True,fill="both",)

btn22=Button(
    btnrow3,
    text="-",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_min_isclicked,)
btn22.pack(side=LEFT,expand=True,fill="both",)

btn23=Button(
    btnrow3,
    text="%",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_per_isclicked,)
btn23.pack(side=LEFT,expand=True,fill="both",)

btn24=Button(
    btnrow3,
    text="e",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_e_isclicked,)
btn24.pack(side=LEFT,expand=True,fill="both",)

btn25=Button(
    btnrow3,
    text="cos",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_cos_isclicked,)
btn25.pack(side=LEFT,expand=True,fill="both",)


btn7=Button(
    btnrow4,
    text="7",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_7_isclicked,)
btn7.pack(side=LEFT,expand=True,fill="both",)

btn8=Button(
    btnrow4,
    text="8",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_8_isclicked,)
btn8.pack(side=LEFT,expand=True,fill="both",)

btn9=Button(
    btnrow4,
    text="9",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_9_isclicked,)
btn9.pack(side=LEFT,expand=True,fill="both",)

btn33=Button(
    btnrow4,
    text="x",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_pro_isclicked,)
btn33.pack(side=LEFT,expand=True,fill="both",)

btn34=Button(
    btnrow4,
    text="√",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_squareroot_isclicked,)
btn34.pack(side=LEFT,expand=True,fill="both",)

btn35=Button(
    btnrow4,
    text="π",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_pi_isclicked,)
btn35.pack(side=LEFT,expand=True,fill="both",)

btn36=Button(
    btnrow4,
    text="tan",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_tan_isclicked,)
btn36.pack(side=LEFT,expand=True,fill="both",)

btnC=Button(
    btnrow5,
    text="C",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_C_isclicked,)
btnC.pack(side=LEFT,expand=True,fill="both",)

btn0=Button(
    btnrow5,
    text="0",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_0_isclicked,)
btn0.pack(side=LEFT,expand=True,fill="both",)

btn43=Button(
    btnrow5,
    text="=",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=result,)
btn43.pack(side=LEFT,expand=True,fill="both",)
btn44=Button(
    btnrow5,
    text="/",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_div_isclicked,)
btn44.pack(side=LEFT,expand=True,fill="both",)

btn45=Button(
    btnrow5,
    text="!",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_factorial_isclicked,)
btn45.pack(side=LEFT,expand=True,fill="both",)

btn46=Button(
    btnrow5,
    text=".",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_dot_isclicked,)
btn46.pack(side=LEFT,expand=True,fill="both",)

btn47=Button(
    btnrow5,
    text="log",
    font=("Verdana",20),
    relief=GROOVE,
    border=0,
    command=btn_log_isclicked,)
btn47.pack(side=LEFT,expand=True,fill="both",)
root.mainloop()
