from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk
from funcoesgui import submit, delete

def mat_db_wdw():
    mat_db=Toplevel()

    frame2=LabelFrame(mat_db,text="Lista de Materiais")
    frame2.grid(row=1,column=2,padx=10,pady=10,rowspan=15)

    nome_db=Label(mat_db,text="Database de Materiais")
    nome_db.grid(row=0,columnspan=4)

    nome_mat=Label(mat_db,text="Nome do material:")
    nome_mat.grid(row=1,column=0,sticky="W")

    nome_mat1=Entry(mat_db)
    nome_mat1.grid(row=1,column=1,sticky="W")

    ten_mat=Label(mat_db,text="Tensão Admissível do Material(MPa):")
    ten_mat.grid(row=2,column=0,sticky="W")

    ten_mat1=Entry(mat_db)
    ten_mat1.grid(row=2,column=1,sticky="W")

    add_btn=Button(mat_db,text="Adicionar material",command=lambda: submit(ten_mat1,nome_mat1,frame2,list_of_widgets))
    add_btn.grid(row=3,columnspan=2,ipadx=100)

    rem_btn=Button(mat_db,text="Remover material",command=lambda: delete(id_entry,frame2,list_of_widgets))
    rem_btn.grid(row=5,columnspan=2,ipadx=100)

    mat_name=Label(frame2,text="Nome")
    mat_name.grid(row=1,column=2,sticky="W")

    unit_name=Label(frame2,text="Valor(MPa)")
    unit_name.grid(row=1,column=3,sticky="W")

    id_name=Label(frame2,text="ID")
    id_name.grid(row=1,column=4,sticky="W")

    id_box=Label(mat_db,text="ID: ")
    id_box.grid(row=4,column=0,sticky="W")

    id_entry=Entry(mat_db)
    id_entry.grid(row=4,column=1,sticky="W")  

    i=2
    list_of_widgets=[]

    conn2 = sqlite3.connect('materiais.db')
    cursor2= conn2.cursor()
    cursor2.execute("SELECT *, oid FROM listamateriais")
    records=cursor2.fetchall()
    conn2.commit()
    conn2.close()

    for listamateriais in records:
        for j in range(len(listamateriais)):
            e = Label(frame2,text=listamateriais[j])
            e.grid(row=i,column=j+2)
            list_of_widgets.append(e)
        i+=1  
