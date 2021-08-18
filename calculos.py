import math
from tkinter import *
from GUI import *
from tkinter import messagebox
from create_pdf import create_pdf
from res import *


def calculate(shell, pre, weld_eff, diam, shell_mat, head_mat, head, cone_angle, root, proj_name, list_of_res, saddle_A, saddle_angle, shell_length,fluid_dens,fluid_level):

    clearGrid(list_of_res)

    data_in = [["Característica", "Valor", "Unidade", ]]
    if not check_str_field(proj_name, "Nome do projeto"):
        return

    if not check_float_field(diam, "Diâmetro Interno"):
        return
    data_in.append(["Diâmetro Interno", f"{diam.get()}", "mm", ])
    if not check_float_field(pre, "Pressão de projeto"):
        return
    data_in.append(["Pressão de Projeto", f"{pre.get()}", "MPa", ])
    if not check_float_field(weld_eff, "Eficiência de junta"):
        return
    data_in.append(["Eficiência de Junta", f"{diam.get()}", "-", ])
    if not check_radio_field(shell, "Tipo de casco", 1, 2):
        return
    if shell.get() == 1:
        data_in.append(["Tipo de casco", "Cilíndrico", "-", ])
    else:
        data_in.append(["Tipo de casco", "Esférico", "-", ])
    if not check_mat_field(shell_mat, "Material do casco"):
        return
    data_in.append(["Material do casco", shell_mat.get(), "-", ])
    if not check_float_field(saddle_A, "Distância entre suportes"):
        return
    data_in.append(["Distância entre suportes", f"{saddle_A.get()}", "mm"])
    if not check_radio_field(saddle_angle, "Ângulo do suport", 120, 150):
        return
    data_in.append(["Ângulo do Suporte", f"{saddle_angle.get()}", "Graus"])
    if shell.get() == 1:
        if not check_float_field(shell_length, "Comprimento do casco"):
            return
        data_in.append(["Comprimento do casco", f"{shell_length.get()}", "mm"])
        if not check_radio_field(head, "Tipo de tampo", 1, 5):
            return
        if head.get() == 1:
            data_in.append(["Tipo de tampo", "Elipsóidal 2:1", "-", ])
        elif head.get() == 2:
            data_in.append(["Tipo de tampo", "Toro Esférico", "-", ])
        elif head.get() == 3:
            data_in.append(["Tipo de tampo", "Hemisférico", "-", ])
        elif head.get() == 4:
            data_in.append(["Tipo de tampo", "Cônico", "-", ])
        else:
            data_in.append(["Tipo de tampo", "Toro Cônico", "-", ])
        if not check_mat_field(head_mat, "Material do tampo"):
            return
        data_in.append(["Material do tampo", head_mat.get(), "-", ])
        if head.get() > 3:
            if not check_float_field(cone_angle, "Ângulo de cone"):
                return
            data_in.append(
                ["Ângulo de cone", f"{cone_angle.get()}", "Graus", ])
    if not check_float_field(fluid_dens,"Densidade do fluido"):
        return
    data_in.append(["Densidade do Fluido",f"{fluid_dens.get()}","kg/mm3"])
    if not check_float_field(fluid_level,"Nivel do fluido"):
        return
    data_in.append(["Nivel do Fluido",f"{fluid_level.get()}%","-"])
    data_out = [["Característica", "Valor", "Unidade", ]]

    frame_res = root.create_LabelFrame(
        "Resultados", 0, 2, 2, padxint=10, padyint=10, rowspanint=15)

    list_of_res.append(frame_res)

    # Puxando os dados dos campos
    shell_type = shell.get()

    P = float(pre.get())
    WE = float(weld_eff.get())
    D = float(diam.get())
    S = get_valor(shell_mat)
    S1 = get_valor(head_mat)
    La = float(saddle_A.get())
    Sa = float(saddle_angle.get())

    if shell_type == 1:
        Ls = float(shell_length.get())
        head_type = head.get()
        if head_type == 4 or head_type == 5:
            alpha = math.radians(float(cone_angle.get()))
    else:
        Ls = D

    if La > Ls:
        messagebox.showinfo(
            "Erro", "A distância entre suportes tem que ser menor que o comprimento do casco")
        return

    A = (Ls - La)/2
    # Calculando raio e raio de coroa
    R = D/2
    L = 0.9*D

    if A > R/2:
        messagebox.showinfo(
            "Erro", "A distância entre suportes excede os limites da norma")
    if Sa == 120:
        K2=0.880
        Kst=0.0132
        Khs=0.401
        Kas=0.204
    else:
        K2=0.485
        Kst=0.0079
        Khs=0.297
        Kas=0.260
    # Calculo espessura do casco e tampo
    if shell_type == 1:
        if P <= 0.385*S*WE:
            circunf_thick = (P*R)/(S*WE - 0.6*P)
        else:
            messagebox.showinfo(
                "Erro", "O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
            return
        if P <= 1.25*S*WE:
            long_thick = (P*R)/(2*S*WE + 0.4*P)
        else:
            messagebox.showinfo(
                "Erro", "O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
            return
        shell_thick = max(circunf_thick, long_thick)
        if head_type == 1:
            Hint=D/4
            head_thick = (P*D)/(2*S1*WE - 0.2*P)
        elif head_type == 2:
            Hint=D/3.8
            head_thick = (0.885*P*L)/(S1*WE-0.1*P)
        elif head_type == 3:
            Hint=R
            head_thick = (P*L)/(2*S1*WE-0.2*P)
        elif head_type == 4:
            Hint=R/math.tan(alpha)
            head_thick = (P*D)/(2*math.cos(alpha)*(S1*WE-0.6*P))
        elif head_type == 5:
            Di = L*2*math.cos(alpha)
            head_thick = (P*Di)/(2*math.cos(alpha)*(S*WE-0.6*P))
    else:
        if P <= 0.665*S*WE:
            shell_thick = (P*R)/(2*S*WE - 0.2*P)
        else:
            messagebox.showinfo(
                "Erro", "O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
            return


    #Calculo suportes


    data_out.append(["Espessura mínima do casco",
                    f"{shell_thick:.2f}", "mm", ])

    shell_thick_label = frame_res.create_Label(
        "Espessura do casco:", 1, 3, stickystr='W')
    list_of_res.append(shell_thick_label)

    shell_thick_res = frame_res.create_Label(
        f'{shell_thick:.2f} mm', 1, 4, stickystr='W')
    list_of_res.append(shell_thick_res)

    saddle_dist_label= frame_res.create_Label("Distância casco-suporte:",3,3,stickystr='W')
    list_of_res.append(saddle_dist_label)
    saddle_dist = frame_res.create_Label(f'{A:.2f} mm',3,4,stickystr='W')
    list_of_res.append(saddle_dist)
    if shell_type == 1:

        data_out.append(["Espessura mínima do tampo",
                        f"{head_thick:.2f}", "mm", ])
        head_thick_label = frame_res.create_Label(
            "Espessura do tampo:", 2, 3, stickystr='W')
        list_of_res.append(head_thick_label)

        head_thick_res = frame_res.create_Label(
            f'{head_thick:.2f} mm', 2, 4, stickystr='W')
        list_of_res.append(head_thick_res)

    name = proj_name.get()
    pdf_button = root.create_Button("Gerar PDF", lambda: create_pdf(
        name, data_in, data_out), 20, 2, 2, ipadxint=100, padyint=10, padxint=10)
    list_of_res.append(pdf_button)

    if shell_type == 1:
        shell_name = "Cilíndrico"
        if head_type == 1:
            head_name = "Elipsóidal 2:1"
            x = results(name, D, P, WE, shell_name, shell_mat.get(
            ), head_name, head_mat.get(), None, head_thick, shell_thick)
        elif head_type == 2:
            head_name = "Toro Esférico"
            x = results(name, D, P, WE, shell_name, shell_mat.get(
            ), head_name, head_mat.get(), None, head_thick, shell_thick)
        elif head_type == 3:
            head_name = "Hemisférico"
            x = results(name, D, P, WE, shell_name, shell_mat.get(
            ), head_name, head_mat.get(), None, head_thick, shell_thick)
        elif head_type == 4:
            head_name = "Cônico"
            x = results(name, D, P, WE, shell_name, shell_mat.get(
            ), head_name, head_mat.get(), cone_angle.get(), head_thick, shell_thick)
        else:
            head_name = "Toro Cônico"
            x = results(name, D, P, WE, shell_name, shell_mat.get(
            ), head_name, head_mat.get(), cone_angle.get(), head_thick, shell_thick)
    else:
        shell_name = "Esférico"
        x = results(name, D, P, WE, shell_name, shell_mat.get(
        ), None, None, None, None, shell_thick)

    x.save()
