from tkinter import *

janela = Tk()

janela.geometry('300x150')

janela.title('Janela Principal')


frame_sexo = Frame(janela)
frame_sexo.grid(row=1, column=0, columnspan=2)

Label(frame_sexo, text='Sexo:', font=20).pack(side=LEFT)

def informacao():
    sexo = var_sexo.get()

    if sexo == 'F':
        print(f'Você selecionou o sexo: {sexo}eminino')
    elif sexo == 'M':
        print(f'Você selecionou o sexo: {sexo}asculino')
    else:
        print(f'Você não selecionou nenhuma das opções!')


# variable -> Variável de controle que rastreia o estado do checkbutton
# onvalue -> Valor quando o checkbutton está marcado
# offvalue -> Valor quando o checkbutton está desmarcado
        
var_sexo = StringVar()
sexoFeminino = Checkbutton(frame_sexo, text='F', variable=var_sexo, onvalue='F', offvalue='', font=20)
sexoMasculino = Checkbutton(frame_sexo, text='M', variable=var_sexo, onvalue='M', offvalue='', font=20)
sexoFeminino.pack(side=LEFT)
sexoMasculino.pack(side=LEFT)

frame_botao = Frame(janela)
frame_botao .grid(row=2, column=0, columnspan=2)

botao = Button(frame_botao, text='Enviar', command=informacao, font=20)
botao.pack()


janela.mainloop()