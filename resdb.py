from tkinter import *
from GUI import *
import sqlite3
from tkinter import messagebox


def red_db_wdw():
    res_db = Toplevel()

    res_frame = create_LabelFrame(
        res_db, 'Histórico de Projetos', 0, columnspanint=12, padyint=10, padxint=10)

    name = create_Label(res_frame, 'Nome do Vaso', 0, 0)

    diam = create_Label(res_frame, 'Diâmetro Interno', 0, 1)

    pre = create_Label(res_frame, 'Pressão de Projeto', 0, 2)

    weld_eff = create_Label(res_frame, 'Eficiência de Junta', 0, 3)

    shell_type = create_Label(res_frame, 'Tipo de Casco', 0, 4)

    shell_mat = create_Label(res_frame, 'Material do Casco', 0, 5)

    head_type = create_Label(res_frame, 'Tipo de Tampo', 0, 6)

    head_mat = create_Label(res_frame, 'Material do Tampo', 0, 7)

    cone_angle = create_Label(res_frame, 'Ângulo de Cone', 0, 8)

    shell_thick = create_Label(res_frame, 'Espessura mínima do Casco', 0, 9)

    head_thick = create_Label(res_frame, 'Espessura mínima do Tampo', 0, 10)

    ID = create_Label(res_frame, 'ID', 0, 11)

    i = 1
    res_list = []
    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM results")
    records = c.fetchall()
    conn.commit()
    conn.close()

    for results in records:
        for j in range(len(results)):
            res = create_Label(res_frame, results[j], i, j)
            res_list.append(res)
        i += 1

    identry_lb = create_Label(res_db, "ID:", 10, 0)

    identry = create_Entry(res_db, 10, 1)

    rmv_btn = create_Button(res_db, 'Remover Vaso', lambda: delete_res(
        identry, res_frame, res_list), 10, 2, ipadxint=100, padyint=10)

    pdf_btn = create_Button(res_db, "Gerar PDF",
                            lambda: pdf_res(identry), 10, 3, ipadxint=100, padyint=10)
