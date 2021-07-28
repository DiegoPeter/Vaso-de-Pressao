import math
def esp_casco(type,P,S,E,R):
    if type == 1:
        if P <= 0.385*S*E:
            tcircunf=(P*R)/(S*E - 0.6*P)
        else:
            print('ERRO - Pressão de projeto excede limites estabelecidos pela norma ASME, considere trocar de material')
            exit
        if P <= 1.25*S*E:
            tlong=(P*R)/(2*S*E + 0.4*P)
        else:
            print('ERRO - Pressão de projeto excede limites estabelecidos pela norma ASME, considere trocar de material')
            exit
        t1=max(tcircunf,tlong)
        return t1
    elif type == 2:
        if P <= 0.665*S*E:
            t1=(P*R)/(2*S*E - 0.2*P)
            return t1
        else:
            print('ERRO - Pressão de projeto excede limites estabelecidos pela norma ASME, considere trocar de material')
            exit
    else:
        print('Erro no input do tipo de casco')
        exit

def esp_tampo(type,P,S,E,D,L,alpha):
    if type==1:
        t2=(P*D)/(2*S*E - 0.2*P)
        return t2
    elif type==2:
        t2=(0.885*P*L)/(S*E-0.1*P)
        return t2
    elif type==3:
        t2=(P*L)/(2*S*E-0.2*P)
        return t2
    elif type==4:
        t2=(P*D)/(2*math.cos(alpha)*(S*E-0.6*P))
        return t2
    elif type==5:
        Di=L*2*math.cos(alpha)
        t2=(P*Di)/(2*math.cos(alpha)*(S*E-0.6*P))
        return t2
    else:
        print('Erro no input do tipo de tampo')
        exit
