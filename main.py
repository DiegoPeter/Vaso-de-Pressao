import math
from espessura import esp_casco, esp_tampo
from create_pdf import create_pdf

nome_proj=input('Digite o nome do projeto: ')
#Definição de Variáveis
P=10 #Pressão de Projeto em Mpa
D=2000 #Diametro em mm
S=82.7 #Tensão Admissível em Mpa
E=0.85 #Eficiência de Junta considerando que será parcialmente radiografado
Ca=6 #Sobreespessura de corrosão
R=D/2 #Raio em mm
L=0.9*D #Raio interno de coroa
Inout=3 # Quantidade de entradas e saídas
alpha=0 #Angulo do Cone em radianos

casco=1 #Definição de tipo de casco: 1=cilíndrico ; 2=esférico
tampo=1 #Definição de tipo de tampo: 1=Elipsoidal 2:1 ; 2=Toro Esférico ; 3=Hemisférico ; 4=Cônico ; 5= Toro Cônico

#Espessura do casco
t1=esp_casco(casco,P,S,E,R)

#Espessura Tampo
t2=esp_tampo(tampo,P,S,E,D,L,alpha)

#Diâmetro Entradas e Saídas
if D<=1520:
    if D/2 > 510:
        Da=510
    else:
        Da=D/2
else:
    if D/3 > 1020:
        Da=1020
    else:
        Da=D/3

print('A espessura mínima do casco será de: ',t1,' mm')
print('A espessura mínima do tampo será de: ',t2,' mm')
print('O diâmetro das aberturas será de: ',Da,'mm')

create_pdf(nome_proj,P,D,S,E,casco,tampo,t1,t2,Da)