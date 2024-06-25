from tkinter import *
from PIL import ImageTk, Image

janela = Tk()

janela.geometry('520x300')

janela.title('Interface Gráfica')

caminho_image = Image.open('fundo.jpg')
imagem_redimensionada = caminho_image.resize((520,300), Image.LANCZOS)
image_de_fundo = ImageTk.PhotoImage(imagem_redimensionada)

label_imagem_de_fundo = Label(janela, image=image_de_fundo)
label_imagem_de_fundo.place(x=0, y=0, relwidth=1, relheight=1)

texto1 = Label(janela, text='Texto sobre a imagem de fundo', font=('Roman', 16, 'bold'), bg='lightblue')
texto1.pack(pady=20)

janela.mainloop()