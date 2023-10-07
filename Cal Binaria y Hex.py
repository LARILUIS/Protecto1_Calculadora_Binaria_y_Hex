from tkinter import *

ventana = Tk()
ventana.title("calculadora")
ventana.configure(bg= 'blue')

i = 0
base_numerica = 10 #Inicialmente, la base es decimal

#entrada
e_texto = Entry(ventana, font = ("Century 28"))
e_texto.grid(row = 0, column = 0, columnspan = 4, padx = 5, pady=5)

#Funciones

import random
    
    
def changeBG():
    ventana.config(background = 'green')
    colors =["black", "pink", "yellow", "green", "purple", "red", "gray"]
    random_colors = random.choice(colors)
    ventana.config(backgroup = random_colors)
    
    
def click_boton(valor):
    global i
    e_texto.insert(i, valor)
    i += 1
    
def borrar():
    global i
    e_texto.delete(0, END)
    i = 0

def cambiar_base(base):
    global base_numerica
    base_numerica = base
    borrar()

def BACK ():
    global i
    i = i-1 
    e_texto.delete(i, END)
    
    
def hacer_operacion():
    ecuacion = e_texto.get()
    resultado = ""
    try:
        if base_numerica == 10:
            resultado = str(eval(ecuacion))
        elif base_numerica == 2:
            resultado = bin(eval(ecuacion))[2:]
        elif base_numerica == 16:
            resultado = hex(eval(ecuacion))[2:]
        borrar()
        e_texto.insert(0, resultado)
    except Exception as e:
        borrar()
        e_texto.insert(0, "Error")
        
#dissable 
def BOTON_BLOQ():
    if (boton_ON['text'] == 'ON'):
     boton_ON ['text'] = 'OFF'
    else:
        boton_ON ['text'] = 'ON' 
    
    if (boton1 ['state'] == NORMAL ):
        boton1['state'] = DISABLED
    
    else: 
        boton1['state']= NORMAL     
        
    if (boton2 ['state'] == NORMAL ):
        boton2['state'] = DISABLED
    
    else: 
        boton2['state']= NORMAL  
        
    if (boton3 ['state'] == NORMAL ):
        boton3['state'] = DISABLED
    
    else: 
        boton3['state']= NORMAL  
        
    if (boton4 ['state'] == NORMAL ):
        boton4['state'] = DISABLED
    
    else: 
        boton4['state']= NORMAL
    
    if (boton5 ['state'] == NORMAL ):
        boton5['state'] = DISABLED
    
    else: 
        boton5['state']= NORMAL 
        
    if (boton6 ['state'] == NORMAL ):
        boton6['state'] = DISABLED
    
    else: 
        boton6['state']= NORMAL  
        
    if (boton7 ['state'] == NORMAL ):
        boton7['state'] = DISABLED
    
    else: 
        boton7['state']= NORMAL  
        
    if (boton8 ['state'] == NORMAL):
        boton8['state'] = DISABLED
        
    else:
        boton8['state']= NORMAL
        
    if (boton9 ['state'] == NORMAL):
        boton9['state'] = DISABLED
        
    else:
        boton9['state'] = NORMAL
    
    
#Botones
boton_ON = Button (ventana, text = "ON", width=5, height=2, command = lambda: BOTON_BLOQ (), bg="red", cursor = "pirate")
boton0 = Button(ventana, text = "0", width = 20, height = 3, command = lambda: click_boton(0), bg="red", cursor = "pirate")
boton1 = Button(ventana, text = "1", width = 8, height = 3, command = lambda: click_boton(1), bg="red")
boton2 = Button(ventana, text = "2", width = 8, height = 3, command = lambda: click_boton(2), bg="red")
boton3 = Button(ventana, text = "3", width = 8, height = 3, command = lambda: click_boton(3), bg="red")
boton4 = Button(ventana, text = "4", width = 8, height = 3, command = lambda: click_boton(4), bg="red")

boton5 = Button(ventana, text = "5", width = 8, height = 3, command = lambda: click_boton(5), bg="red")
boton6 = Button(ventana, text = "6", width = 8, height = 3, command = lambda: click_boton(6), bg="red")
boton7 = Button(ventana, text = "7", width = 8, height = 3, command = lambda: click_boton(7), bg="red")
boton8 = Button(ventana, text = "8", width = 8, height = 3, command = lambda: click_boton(8), bg="red")
boton9 = Button(ventana, text = "9", width = 8, height = 3, command = lambda: click_boton(9), bg="red")

botonA = Button(ventana, text = "A", width = 8, height = 2, command = lambda: click_boton("A"), bg="red")
botonB = Button(ventana, text = "B", width = 8, height = 2, command = lambda: click_boton("B"), bg="red")
botonC = Button(ventana, text = "C", width = 8, height = 2, command = lambda: click_boton("C"), bg="red")
botonD = Button(ventana, text = "D", width = 8, height = 2, command = lambda: click_boton("D"), bg="red")
botonE = Button(ventana, text = "E", width = 8, height = 2, command = lambda: click_boton("E"), bg="red")
botonF = Button(ventana, text = "F", width = 8, height = 2, command = lambda: click_boton("F"), bg="red")

botonDecimal = Button(ventana, text = "Dec", width = 8, height = 2, activebackground= 'purple', command = lambda: cambiar_base(10), bg="red", cursor = "pirate")
botonBinario = Button(ventana, text = "Bin", width = 8, height = 2, activebackground= 'pink', command = lambda: cambiar_base(2), bg="red", cursor = "pirate")
botonHexadecimal = Button(ventana, text = "Hex", width = 8, height = 2,activebackground= 'brown', command = lambda: cambiar_base(16), bg="red", cursor = "pirate")

boton_AC = Button(ventana, text = "AC", width = 10, height = 3,command = lambda: borrar(), bg="red")
boton_parentesis1 = Button(ventana, text = "(", width = 8, height = 3,command = lambda: click_boton("("), bg="red")
boton_parentesis2 = Button(ventana, text = ")", width = 8, height = 3, command = lambda: click_boton(")"), bg="red")
boton_punto = Button(ventana, text = ".", width = 8, height = 3,command = lambda: click_boton("."), bg="red")
boton_BACK = Button(ventana, text = "->", width = 12, height = 3,command = lambda: BACK(), bg="red")


boton_div = Button(ventana, text = "/", width = 8, height = 3,command = lambda: click_boton("/"), bg="red")
boton_mult = Button(ventana, text = "x", width = 8, height = 3,command = lambda: click_boton("*"), bg="red")
boton_sum = Button(ventana, text = "+", width = 8, height = 3,command = lambda: click_boton("+"), bg="red")
boton_rest = Button(ventana, text = "-", width = 8, height = 3,command = lambda: click_boton("-"), bg="red", cursor = "pirate")
boton_igual = Button(ventana, text = "=", width = 12, height = 3, activebackground= 'yellow', command = lambda: hacer_operacion(), bg="red",  cursor = "pirate")

#agregar  botones en pantalla
botonDecimal.grid(row=1, column=1, padx=5, pady=5)
botonBinario.grid(row=1, column=2, padx=5, pady=5)
botonHexadecimal.grid(row=1, column=3, padx=5, pady=5)
boton_BACK.grid(row=1, column=0, padx=5, pady=5)

boton_AC.grid(row = 2, column= 0, padx= 5, pady = 5)
boton_parentesis1.grid(row = 2, column= 1, padx= 5, pady = 5)
boton_parentesis2.grid(row = 2, column= 2, padx= 5, pady = 5)
boton_div.grid(row = 2, column= 3, padx= 5, pady = 5)


boton7.grid(row = 3, column= 0, padx= 5, pady = 5)
boton8.grid(row = 3, column= 1, padx= 5, pady = 5)
boton9.grid(row = 3, column= 2, padx= 5, pady = 5)
boton_mult.grid(row = 3, column= 3, padx= 5, pady = 5)

boton4.grid(row = 4, column= 0, padx= 5, pady = 5)
boton5.grid(row = 4, column= 1, padx= 5, pady = 5)
boton6.grid(row = 4, column= 2, padx= 5, pady = 5)
boton_sum.grid(row = 4, column= 3, padx= 5, pady = 5)

boton1.grid(row = 5, column= 0, padx= 5, pady = 5)
boton2.grid(row = 5, column= 1, padx= 5, pady = 5)
boton3.grid(row = 5, column= 2, padx= 5, pady = 5)
boton_rest.grid(row = 5, column= 3, padx= 5, pady = 5)

boton0.grid(row = 6, column= 0,columnspan = 2, padx= 5, pady = 5)
boton_punto.grid(row = 6, column= 2, padx= 5, pady = 5)
boton_igual.grid(row = 6, column= 3, padx= 5, pady = 5)

botonA.grid(row = 7, column = 0, padx = 5, pady = 5)
botonB.grid(row = 7, column = 1, padx = 5, pady = 5)
botonC.grid(row = 7, column = 2, padx = 5, pady = 5)
botonD.grid(row = 7, column = 3, padx = 5, pady = 5)
botonE.grid(row = 8, column = 0, padx = 5, pady = 5)
botonF.grid(row = 8, column = 1, padx = 5, pady = 5)
boton_ON.grid (row= 8, column=2, padx=5, pady=5)

ventana.mainloop()