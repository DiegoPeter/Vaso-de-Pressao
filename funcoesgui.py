from tkinter import *
import sqlite3
from tkinter import messagebox
from tkinter import ttk

#Limpar lista de materiais da janela do db de materiais
def clearGrid(list_of_widgets):
    for widget in list_of_widgets:
        widget.destroy()
#Checar se é Float
def isfloat(var):
    funciona=False
    try:
        float(var)
        funciona=True 
    except ValueError:
        funciona=False
    return funciona
#Checar se é Int
def isInt(var):
    funciona=False
    try:
        int(var)
        funciona=True 
    except ValueError:
        funciona=False
    return funciona
#Fazer update constante do seletor de materiais
def update_cblist(lista_mat_casco):
    conn = sqlite3.connect('materiais.db')
    cursor1 = conn.cursor()
    cursor1.execute("SELECT nome_mat FROM listamateriais")
    vlist=[]
    for row in cursor1.fetchall():
        vlist.append(row[0])
    lista_mat_casco['values']=vlist
    conn.commit()
    conn.close()
#botao adicionar material na janela do db de materiais
def submit(ten_mat1,nome_mat1,frame2,list_of_widgets):
    
    if not  isfloat(ten_mat1.get()):
        messagebox.showinfo("Erro","O campo de tensão tem que ser um número")
        ten_mat1.delete(0, END)
    elif len(nome_mat1.get())==0 or len(ten_mat1.get())==0:
        messagebox.showinfo("Erro","Um dos campos está vazio")
    else:
        conn = sqlite3.connect('materiais.db')
        cursor1 = conn.cursor()
        # cursor1.execute("INSERT INTO listamateriais VALUES (:nome_mat, :ten_mat)",
        #     {
        #         'nome_mat': nome_mat1.get(),
        #         'ten_mat': float(ten_mat1.get())
        #     }  
        # )
        cursor1.execute("SELECT *, oid FROM listamateriais")
        records=cursor1.fetchall()
        shouldInsert=True
        for record in records:
            if record[0]==nome_mat1.get():
                aux=messagebox.askquestion("Erro","Já existe um material com este nome.\nDeseja sobreescrever?")
                if aux=='no':
                    shouldInsert=False
        if shouldInsert:
            cursor1.execute("INSERT INTO listamateriais VALUES (:nome_mat, :ten_mat) ON CONFLICT(nome_mat) DO UPDATE SET tensao_adm=excluded.tensao_adm",
                {
                    'nome_mat': nome_mat1.get(),
                    'ten_mat': float(ten_mat1.get())
                }  
            )
        cursor1.execute("SELECT *, oid FROM listamateriais")
        records=cursor1.fetchall()
        i=2
        for listamateriais in records:
            for j in range(len(listamateriais)):
                e = Label(frame2,text=listamateriais[j])
                e.grid(row=i,column=j+2)
                list_of_widgets.append(e)
            i+=1
        conn.commit()
        conn.close()

        nome_mat1.delete(0, END)
        ten_mat1.delete(0, END)

#botao remover material na janela db de materiais
def delete(id_entry,frame2,list_of_widgets):
    if not isInt(id_entry.get()):
        messagebox.showinfo("Erro","O campo de ID tem que ser um número")
        id_entry.delete(0,END)
    elif len(id_entry.get())==0:
        messagebox.showinfo("Erro","Um dos campos está vazio")
    else:
        conn = sqlite3.connect('materiais.db')
        cursor1 = conn.cursor()
        cursor1.execute("DELETE from listamateriais WHERE oid= :id_entry",{
            'id_entry': id_entry.get()
        })
        cursor1.execute("SELECT *, oid FROM listamateriais")
        records=cursor1.fetchall()
        i=2
        clearGrid(list_of_widgets)
        for listamateriais in records:
            for j in range(len(listamateriais)):
                e = Label(frame2,text=listamateriais[j])
                e.grid(row=i,column=j+2)
                list_of_widgets.append(e)
            i+=1
        conn.commit()
        conn.close()
        id_entry.delete(0,END)