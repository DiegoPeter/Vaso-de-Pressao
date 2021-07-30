from tkinter import *
import sqlite3
from tkinter import ttk
from funcoesgui import update_cblist, show_tampo, hide_tampo, show_angcone, hide_angcone
from matdb import mat_db_wdw
from calculos import calculate

# Criando Banco de Dados de Materiais

conn = sqlite3.connect('materiais.db')
cursor1 = conn.cursor()
cursor1.execute("""
CREATE TABLE IF NOT EXISTS listamateriais (
  nome_mat text PRIMARY KEY,
  tensao_adm float
)
""")
conn.commit()
conn.close()

# Gerando a Interface Principal da Janela Principal

root = Tk()

root.title("Programa Vaso de Pressão")

MainMenu = Menu(root)
filemenu = Menu(MainMenu, tearoff=0)
filemenu.add_command(label="Editar database de materiais", command=mat_db_wdw)
filemenu.add_separator()
filemenu.add_command(label="Sair", command=root.destroy)
MainMenu.add_cascade(label="Opções", menu=filemenu)


titulo = Label(root, text="Programa Vaso")
titulo.grid(row=0, columnspan=2)

frame1 = LabelFrame(root, text="Dados de Entrada")
frame1.grid(padx=10, pady=10)

Nome1 = Label(frame1, text="Nome do projeto:")
Nome1.grid(row=1, column=0, sticky="W")

nome_proj1 = Entry(frame1)
nome_proj1.grid(row=1, column=1, sticky="W")

diam = Label(frame1, text="Diâmetro do costado(mm):")
diam.grid(row=2, column=0, sticky="W")

D1 = Entry(frame1)
D1.grid(row=2, column=1, sticky="W")

pre_proj = Label(frame1, text="Pressão de Projeto(Mpa):")
pre_proj.grid(row=3, column=0, sticky='W')

pre_proj1 = Entry(frame1)
pre_proj1.grid(row=3, column=1, sticky='W')

ejunta = Label(frame1, text="Eficiência de junta:")
ejunta.grid(row=4, column=0, sticky="W")

ejunta1 = Entry(frame1)
ejunta1.grid(row=4, column=1, sticky="W")

casco = IntVar()
tipocasco = Label(frame1, text="Tipo de casco:")
tipocasco.grid(row=5, column=0, sticky="W")

tc1 = Radiobutton(frame1, text="Cilíndrico", variable=casco, value=1, command=lambda: show_tampo(
    tipotampo, tp1, tp2, tp3, tp4, tp5, tipo_mat_tp, lista_mat_tp))
tc1.grid(row=5, column=1, sticky="W")

tc2 = Radiobutton(frame1, text="Esférico", variable=casco, value=2, command=lambda: hide_tampo(
    tipotampo, tp1, tp2, tp3, tp4, tp5, tipo_mat_tp, lista_mat_tp, ang_cone, ang_cone1))
tc2.grid(row=6, column=1, sticky="W")

tipo_materiais = Label(frame1, text="Tipo de material do casco:")
tipo_materiais.grid(row=7, column=0, sticky="W")

lista_mat_casco = ttk.Combobox(
    frame1, postcommand=lambda: update_cblist(lista_mat_casco))
lista_mat_casco.set("Escolha uma opção:")
lista_mat_casco.grid(row=7, column=1)

tampo = IntVar()
tipotampo = Label(frame1, text="Tipo de tampo:")

tp1 = Radiobutton(frame1, text="Elipsóidal 2:1", variable=tampo,
                  value=1, command=lambda: hide_angcone(ang_cone, ang_cone1))

tp2 = Radiobutton(frame1, text="Toro Esférico", variable=tampo,
                  value=2, command=lambda: hide_angcone(ang_cone, ang_cone1))

tp3 = Radiobutton(frame1, text="Hemisférico", variable=tampo,
                  value=3, command=lambda: hide_angcone(ang_cone, ang_cone1))

tp4 = Radiobutton(frame1, text="Cônico", variable=tampo, value=4,
                  command=lambda: show_angcone(ang_cone, ang_cone1))

tp5 = Radiobutton(frame1, text="Toro Cônico", variable=tampo,
                  value=5, command=lambda: show_angcone(ang_cone, ang_cone1))

ang_cone = Label(frame1, text="Ângulo de cone(em graus):")

ang_cone1 = Entry(frame1)

tipo_mat_tp = Label(frame1, text="Tipo de material do tampo:")

lista_mat_tp = ttk.Combobox(
    frame1, postcommand=lambda: update_cblist(lista_mat_tp))
lista_mat_tp.set("Escolha uma opção")

calc1 = Button(root, text="Calcular", command=lambda: calculate(casco, pre_proj1,
               ejunta1, D1, lista_mat_casco, lista_mat_tp, tampo, ang_cone1, root, nome_proj1))
calc1.grid(row=15, columnspan=2, ipadx=100, pady=10)

root.config(menu=MainMenu)
root.mainloop()


##################
