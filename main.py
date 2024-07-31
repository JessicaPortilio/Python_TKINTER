from tkinter import*
from tkinter import Tk,StringVar, ttk
from tkinter import messagebox 
from PIL import Image,ImageTk
from tkinter import filedialog as fd
import sqlite3 as lite
########################## Calendar ####################################################
from tkcalendar import Calendar,DateEntry
from datetime import date
import sqlite3
from sqlite3 import Error


from tkinter import*
from tkinter import Tk,StringVar, ttk
from tkinter import messagebox 
from PIL import Image,ImageTk
from tkinter import filedialog as fd
import sqlite3 as lite
########################## Calendar ####################################################
from tkcalendar import Calendar,DateEntry
from datetime import date
import sqlite3
from sqlite3 import Error
from comandos import *
import pygetwindow 


import comandos
import cad_produtos 

con = lite.connect('banco.db')



 

######### Cores ############

co0 ="#2e2d2b" # preta
co1 ="#feffff" # branca
co2 ="#4fa882" # verde
co3 ="#38576b" # valor
co4 ="#403d3d" # letra
co5 ="#e06636" # - profit
co6 ="#038cfc" # azul
co7 ="#3fbfb9" # verde
co8 ="#263238" # + verde
co9 ="#e9edf5" # + verde
co10 = "#004338"# vermelho   

janela_cliente =Tk() ### a janela###
janela_cliente.title('Locação de Equipamentos / Vilmar Ferreira da Silva')
#janela_produto.icone(r"C:\Users\User\Desktop\icones.ico")
janela_cliente.geometry("960x600") ### tamanho da janela ###
janela_cliente.configure(background=co9)
janela_cliente.wm_title("Cadastro de Pessoas / Vilmar Ferreira da Silva") ### nome da janela ###
janela_cliente.resizable(width=False,height=False) ## maximinizar ###
style = ttk.Style(janela_cliente)
style.theme_use("clam")    

def janela_cad_produtos():
    


    


groupBoxdados = LabelFrame(janela_cliente,text="Dados Cadastrais",padx=15,pady=15)
groupBoxdados.place(x=10,y=0,width=800,height=100)

groupBox = LabelFrame(janela_cliente,text="Endereço",padx=20,pady=20)
groupBox.place(x=10,y=100,width=800,height=100)

groupBoxpesquisa = LabelFrame(janela_cliente,padx=20,pady=20)
groupBoxpesquisa.place(x=10,y=238,width=940,height=353)



############################################# nome ###################################################################

labelnome=Label(groupBoxdados,text="Nome :",width=11,font=("arial",10))
labelnome.grid(row=1,column=0 ,sticky='e') #n s e w
t_nome=Entry(groupBoxdados,width=53)
t_nome.place(x=80,y=0,width=270,height=22) 

############################################# cpf ####################################################################

labelCpf=Label(groupBoxdados,text="Cpf :",width=11,font=("arial",10))
labelCpf.place(x=360,y=0,width=29,height=22)
t_Cpf=Entry(groupBoxdados,width=53)
t_Cpf.place(x=390,y=0,width=150,height=22)



labeltelefone=Label(groupBoxdados,text="Telefone Fixo:",width=11,font=("arial",10))
labeltelefone.place(x=517,y=35,width=80,height=22) #n s e w
t_fone=Entry(groupBoxdados,width=53)
t_fone.place(x=607,y=0,width=150,height=22)  

labelcelular=Label(groupBoxdados,text="Celular :",width=11,font=("arial",10))
labelcelular.place(x=544,y=0,width=57,height=22) #n s e w
t_celular=Entry(groupBoxdados,width=53)
t_celular.place(x=607,y=35,width=150,height=22)  

#################################################### frame endereço #####################################################

labelrua=Label(groupBox,text="Rua :",width=11,font=("arial",10))
labelrua.place(x=10,y=-10) #n s e w
t_rua=Entry(groupBox,width=53)
t_rua.place(x=80,y=-10,width=380,height=22) 

labelrua=Label(groupBox,text="Rua :",width=11,font=("arial",10))
labelrua.place(x=10,y=-10) #n s e w
t_rua=Entry(groupBox,width=53)
t_rua.place(x=80,y=-10,width=380,height=22) 

############################################# Cep ####################################################################

labelcep=Label(groupBox,text="Cep :",width=11,font=("arial",10))
labelcep.place(x=533,y=-10)
t_cep=Entry(groupBox,width=53)
t_cep.place(x=607,y=-10,width=150,height=22)

############################################# Bairro ##################################################################
# width = maior aumenta da letra  menor diminuir  a letra     
# y e height = move para baixo      X = menos move para esquerda X = maior move para direita

labelbairro=Label(groupBox,text="Bairro :",width=11,font=("arial",10))
labelbairro.place(x=27,y=25,width=43,height=22) #n s e w 
t_bairro=Entry(groupBox,width=53)
t_bairro.place(x=80,y=25,width=220,height=22)  

############################################# Cidade #####################################################################

labelcidade=Label(groupBox,text="Cidade :",width=11,font=("arial",10))
labelcidade.place(x=313,y=27,width=57,height=22) #n s e w
t_cidade=Entry(groupBox,width=53)
t_cidade.place(x=370,y=27,width=150,height=22) 

############################################# estado ################################################################

labelestado=Label(groupBox,text="Estado:",width=11,font=("arial",10))
labelestado.place(x=533,y=27,width=80,height=22) #n s e w
t_estado=Entry(groupBox,width=53)
t_estado.place(x=607,y=27,width=150,height=22)  

labelpesquisar=Label(janela_cliente,text="Pesquisar:",foreground=co6,width=11,font=("arial",10))
labelpesquisar.place(x=10,y=207,width=80,height=22) #n s e w
t_pesquisar=Entry(janela_cliente,width=53)
t_pesquisar.place(x=83,y=208,width=195,height=22)  

def sair():
    result = messagebox.askquestion("Pergunta /Cadastro de Cliente","Tem certeza que deseja sair?")
    if result== 'yes':
        janela_cliente.destroy()
        exit()


def excluir_registro():
    result = messagebox.askquestion("Pergunta /Cadastro de Cliente","Tem certeza que deseja excluir Registro?")
    if result== 'yes':
        deletar()
    





def Salvar_pessoas():
    cursor1=con.cursor()
    
    nome = t_nome.get()
    cpf = t_Cpf.get()
    celular = t_celular.get()
    fone = t_fone.get()
    rua = t_rua.get()
    cep = t_cep.get()
    bairro = t_bairro.get()
    cidade = t_cidade.get()
    estado = t_estado.get()
    
    lista=[nome,cpf,celular,fone,rua,cep,bairro,cidade,estado]

    for i in lista:
        if i=='':
            messagebox.showerror('Erro','Preencha todos os campos')
            
            return
            
    cursor1.execute("INSERT INTO pessoas(nome,cpf,celular,fone,rua,cep,bairro,cidade,estado) VALUES(?,?,?,?,?,?,?,?,?)",(nome,cpf,celular,fone,rua,cep,bairro,cidade,estado))
    con.commit()
    con.close
    messagebox.showinfo("Cadastro Pessoas","Dados inserido com Susseço!")
    limpar_campos()      
    
    mostrar()

def limpar_campos():
    t_nome.delete(0,'end')
    t_Cpf.delete(0,'end')
    t_celular.delete(0,'end')
    t_fone.delete(0,'end')
    t_rua.delete(0,'end')
    t_cep.delete(0,'end')
    t_bairro.delete(0,'end')
    t_cidade.delete(0,'end')
    t_estado.delete(0,'end')
    t_nome.focus()


def atualizar():
    
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']

        valor=treev_lista[0]
        
        t_nome.delete(0,'end')
        t_Cpf.delete(0,'end')
        t_celular.delete(0,'end')
        t_fone.delete(0,'end')
        t_rua.delete(0,'end')
        t_cep.delete(0,'end')
        t_bairro.delete(0,'end')
        t_cidade.delete(0,'end')
        t_estado.delete(0,'end')
    

        id =int(treev_lista[0])
        t_nome.insert(0,treev_lista[1])
        t_Cpf.insert(0,treev_lista[2])
        t_celular.insert(0,treev_lista[3])
        t_fone.insert(0,treev_lista[4])
        t_rua.insert(0,treev_lista[5])
        t_cep.insert(0,treev_lista[6])
        t_bairro.insert(0,treev_lista[7])
        t_cidade.insert(0,treev_lista[8])
        t_estado.insert(0,treev_lista[9])

        def update():
            global imagem, imagem_string, l_imagem


            nome = t_nome.get()
            cpf = t_Cpf.get()
            celular = t_celular.get()
            fone = t_fone.get()
            rua = t_rua.get()
            cep = t_cep.get()
            bairro = t_bairro.get()
            cidade = t_cidade.get()
            estado = t_estado.get()

            

            lista_atualizar = [nome,cpf,celular,fone,rua,cep,bairro,cidade,estado,id]

            for i in lista_atualizar:
                if i=='':
                    messagebox.showerror('Erro','Preencha todos os campos')
                    return
                
            atualizar_form(lista_atualizar) 
            messagebox.showinfo('Sucesso','Os dados foram Atualizados com sucesso')

            t_nome.delete(0,'end')
            t_Cpf.delete(0,'end')
            t_celular.delete(0,'end')
            t_fone.delete(0,'end')
            t_rua.delete(0,'end')
            t_cep.delete(0,'end')
            t_bairro.delete(0,'end')
            t_cidade.delete(0,'end')
            t_estado.delete(0,'end')

            B_comfirmar.destroy() 
            mostrar()
            
        B_comfirmar = Button(janela_cliente,command=update, image=img_salve,width=87,text='  Confirmar'.upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=('Ivy 8'),bg=co1,fg=co0)
        B_comfirmar.place(x=820,y=40) 
    
    except IndexError:
        messagebox.showerror('Erro','Seleciona os Dados da tabela')


def Pesquisa_pessoa():
        nome = input('t_pesquisar')
        resultado = comandos.Pesquisa_pessoa(nome)
        for linha in resultado:
            print(linha)
            mostrar
      


################  inserir a imagem nos botoes ##############################################################
img_salve= Image.open('salve.png')
img_salve = img_salve.resize((20,20))
img_salve = ImageTk.PhotoImage(img_salve)

img_novo = Image.open('novo.png')
img_novo = img_novo.resize((20,20))                                                                      
img_novo = ImageTk.PhotoImage(img_novo)

img_update = Image.open('atualizar.png')
img_update = img_update.resize((20,20))
img_update = ImageTk.PhotoImage(img_update)

img_delete = Image.open('deletar.png')
img_delete = img_delete.resize((20,20))
img_delete = ImageTk.PhotoImage(img_delete)

img_close = Image.open('sair.png')
img_close = img_close.resize((20,20))
img_close = ImageTk.PhotoImage(img_close)

img_pesquisar = Image.open('pesquisar.png')
img_pesquisar = img_pesquisar.resize((20,20))
img_pesquisar = ImageTk.PhotoImage(img_pesquisar)
#############################################################################################################

def deletar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        treev_lista = treev_dicionario['values']
        valor=treev_lista[0]
        
        deletar_form([valor])
    
        messagebox.showinfo('Sucesso','Os dados foram Excluido com sucesso')
        
        mostrar()
    except IndexError:
        messagebox.showerror('Erro','Seleciona os Dados da tabela')    


##################################### colocar botões no formulario ##########################################
################   Botão Atualizar ##########################################################################
B_atualizar = Button(janela_cliente,command=atualizar,image=img_update,width=87,text='  Atualizar'.upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=('Ivy 8'),bg=co1,fg=co0)
B_atualizar.place(x=820,y=70)

################   Botão Deletarr ###########################################################################
B_delete = Button(janela_cliente,command=excluir_registro,image=img_delete,width=87,text='  Deletar'.upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=('Ivy 8'),bg=co1,fg=co0)
B_delete.place(x=820,y=100)

################   Botão sair ###############################################################################
B_sair = Button(janela_cliente,command=sair,image=img_close,width=87,text='  Sair'.upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=('Ivy 8'),bg=co1,fg=co0)
B_sair.place(x=820,y=130)

################  inserir a imagem adicionar ################################################################
B_novo = Button(janela_cliente, image=img_novo,width=87,text='  Novo'.upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=('Ivy 8'),bg=co1,fg=co0)
B_novo.place(x=820,y=10)

B_inserir = Button(janela_cliente,command=Salvar_pessoas,image=img_salve,width=87,text='  Salvar'.upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=('Ivy 8'),bg=co1,fg=co0)
B_inserir.place(x=820,y=40)

B_pesquisar = Button(janela_cliente,command=Pesquisa_pessoa,image=img_pesquisar,width=87,text=' Pesquisar'.upper(),compound=LEFT,anchor=NW,overrelief=RIDGE,font=('Ivy 8'),bg=co1,fg='red')
B_pesquisar.place(x=290,y=205)

################   Botão adicionar ##########################################################################

def mostrar():
    global tree

    tabela_head =['Item','Nome','Cpf','Fone','Celular','Endereço','Bairro','Cidade','Estado']

    lista_itens = ver_form()

    tree = ttk.Treeview(groupBoxpesquisa, selectmode="extended",columns=tabela_head, show="headings")

######################  tabela vestical ,Horizontal ####################################################
    vsb = ttk.Scrollbar(groupBoxpesquisa, orient="vertical", command=tree.yview)
    hsb = ttk.Scrollbar(groupBoxpesquisa, orient="horizontal", command=tree.xview)
    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    tree.grid(column=0,row=0, sticky='nsew')
    vsb.grid(column=1,row=0, sticky='ns')
    hsb.grid(column=0,row=1, sticky='ew')

    tree.configure(yscrollcommand=vsb.set,xscrollcommand=hsb.set)
    tree.grid(column=0,row=0, sticky='nsew')
    vsb.grid(column=1,row=0, sticky='ns')
    hsb.grid(column=0,row=1, sticky='ew')
    groupBoxpesquisa.grid_rowconfigure(0,weight=12)

    hd=["center","nw","center","nw","nw","center","nw","center","center"]
    h=[45,190,100,95,95,110,80,90,80]
    n=0


    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        
        tree.column(col, width=h[n],anchor=hd[n])

        n+=1

######################### inserindo no data grid ########################################################
    for item in lista_itens:
        tree.insert('','end', values=item)

    quant_total = [0000,00]
    for iten in lista_itens:
        quant_total.append(iten[6])

# total_valor = sum(quant_total) 
# total_itens = len(quant_total)  

#l_total['text'] = 'R$ {:,.2f}'.format(total_valor)
# l_quan_total['text'] = total_itens
mostrar()  




janela_cliente.mainloop()


from tkinter import*
from tkinter import Tk,StringVar, ttk
from tkinter import messagebox 
from PIL import Image,ImageTk
from tkinter import filedialog as fd
import sqlite3 as lite
########################## Calendar ####################################################
from tkcalendar import Calendar,DateEntry
from datetime import date
import sqlite3
from sqlite3 import Error
from comandos import *
import pygetwindow 

import comandos

con = lite.connect('banco.db')



 

######### Cores ############

co0 ="#2e2d2b" # preta
co1 ="#feffff" # branca
co2 ="#4fa882" # verde
co3 ="#38576b" 