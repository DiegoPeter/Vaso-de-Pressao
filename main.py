
from tkinter import *
from GUI import *
from matdb import *
from resdb import *
from calculos import *


if __name__ == '__main__':

    root = GUI(window_type.main, "Programa Vasos",
               mat_db_wdw=mat_db_wdw, res_db_wdw=res_db_wdw)

    input_frame = root.create_LabelFrame(
        "Dados de Entrada", padxint=10, padyint=10)

    proj_name_label = input_frame.create_Label(
        "Nome do Projeto:", 0, 0, stickystr='W')
    proj_name_input = input_frame.create_Entry(0, 1, stickystr='W')

    diam_label = input_frame.create_Label(
        "Diâmetro Interno(mm):", 1, 0, stickystr='W')
    diam_input = input_frame.create_Entry(1, 1, stickystr='W')

    pressure_label = input_frame.create_Label(
        "Pressão de Projeto(MPa):", 2, 0, stickystr='W')
    pressure_input = input_frame.create_Entry(2, 1, stickystr='W')

    weld_efficiency_label = input_frame.create_Label(
        "Eficiência de Junta:", 3, 0, stickystr='W')
    weld_efficiency_input = input_frame.create_Entry(3, 1, stickystr='W')

    shell = IntVar()
    shell_type_label = input_frame.create_Label(
        "Tipo de casco:", 4, 0, stickystr='W')
    shell_type_1 = input_frame.create_RadioButton(
        "Cilíndrico", shell, 1, rowint=4, columnint=1, stickystr='W', commandf=lambda: show_head(head_widgets, True))
    shell_type_2 = input_frame.create_RadioButton(
        "Esférico", shell, 2, rowint=5, columnint=1, stickystr='W', commandf=lambda: show_head(head_widgets, False))

    shell_material_label = input_frame.create_Label(
        "Tipo de Material do Casco:", 6, 0, stickystr='W')
    shell_material_combobox = input_frame.create_Combobox(
        "Escolha uma opção", 6, 1, postcommandf=lambda: update_cblist(shell_material_combobox))

    head = IntVar()
    head_widgets = []*8

    saddle_A_label = input_frame.create_Label(
        "Distância entre suportes:", 7, 0, stickystr='W')
    saddle_A_input = input_frame.create_Entry(7, 1, stickystr='W')

    saddle_angle = IntVar()
    saddle_angle_label = input_frame.create_Label(
        "Ângulo do suporte:", 8, 0, stickystr='W')
    saddle_angle_120 = input_frame.create_RadioButton(
        "120°", saddle_angle, 120, None, 8, 1)
    saddle_angle_150 = input_frame.create_RadioButton(
        "150°", saddle_angle, 150, None, 9, 1)

    length_label = input_frame.create_Label(
        "Comprimento do casco(mm):", stickystr='W', show=False)
    head_widgets.append(length_label)
    length_input = input_frame.create_Entry(stickystr='W', show=False)
    head_widgets.append(length_input)

    head_type_label = input_frame.create_Label("Tipo de tampo:", show=False)
    head_widgets.append(head_type_label)
    head_type_1 = input_frame.create_RadioButton("Elipsóidal 2:1", head,
                                                 1, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, False), show=False)
    head_widgets.append(head_type_1)
    head_type_2 = input_frame.create_RadioButton("Toro Esférico", head,
                                                 2, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, False), show=False)
    head_widgets.append(head_type_2)
    head_type_3 = input_frame.create_RadioButton("Hemisférico", head,
                                                 3, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, False), show=False)
    head_widgets.append(head_type_3)
    head_type_4 = input_frame.create_RadioButton("Cônico", head,
                                                 4, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, True), show=False)
    head_widgets.append(head_type_4)
    head_type_5 = input_frame.create_RadioButton("Toro Cônico", head,
                                                 5, commandf=lambda: show_cone_angle(cone_angle_label, cone_angle_entry, True), show=False)
    head_widgets.append(head_type_5)
    cone_angle_label = input_frame.create_Label(
        "Ângulo de cone(em graus):", show=False)
    cone_angle_entry = input_frame.create_Entry(show=False)

    head_material_label = input_frame.create_Label(
        "Tipo de material do tampo:", show=False)
    head_widgets.append(head_material_label)
    head_material_combobox = input_frame.create_Combobox(
        "Escolha uma opção", postcommandf=lambda: update_cblist(head_material_combobox), show=False)
    head_widgets.append(head_material_combobox)

    fluid_label = input_frame.create_Label("Densidade do fluido(kg/mm3):",18,0,stickystr='W')
    fluid_entry = input_frame.create_Entry(18,1,stickystr='W')

    fluid_level_label = input_frame.create_Label("Nível do fluido no vaso(%):",19,0,stickystr='W')
    fluid_level_entry = input_frame.create_Spinbox(0,100,19,1,stickystr='W')

    calc_button = root.create_Button("Calcular", rowint=20, columnspanint=2, ipadxint=100, padyint=10, commandf=lambda: calculate(
        shell, pressure_input, weld_efficiency_input, diam_input, shell_material_combobox, head_material_combobox, head, cone_angle_entry,
         root, proj_name_input, list_of_res, saddle_A_input, saddle_angle, length_input))

    list_of_res = []

    root.window.mainloop()
