from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from funcoesgui import update_cblist
from matdb import mat_db_wdw


#Criando Banco de Dados de Materiais

conn = sqlite3.connect('materiais.db')
cursor1 = conn.cursor()
cursor1.execute(
  """SELECT count(name) FROM sqlite_master WHERE type='table'
  AND Name='listamateriais'; """)
if cursor1.fetchone()[0] != 1: #Checagem para ver se a table do database já existe, para o programa não dar erro
    cursor1.execute("""CREATE TABLE listamateriais (
        nome_mat text PRIMARY KEY,
        tensao_adm float
        )""")
conn.commit()
conn.close()

##############################################


#Gerando a Interface Principal da Janela Principal

root=Tk()

root.title("Programa Vaso de Pressão")

MainMenu=Menu(root)
filemenu = Menu(MainMenu, tearoff=0)
filemenu.add_command(label="Editar database de materiais",command=mat_db_wdw)
filemenu.add_separator()
filemenu.add_command(label="Sair",command=root.destroy)
MainMenu.add_cascade(label="Opções",menu=filemenu)


titulo=Label(root,text="Programa Vaso")
titulo.grid(row=0,columnspan=2)

frame1=LabelFrame(root,text="Dados de Entrada")
frame1.grid(padx=10,pady=10)

Nome1=Label(frame1,text="Nome do Projeto:")
Nome1.grid(row=1,column=0,sticky="W")

nome_proj1=Entry(frame1)
nome_proj1.grid(row=1,column=1,sticky="W")

diam=Label(frame1,text="Diâmetro do Costado(mm):")
diam.grid(row=2,column=0,sticky="W")

D1=Entry(frame1)
D1.grid(row=2,column=1,sticky="W")

ejunta=Label(frame1,text="Eficiência de Junta:")
ejunta.grid(row=3,column=0,sticky="W")

ejunta1=Entry(frame1)
ejunta1.grid(row=3,column=1,sticky="W")

casco=IntVar()
tipocasco=Label(frame1,text="Tipo de Casco:")
tipocasco.grid(row=4,column=0,sticky="W")

tc1=Radiobutton(frame1,text="Cilíndrico",variable=casco,value=1)
tc1.grid(row=4,column=1,sticky="W")

tc2=Radiobutton(frame1,text="Esférico",variable=casco,value=2)
tc2.grid(row=5,column=1,sticky="W")

tipo_materiais=Label(frame1,text="Tipo de material do casco:")
tipo_materiais.grid(row=6,column=0,sticky="W")

lista_mat_casco=ttk.Combobox(frame1,postcommand=lambda: update_cblist(lista_mat_casco))
lista_mat_casco.set("Escolha uma opção")
lista_mat_casco.grid(row=6,column=1)

root.config(menu = MainMenu)
root.mainloop()