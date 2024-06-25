from tkinter import *

root = Tk()
root.title('Minha Primeira Janela')

frase = """Seja Bem-vidos ao Nosso Canal!
Se estiver gostando, deixe seu like.
"""

texto0 = Label(root, text=f'{frase}')
texto0.pack()

texto1 = Label(root, text='Texto 1')
texto1.pack()

# Cor de fundo (bg)
# Cor do Texto (fg)
# Fonte (font)]
# Largura (with)
# Altura (heigth)
# Borda (borderwidth) - Dedfine a largura da borda botão
# Estilo de Borda (relief)
# RAISED, SUNKEN, FLAT, GROOVE, RIDGE

#  Alinha à direita 'e' e outras opções de ancoragem incluem 'w' (esquerda), 
# 'n' (topo), 's' (baixo), 'nw' (canto superior esquerdo), 
# 'ne' (canto superior direito), 'sw' (canto inferior esquerdo) 
# e 'se' (canto inferior direito).

texto2 = Label(root, text='Texto 2', bg='blue', fg='yellow')
texto2.pack()

texto3 = Label(root, text='Texto 3', font=('Rupee Foradian', 16, 'bold'))
texto3.pack()

texto4 = Label(root, text='Texto 4',bg='yellow', fg='blue', width=20, height=3)
texto4.pack()

texto5 = Label(root, text='Texto 5',bg='yellow', fg='blue', padx=10, pady=5)
texto5.pack()

texto6 = Label(root, text='Texto 6',anchor='w')
texto6.pack(anchor='w')

texto7 = Label(root, text='Texto 7', bg='yellow', fg='blue', relief=RAISED, borderwidth=10)
texto7.pack()
texto8 = Label(root, text='Texto 8', relief=RAISED, font=('Rupee Foradian', 16, 'bold'))
texto8.pack()
texto9 = Label(root, text='Texto 9', relief=SUNKEN, font=('Rupee Foradian', 16, 'bold'))
texto9.pack()
texto10 = Label(root, text='Texto 10', relief=FLAT, font=('Rupee Foradian', 16, 'bold'))
texto10.pack()
texto11 = Label(root, text='Texto 11', relief=GROOVE, font=('Rupee Foradian', 16, 'bold'))
texto11.pack()
texto12 = Label(root, text='Texto 12', relief=RIDGE, font=('Rupee Foradian', 16, 'bold'))
texto12.pack()

root.mainloop()