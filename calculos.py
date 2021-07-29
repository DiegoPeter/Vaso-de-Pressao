import math
from tkinter import *
from funcoesgui import get_valor
from tkinter import messagebox
from tkinter import ttk
from create_pdf import create_pdf

def calculate(casco,pre_proj1,ejunta1,D1,lista_mat_casco,lista_mat_tp,tampo,ang_cone1,root,nome_proj1):

    #Puxando os dados dos campos
    type_casco=casco.get()

    P=float(pre_proj1.get())
    E=float(ejunta1.get())
    D=float(D1.get())
    S=get_valor(lista_mat_casco)
    S1=get_valor(lista_mat_tp)

    if type_casco==1:
        type_tampo=tampo.get()
        if type_tampo==4 or type_tampo==5:
            alpha=ang_cone1.get()


    #Calculando raio e raio de coroa
    R=D/2
    L=0.9*D


    #Calculo espessura do casco e tampo
    if type_casco ==1:
        if P<= 0.385*S*E:
            tcircunf=(P*R)/(S*E - 0.6*P)
        else:
            messagebox.showinfo("Erro","O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
        if P <= 1.25*S*E:
            tlong=(P*R)/(2*S*E + 0.4*P)
        else:
            messagebox.showinfo("Erro","O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
        t_casco=max(tcircunf,tlong)
        if type_tampo==1:
            t_tampo=(P*D)/(2*S1*E - 0.2*P)
        elif type_tampo==2:
            t_tampo=(0.885*P*L)/(S1*E-0.1*P)
        elif type_tampo==3:
            t_tampo=(P*L)/(2*S1*E-0.2*P)
        elif type_tampo==4:
            t_tampo=(P*D)/(2*math.cos(alpha)*(S1*E-0.6*P))
        elif type_tampo==5:
            Di=L*2*math.cos(alpha)
            t_tampo=(P*Di)/(2*math.cos(alpha)*(S*E-0.6*P))
    else:
        if P <= 0.665*S*E:
            t_casco=(P*R)/(2*S*E - 0.2*P)
        else:
            messagebox.showinfo("Erro","O valor da pressão de projeto excede aos limites da norma ASME.\nConsidere trocar de material")
    

    frame_res=LabelFrame(root,text="Resultados")
    frame_res.grid(row=1,column=2,columnspan=2,rowspan=15,padx=10,pady=10)

    esp_casco_label=Label(frame_res,text="Espessura do casco:")
    esp_casco_label.grid(row=1,column=2,sticky="W")

    esp_casco_res=Label(frame_res,text=f'{t_casco} mm')
    esp_casco_res.grid(row=1,column=3,sticky="W")

    esp_tampo_label=Label(frame_res,text="Espessura do tampo:")
    esp_tampo_label.grid(row=2,column=2,sticky="W")

    esp_tampo_res=Label(frame_res,text=f'{t_tampo} mm')
    esp_tampo_res.grid(row=2,column=3,sticky="W")
    
    nome=nome_proj1.get()
    pdf_button=Button(root,text="Gerar PDF",command=lambda: create_pdf(nome,P,D,S,E,type_casco,type_tampo,t_casco,t_tampo,S1))
    pdf_button.grid(row=15,column=2,columnspan=2,ipadx=100,pady=10)







