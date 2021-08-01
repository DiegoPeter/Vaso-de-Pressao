from tkinter import *
import sqlite3
from tkinter import messagebox

# Limpar lista de materiais da janela do db de materiais


def clearGrid(list_of_widgets):
    for widget in list_of_widgets:
        widget.destroy()


# Checar se é Float
def isfloat(var):
    funciona = False
    try:
        float(var)
        funciona = True
    except ValueError:
        funciona = False
    return funciona


# Checar se é Int
def isInt(var):
    funciona = False
    try:
        int(var)
        funciona = True
    except ValueError:
        funciona = False
    return funciona


# Fazer update constante do seletor de materiais
def update_cblist(lista_mat_casco):
    conn = sqlite3.connect('materiais.db')
    cursor1 = conn.cursor()
    cursor1.execute("SELECT nome_mat FROM listamateriais")
    vlist = []
    for row in cursor1.fetchall():
        vlist.append(row[0])
    lista_mat_casco['values'] = vlist
    conn.commit()
    conn.close()


def get_valor(nome):
    conn = sqlite3.connect('materiais.db')
    cursor1 = conn.cursor()
    cursor1.execute(
        f"SELECT tensao_adm FROM listamateriais WHERE nome_mat='{nome.get()}'")
    ret = cursor1.fetchall()
    conn.commit()
    conn.close()
    if len(ret) != 1:
        return None
    return ret[0][0]


# botao adicionar material na janela do db de materiais
def submit(ten_mat1, nome_mat1, frame2, list_of_widgets):
    if check_str_field(nome_mat1, "Nome do material") and check_float_field(ten_mat1, "Tensão admissível do material"):
        conn = sqlite3.connect('materiais.db')
        cursor1 = conn.cursor()
        cursor1.execute("SELECT *, oid FROM listamateriais")
        records = cursor1.fetchall()
        shouldInsert = True
        for record in records:
            if record[0] == nome_mat1.get():
                aux = messagebox.askquestion(
                    "Erro", "Já existe um material com este nome.\nDeseja sobreescrever?")
                if aux == 'no':
                    shouldInsert = False
        if shouldInsert:
            cursor1.execute("INSERT INTO listamateriais VALUES (:nome_mat, :ten_mat) ON CONFLICT(nome_mat) DO UPDATE SET tensao_adm=excluded.tensao_adm",
                            {
                                'nome_mat': nome_mat1.get(),
                                'ten_mat': float(ten_mat1.get())
                            }
                            )
        cursor1.execute("SELECT *, oid FROM listamateriais")
        records = cursor1.fetchall()
        i = 2
        for listamateriais in records:
            for j in range(len(listamateriais)):
                e = Label(frame2, text=listamateriais[j])
                e.grid(row=i, column=j+2)
                list_of_widgets.append(e)
            i += 1
        conn.commit()
        conn.close()

        nome_mat1.delete(0, END)
        ten_mat1.delete(0, END)


# botao remover material na janela db de materiais
def delete(id_entry, frame2, list_of_widgets):
    if check_int_field(id_entry, "O ID"):
        conn = sqlite3.connect('materiais.db')
        cursor1 = conn.cursor()
        cursor1.execute("DELETE from listamateriais WHERE oid= :id_entry", {
            'id_entry': id_entry.get()
        })
        cursor1.execute("SELECT *, oid FROM listamateriais")
        records = cursor1.fetchall()
        i = 2
        clearGrid(list_of_widgets)
        for listamateriais in records:
            for j in range(len(listamateriais)):
                e = Label(frame2, text=listamateriais[j])
                e.grid(row=i, column=j+2)
                list_of_widgets.append(e)
            i += 1
        conn.commit()
        conn.close()
        id_entry.delete(0, END)


# mostrar opcoes de tipo de tampo quando casco cilindrico for selecionado
def show_tampo(tipotampo, tp1, tp2, tp3, tp4, tp5, tipo_mat_tp, lista_mat_tp):
    tipotampo.grid(row=8, column=0, sticky="W")
    tp1.grid(row=8, column=1, sticky="W")
    tp2.grid(row=9, column=1, sticky="W")
    tp3.grid(row=10, column=1, sticky="W")
    tp4.grid(row=11, column=1, sticky="W")
    tp5.grid(row=12, column=1, sticky="W")
    tipo_mat_tp.grid(row=13, column=0, sticky='W')
    lista_mat_tp.grid(row=13, column=1, sticky='W')


# esconder opcoes de tipo de tampo quando casco esferico for selecionado
def hide_tampo(tipotampo, tp1, tp2, tp3, tp4, tp5, tipo_mat_tp, lista_mat_tp, ang_cone, ang_cone1):
    tipotampo.grid_forget()
    tp1.grid_forget()
    tp2.grid_forget()
    tp3.grid_forget()
    tp4.grid_forget()
    tp5.grid_forget()
    tipo_mat_tp.grid_forget()
    lista_mat_tp.grid_forget()
    ang_cone.grid_forget()
    ang_cone1.grid_forget()


# mostrar opcao de ang de cone dependendo da selecao
def show_angcone(ang_cone, ang_cone1):
    ang_cone.grid(row=14, column=0, sticky='W')
    ang_cone1.grid(row=14, column=1, sticky='W')


# esconder opcao de ang de cone dependendo da selecao
def hide_angcone(ang_cone, ang_cone1):
    ang_cone.grid_forget()
    ang_cone1.grid_forget()


# checagem de campos float vazios
def check_float_field(field, nome):
    if len(field.get()) == 0:
        messagebox.showinfo("Erro", f"{nome} está vazio")
        return False
    elif not isfloat(field.get()):
        messagebox.showinfo("Erro", f"{nome} tem que ser um número")
        field.delete(0, END)
        return False
    return True


# checagem de campos str vazios
def check_str_field(field, nome):
    if len(field.get()) == 0:
        messagebox.showinfo("Erro", f"{nome} está vazio")
        return False
    return True


# checagem de campos int vazios
def check_int_field(field, nome):
    if len(field.get()) == 0:
        messagebox.showinfo("Erro", f"{nome} está vazio")
        return False
    elif not isInt(field.get()):
        messagebox.showinfo("Erro", f"{nome} tem que ser um número")
        field.delete(0, END)
        return False
    return True


# checagem de radiobts
def check_radio_field(field, nome, min, max):
    if field.get() < min or field.get() > max:
        messagebox.showinfo("Erro", f"{nome} está vazio")
        return False
    return True


# check mat field
def check_mat_field(field, nome):
    if get_valor(field) == None:
        messagebox.showinfo("Erro", f"{nome} está vazio")
        return False
    return True


# delete from resdb
def delete_res(id_entry, frame, lista):
    if check_int_field(id_entry, "O ID"):
        conn = sqlite3.connect('resultados.db')
        cursor1 = conn.cursor()
        cursor1.execute("DELETE from vaso WHERE oid= :id_entry", {
            'id_entry': id_entry.get()
        })
        cursor1.execute("SELECT *, oid FROM vaso")
        records = cursor1.fetchall()
        i = 1
        clearGrid(lista)
        for listares in records:
            for j in range(len(listares)):
                e = Label(frame, text=listares[j])
                e.grid(row=i, column=j)
                lista.append(e)
            i += 1
        conn.commit()
        conn.close()
        id_entry.delete(0, END)
