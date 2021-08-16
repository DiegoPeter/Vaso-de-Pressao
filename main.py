
from tkinter import *
from GUI import *
from matdb import *
from resdb import *
from calculos import *

conn = sqlite3.connect('storage.db')
c = conn.cursor()
c.execute("""
CREATE TABLE IF NOT EXISTS materials_list (
  mat_name text PRIMARY KEY,
  adm_tension float
)
""")
c.execute("""
CREATE TABLE IF NOT EXISTS results (
name text PRIMARY KEY,
diameter float,
pressure float,
weld_eff float,
shell_type text,
shell_mat text,
head_type text,
head_mat text,
cone_angle float,
shell_thick float,
head_thick float
)
""")
conn.commit()
conn.close()


if __name__ == '__main__':

    root = Tk()

    MainMenu = Menu(root)
    filemenu = Menu(MainMenu, tearoff=0)
    filemenu.add_command(
        label="Editar database de materiais", command=mat_db_wdw)
    filemenu.add_command(
        label="Ver histórico de resultados", command=red_db_wdw)
    filemenu.add_separator()
    filemenu.add_command(label="Sair", command=root.destroy)
    MainMenu.add_cascade(label="Opções", menu=filemenu)

    root.title("Programa Vaso de Pressão")

    title = create_Label(root, "Programa Vaso", 0, 0, 2)

    input_frame = create_LabelFrame(
        root, "Dados de Entrada", padxint=10, padyint=10)

    proj_name_label = create_Label(
        input_frame, "Nome do Projeto:", 1, 0, stickystr='W')
    proj_name_input = create_Entry(input_frame, 1, 1, stickystr='W')

    diam_label = create_Label(
        input_frame, "Diâmetro Interno:", 2, 0, stickystr='W')
    diam_input = create_Entry(input_frame, 2, 1, stickystr='W')

    pressure_label = create_Label(
        input_frame, "Pressão de Projeto:", 3, 0, stickystr='W')
    pressure_input = create_Entry(input_frame, 3, 1, stickystr='W')

    weld_efficiency_label = create_Label(
        input_frame, "Eficiência de Junta:", 4, 0, stickystr='W')
    weld_efficiency_input = create_Entry(input_frame, 4, 1, stickystr='W')

    shell = IntVar()
    shell_type_label = create_Label(
        input_frame, "Tipo de casco:", 5, 0, stickystr='W')
    shell_type_1 = create_RadioButton(
        input_frame, "Cilíndrico", shell, 1, rowint=5, columnint=1, stickystr='W', commandf=lambda: show_head(head_widgets, True))
    shell_type_2 = create_RadioButton(
        input_frame, "Esférico", shell, 2, rowint=6, columnint=1, stickystr='W', commandf=lambda: show_head(head_widgets, False))

    shell_material_label = create_Label(
        input_frame, "Tipo de Material do Casco:", 7, 0, stickystr='W')
    shell_material_combobox = create_Combobox(
        input_frame, "Escolha uma opção", 7, 1, postcommandf=lambda: update_cblist(shell_material_combobox))

    head = IntVar()
    head_widgets = []*8
    head_type_label = create_Label(input_frame, "Tipo de tampo:", show=False)
    head_widgets.append(head_type_label)
    head_type_1 = create_RadioButton(input_frame, "Elipsóidal 2:1", head,
                                     1, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, False), show=False)
    head_widgets.append(head_type_1)
    head_type_2 = create_RadioButton(input_frame, "Toro Esférico", head,
                                     2, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, False), show=False)
    head_widgets.append(head_type_2)
    head_type_3 = create_RadioButton(input_frame, "Hemisférico", head,
                                     3, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, False), show=False)
    head_widgets.append(head_type_3)
    head_type_4 = create_RadioButton(input_frame, "Cônico", head,
                                     4, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, True), show=False)
    head_widgets.append(head_type_4)
    head_type_5 = create_RadioButton(input_frame, "Toro Cônico", head,
                                     5, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, True), show=False)
    head_widgets.append(head_type_5)
    cone_angle_label = create_Label(
        input_frame, "Ângulo de cone(em graus):", show=False)
    cone_angle_entry = create_Entry(input_frame, show=False)

    head_material_label = create_Label(
        input_frame, "Tipo de material do tampo:", show=False)
    head_widgets.append(head_material_label)
    head_material_combobox = create_Combobox(
        input_frame, "Escolha uma opção", postcommandf=lambda: update_cblist(head_material_combobox), show=False)
    head_widgets.append(head_material_combobox)

    calc_button = create_Button(
        root, "Calcular", rowint=15, columnspanint=2, ipadxint=100, padyint=10, commandf=lambda: calculate(shell, pressure_input, weld_efficiency_input, diam_input, shell_material_combobox, head_material_combobox, head, cone_angle_entry, root, proj_name_input, list_of_res))

    list_of_res = []

    root.config(menu=MainMenu)
    root.mainloop()
