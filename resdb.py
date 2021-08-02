from tkinter import *
import sqlite3
from tkinter import messagebox
from funcoesgui import delete_res, pdf_res


def red_db_wdw():
    res_db = Toplevel()

    frame_res = LabelFrame(res_db, text='Histórico de Projetos')
    frame_res.grid(row=0, columnspan=12, pady=10, padx=10)

    nome = Label(frame_res, text='Nome do Vaso')
    nome.grid(row=0, column=0)

    diam = Label(frame_res, text='Diâmetro Interno')
    diam.grid(row=0, column=1)

    pre = Label(frame_res, text='Pressão de Projeto')
    pre.grid(row=0, column=2)

    ejunta = Label(frame_res, text='Eficiência de Junta')
    ejunta.grid(row=0, column=3)

    tcasco = Label(frame_res, text='Tipo de Casco')
    tcasco.grid(row=0, column=4)

    matcasco = Label(frame_res, text='Material do Casco')
    matcasco.grid(row=0, column=5)

    ttampo = Label(frame_res, text='Tipo de Tampo')
    ttampo.grid(row=0, column=6)

    mattampo = Label(frame_res, text='Material do Tampo')
    mattampo.grid(row=0, column=7)

    angcone = Label(frame_res, text='Ângulo de Cone')
    angcone.grid(row=0, column=8)

    espcasco = Label(frame_res, text='Espessura mínima do Casco')
    espcasco.grid(row=0, column=9)

    esptampo = Label(frame_res, text='Espessura mínima do Tampo')
    esptampo.grid(row=0, column=10)

    ID = Label(frame_res, text='ID')
    ID.grid(row=0, column=11)

    i = 1
    lista_res = []
    conn2 = sqlite3.connect('resultados.db')
    cursor2 = conn2.cursor()
    cursor2.execute("SELECT *, oid FROM vaso")
    records = cursor2.fetchall()
    conn2.commit()
    conn2.close()

    for listaresultados in records:
        for j in range(len(listaresultados)):
            res1 = Label(frame_res, text=listaresultados[j])
            res1.grid(row=i, column=j)
            lista_res.append(res1)
        i += 1

    identry_lb = Label(res_db, text="ID:")
    identry_lb.grid(row=10, column=0)

    identry = Entry(res_db)
    identry.grid(row=10, column=1)

    rmv_btn = Button(res_db, text='Remover Vaso', command=lambda: delete_res(
        identry, frame_res, lista_res))
    rmv_btn.grid(row=10, column=2, ipadx=100, pady=10)

    pdf_btn = Button(res_db, text="Gerar PDF",
                     command=lambda: pdf_res(identry))
    pdf_btn.grid(row=10, column=3, ipadx=100, pady=10)
