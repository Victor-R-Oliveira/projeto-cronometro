from tkinter import*

cor_de_fundo = "#0f0f0f"

janela = Tk()
janela.geometry('360x360')
janela.title('Cornômetro')
janela.config(bg = cor_de_fundo)
janela.resizable(width=False, height=False)
janela.iconphoto(False, PhotoImage(file='cronometro.png'))

tempo ='00:00:00'
rodar = False
contador = 0

def iniciar():
    global rodar, contador
    rodar = True
    contar()


def contar():
    global contador, tempo, rodar
    
    if rodar:
        
        contador += 1
        horas = contador // 3600
        minutos = (contador % 3600) // 60
        segundos = contador % 60
        
        
        tempo = f'{horas:02}:{minutos:02}:{segundos:02}'
        
        
        label_tempo['text'] = tempo
        
        
        janela.after(1000, contar)


def pausar():
    global rodar
    rodar = False


def reiniciar():
    global contador, tempo, rodar
    rodar = False
    contador = 0
    tempo = '00:00:00'
    label_tempo['text'] = tempo


#----------------------------------------------------------------------------------

label_nome = Label(janela,width=10,height=2,text='Cronômetro',fg='#f0f1f2',bg=cor_de_fundo,font=('Arial 10'))
label_nome.place(relx=0.5, rely=0.15, anchor=CENTER)

label_tempo = Label(janela,text='00:00:00',fg='#0eeb49',bg=cor_de_fundo,font=('Arial 50 bold'))
label_tempo.place(relx=0.5, rely=0.4, anchor=CENTER)

#----------------------------------------------------------------------------------
botao_iniciar = Button(janela,command=iniciar,width=10,height=2,text='Iniciar',fg="white",background= cor_de_fundo, relief='raised')
botao_iniciar.place(relx=0.2, rely=0.8,anchor=CENTER)

botao_pausar = Button(janela,command=pausar,width=10,height=2,text='Pausar',fg="white",background= cor_de_fundo, relief='raised')
botao_pausar.place(relx=0.5, rely=0.8,anchor=CENTER)

botao_reiniciar = Button(janela,command=reiniciar,width=10,height=2,text='Reiniciar',fg="white",background= cor_de_fundo, relief='raised')
botao_reiniciar.place(relx=0.8, rely=0.8,anchor=CENTER)


janela.mainloop()