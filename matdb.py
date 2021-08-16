from tkinter import *
import sqlite3
from GUI import *


def mat_db_wdw():
    mat_db = Toplevel()

    mat_frame = create_LabelFrame(
        mat_db, "Lista de Materiais", rowint=1, columnint=2, padxint=10, padyint=10, rowspanint=15)

    db_name = create_Label(
        mat_db, "Database de Materiais", rowint=0, columnspanint=4)

    mat_name_label = create_Label(
        mat_db, "Nome do material:", 1, 0, stickystr='W')

    mat_name_entry = create_Entry(mat_db, 1, 1, stickystr='W')

    mat_ten_label = create_Label(
        mat_db, "Tensão Admissível do Material(MPa):", 2, 0, stickystr='W')

    mat_ten_entry = create_Entry(mat_db, 2, 1, stickystr='W')

    add_button = create_Button(mat_db, "Adicionar Material", commandf=lambda: submit(
        mat_ten_entry, mat_name_entry, mat_frame, list_of_widgets), rowint=3, columnspanint=2, ipadxint=100, padyint=10)

    remove_button = create_Button(mat_db, "Remover material", lambda: delete(
        id_entry, mat_frame, list_of_widgets), 5, columnspanint=2, ipadxint=100, padyint=10)

    mat_name = create_Label(mat_frame, "Nome", 1, 2, stickystr='W')

    unit_name = create_Label(mat_frame, "Valor(MPa)", 1, 3, stickystr='W')

    id_name = create_Label(mat_frame, "ID", 1, 4, stickystr='W')

    id_box = create_Label(mat_db, "ID: ", 4, 0, stickystr='W')

    id_entry = create_Entry(mat_db, 4, 1, stickystr='W')

    i = 2
    list_of_widgets = []

    conn = sqlite3.connect('storage.db')
    c = conn.cursor()
    c.execute("SELECT *, oid FROM materials_list")
    records = c.fetchall()
    conn.commit()
    conn.close()

    for materials in records:
        for j in range(len(materials)):
            e = create_Label(mat_frame, materials[j], i, j+2)
            list_of_widgets.append(e)
        i += 1
