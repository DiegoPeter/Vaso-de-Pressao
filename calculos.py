import math
from tkinter import *
from funcoesgui import check_float_field, check_mat_field, check_radio_field, check_str_field, get_valor, clearGrid
from tkinter import messagebox
from create_pdf import create_pdf


def calculate(casco, pre_proj1, ejunta1, D1, lista_mat_casco, lista_mat_tp, tampo, ang_cone1, root, nome_proj1, list_of_res):

    clearGrid(list_of_res)

    data_in = [["Característica", "Valor", "Unidade", ]]
    if not check_str_field(nome_proj1, "Nome do projeto"):
        return

    if not check_float_field(D1, "Diâmetro do casco"):
        return
    data_in.append(["Diâmetro do Casco", f"{D1.get()}", "mm", ])
    if not check_float_field(pre_proj1, "Pressão de projeto"):
        return
    data_in.append(["Pressão de Projeto", f"{pre_proj1.get()}", "MPa", ])
    if not check_float_field(ejunta1, "Eficiência de junta"):
        return
    data_in.append(["Eficiência de Junta", f"{D1.get()}", "-", ])
    if not check_radio_field(casco, "Tipo de casco", 1, 2):
        return
    if casco.get() == 1:
        data_in.append(["Tipo de casco", "Cilíndrico", "-", ])
    else:
        data_in.append(["Tipo de casco", "Esférico", "-", ])
    if not check_mat_field(lista_mat_casco, "Material do casco"):
        return
    data_in.append(["Material do casco", lista_mat_casco.get(), "-", ])
    if casco.get() == 1:
        if not check_radio_field(tampo, "Tipo de tampo", 1, 5):
            return
        if tampo.get() == 1:
            data_in.append(["Tipo de tampo", "Elipsóidal 2:1", "-", ])
        elif tampo.get() == 2:
            data_in.append(["Tipo de tampo", "Toro Esférico", "-", ])
        elif tampo.get() == 3:
            data_in.append(["Tipo de tampo", "Hemisférico", "-", ])
        elif tampo.get() == 4:
            data_in.append(["Tipo de tampo", "Cônico", "-", ])
        else:
            data_in.append(["Tipo de tampo", "Toro Cônico", "-", ])
        if not check_mat_field(lista_mat_tp, "Material do tampo"):
            return
        data_in.append(["Material do tampo", lista_mat_tp.get(), "-", ])
        if tampo.get() > 3:
            if not check_float_field(ang_cone1, "Ângulo de cone"):
                return
            data_in.append(["Ângulo de cone", f"{ang_cone1.get()}", "Graus", ])

    data_out = [["Característica", "Valor", "Unidade", ]]

    frame_res = LabelFrame(root, text="Resultados")
    list_of_res.append(frame_res)

    # Puxando os dados dos campos
    type_casco = casco.get()

    P = float(pre_proj1.get())
    E = float(ejunta1.get())
    D = float(D1.get())
    S = get_valor(lista_mat_casco)
    S1 = get_valor(lista_mat_tp)

    if type_casco == 1:
        type_tampo = tampo.get()
        if type_tampo == 4 or type_tampo == 5:
            alpha = math.radians(float(ang_cone1.get()))

    # Calculando raio e raio de coroa
    R = D/2
    L = 0.9*D

    # Calculo espessura do casco e tampo
    if type_casco == 1:
        if P <= 0.385*S*E:
            tcircunf = (P*R)/(S*E - 0.6*P)
        else:
            messagebox.showinfo(
                "Erro", "O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
        if P <= 1.25*S*E:
            tlong = (P*R)/(2*S*E + 0.4*P)
        else:
            messagebox.showinfo(
                "Erro", "O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
        t_casco = max(tcircunf, tlong)
        if type_tampo == 1:
            t_tampo = (P*D)/(2*S1*E - 0.2*P)
        elif type_tampo == 2:
            t_tampo = (0.885*P*L)/(S1*E-0.1*P)
        elif type_tampo == 3:
            t_tampo = (P*L)/(2*S1*E-0.2*P)
        elif type_tampo == 4:
            t_tampo = (P*D)/(2*math.cos(alpha)*(S1*E-0.6*P))
        elif type_tampo == 5:
            Di = L*2*math.cos(alpha)
            t_tampo = (P*Di)/(2*math.cos(alpha)*(S*E-0.6*P))
    else:
        if P <= 0.665*S*E:
            t_casco = (P*R)/(2*S*E - 0.2*P)
        else:
            messagebox.showinfo(
                "Erro", "O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")

    data_out.append(["Espessura mínima do casco", f"{t_casco:.2f}", "mm", ])

    frame_res.grid(row=1, column=2, columnspan=2, rowspan=15, padx=10, pady=10)

    esp_casco_label = Label(frame_res, text="Espessura do casco:")
    esp_casco_label.grid(row=1, column=2, sticky="W")
    list_of_res.append(esp_casco_label)

    esp_casco_res = Label(frame_res, text=f'{t_casco:.2f} mm')
    esp_casco_res.grid(row=1, column=3, sticky="W")
    list_of_res.append(esp_casco_res)

    if type_casco == 1:

        data_out.append(["Espessura mínima do tampo", f"{t_tampo:.2f}", "mm", ])
        esp_tampo_label = Label(frame_res, text="Espessura do tampo:")
        esp_tampo_label.grid(row=2, column=2, sticky="W")
        list_of_res.append(esp_tampo_label)

        esp_tampo_res = Label(frame_res, text=f'{t_tampo:.2f} mm')
        esp_tampo_res.grid(row=2, column=3, sticky="W")
        list_of_res.append(esp_tampo_res)

    nome = nome_proj1.get()
    pdf_button = Button(root, text="Gerar PDF", command=lambda: create_pdf(
        nome, data_in, data_out))
    pdf_button.grid(row=15, column=2, columnspan=2, ipadx=100, pady=10)
    list_of_res.append(pdf_button)
