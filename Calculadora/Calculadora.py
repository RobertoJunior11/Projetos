from tkinter import *
from tkinter import ttk
import tkinter.font as tkFont

#Cores

corPreta = '#030303'
corCinzaEscuro = '#444'
corCinzaClaro = '#a7a7a7'
corBranca = '#fff'
corVermelhoClaro = '#fa3e3e'

#Janela

janela = Tk()
janela.title('Calculadora')
janela.geometry('235x318')
janela.config(bg=corPreta)

#Criando frames

frame_tela = Frame(janela, width=236, height=50,bg=corPreta)
frame_tela.grid(row=0, column=0)

frame_corpo = Frame(janela, width=236, height=268,bg=corPreta)
frame_corpo.grid(row=1, column=0)

#Variável todos os valores

todos_valores = ''

#Criando label

digito = StringVar()

#Criando função

def entrar_valores(event):
    global todos_valores
    todos_valores = todos_valores + str(event)
    
    #Passando valor para tela

    digito.set(todos_valores)

#Criando função para calcular

def calcular():
    global todos_valores
    resultado = round(eval(todos_valores), 2)
    todos_valores = str(resultado)
    digito.set(todos_valores)

#Criando função -1

def negativo():
    global todos_valores
    resultado = eval(todos_valores) * -1
    todos_valores = str(resultado)
    digito.set(todos_valores)

#Criando função limpar a tela

def limpar_tela():
    global todos_valores
    todos_valores = ''
    digito.set('')

#Display

app_label = Label(frame_tela, textvariable=digito, width=16, height=2, anchor='e',bg=corPreta, fg=corBranca, font=('Ivy 18'))
app_label.place(x=0, y=0)

#Criando botões

b_1 = Button(frame_corpo, command = limpar_tela, text='C', width=5, height=2, bg=corCinzaClaro, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_1.place(x=12, y=10.5)
b_2 = Button(frame_corpo, command = negativo, text='+/-', width=5, height=2, bg=corCinzaClaro, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_2.place(x=68, y=10.5)
b_3 = Button(frame_corpo, command = lambda: entrar_valores('%'), text='%', width=5, height=2, bg=corCinzaClaro, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_3.place(x=124, y=10.5)
b_4 = Button(frame_corpo, command = lambda: entrar_valores('/'), text='/', width=5, height=2, bg=corVermelhoClaro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_4.place(x=180, y=10.5)

b_5 = Button(frame_corpo, command = lambda: entrar_valores('7'), text='7', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_5.place(x=12, y=62)
b_6 = Button(frame_corpo, command = lambda: entrar_valores('8'), text='8', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_6.place(x=68, y=62)
b_7 = Button(frame_corpo, command = lambda: entrar_valores('9'), text='9', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_7.place(x=124, y=62)
b_8 = Button(frame_corpo, command = lambda: entrar_valores('*'), text='X', width=5, height=2, bg=corVermelhoClaro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_8.place(x=180, y=62)

b_9 = Button(frame_corpo, command = lambda: entrar_valores('4'), text='4', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_9.place(x=12, y=113.5)
b_10 = Button(frame_corpo, command = lambda: entrar_valores('5'), text='5', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_10.place(x=68, y=113.5)
b_11 = Button(frame_corpo, command = lambda: entrar_valores('6'), text='6', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_11.place(x=124, y=113.5)
b_12 = Button(frame_corpo, command = lambda: entrar_valores('-'), text='-', width=5, height=2, bg=corVermelhoClaro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_12.place(x=180, y=113.5)

b_13 = Button(frame_corpo, command = lambda: entrar_valores('1'), text='1', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_13.place(x=12, y=165)
b_14 = Button(frame_corpo, command = lambda: entrar_valores('2'), text='2', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_14.place(x=68, y=165)
b_15 = Button(frame_corpo, command = lambda: entrar_valores('3'), text='3', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_15.place(x=124, y=165)
b_16 = Button(frame_corpo, command = lambda: entrar_valores('+'), text='+', width=5, height=2, bg=corVermelhoClaro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_16.place(x=180, y=165)

b_17 = Button(frame_corpo, command = lambda: entrar_valores('0'), text='0', width=9, height=2, anchor='w', padx=15, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_17.place(x=12, y=216.5)
b_18 = Button(frame_corpo, command = lambda: entrar_valores(','), text=',', width=5, height=2, bg=corCinzaEscuro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_18.place(x=124, y=216.5)
b_19 = Button(frame_corpo, command = calcular, text='=', width=5, height=2, bg=corVermelhoClaro, fg=corBranca, font=('Ivy 9 bold'), relief=RAISED, overrelief=RIDGE)
b_19.place(x=180, y=216.5)


janela.mainloop()