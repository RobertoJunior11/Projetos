'''
Roberto Junior, 2024/05/04
Title: Seletor de Cores (Color Picker)
'''

from tkinter import *
import tkinter.messagebox

# Criando cores

cor1 = "#000000"  # Preta/Black
cor2 = "#ffffff"  # Branca/White
cor3 = "#adadad"  # Cinza/Grey

# Criando a janela

janela = Tk()
janela.geometry('560x205')
janela.configure(bg=cor2)

# Configurando a janela

tela = Label(janela, bg=cor3, width=40, height=10)
tela.grid(row=0, column=0, padx=10)

frame_direita = Frame(janela, bg=cor2)
frame_direita.grid(row=0, column=1, padx=10)

frame_baixo = Frame(janela, bg=cor2)
frame_baixo.grid(row=1, column=0, columnspan=2, pady=10)

# Função Scale

def escala(valor):
    r=scale_red.get()
    g=scale_green.get()
    b=scale_blue.get()

    rgb = f'{r}, {g}, {b}'

    hexadecimal = "#%02x%02x%02x" % (r, g, b)

    # Adicionando cor na tela

    tela['bg'] = hexadecimal

    # Adicionando Hexadecimal na Caixa

    caixa_cor.delete(0,END)
    caixa_cor.insert(0, hexadecimal)

# Função Copiar

def click():
    
    # Mensagem

    tkinter.messagebox.showinfo('Seletor de Cores', 'Cor copiada com sucesso!')

    clip = Tk()
    clip.withdraw()
    clip.clipboard_clear()
    clip.clipboard_append(caixa_cor.get())
    clip.destroy()

# Configurando o frame direita

red = Label(frame_direita, text= 'Red', width=7, bg=cor2, fg='red', anchor='nw', font=('Time New Roman', 12, 'bold'))
red.grid(row=0, column=0)
scale_red = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor2, fg='red', orient=HORIZONTAL)
scale_red.grid(row=0, column=1)

green = Label(frame_direita, text= 'Green', width=7, bg=cor2, fg='green', anchor='nw', font=('Time New Roman', 12, 'bold'))
green.grid(row=1, column=0)
scale_green = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor2, fg='green', orient=HORIZONTAL)
scale_green.grid(row=1, column=1)

blue = Label(frame_direita, text= 'Blue', width=7, bg=cor2, fg='blue', anchor='nw', font=('Time New Roman', 12, 'bold'))
blue.grid(row=2, column=0)
scale_blue = Scale(frame_direita, command=escala, from_=0, to=255, length=150, bg=cor2, fg='blue', orient=HORIZONTAL)
scale_blue.grid(row=2, column=1)

# Configurando o Cod Hex

codhex = Label(frame_baixo, text= 'Código HEX: ', bg=cor2, font=('Ivy', 10, 'bold'))
codhex.grid(row=0, column=0)

# Caixa

caixa_cor = Entry(frame_baixo, width=12, font=('Ivy', 10, 'bold'), justify=CENTER)
caixa_cor.grid(row=0, column=1, padx=5)

# Botão Copiar

copiar = Button(frame_baixo, command=click, text='Copiar', bg=cor2, font=('Ivy', 8, 'bold'), relief=RAISED, overrelief=RIDGE)
copiar.grid(row=0, column=2, padx=10)

# Nome da Ferramenta

app_nome = Label(frame_baixo, text='Seletor de Cores', bg=cor2, font=('Ivy', 15, 'bold'))
app_nome.grid(row=0, column=3, padx=55)

janela.mainloop()
