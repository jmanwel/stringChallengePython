def StringChallenge(strParam):
    ct = "30e5dmvcf"
    nl = list(strParam)    
    for i in range(len(nl)):  
        if nl[i] == "M" and i == 0:                
            nl[0] = ""
        elif nl[i] == "M" and i != 0:
            prev = nl[i-1]                        
            nl[i] = prev            
        if nl[i] == "N" and i != len(nl):
            prox = nl[i+1]    
            nl[i]= prox
        if nl[i] == "N" and i == len(nl):                                                            
            nl[i] = ""
    nl = [x for x in nl if x !=""]
    salida = f"{''.join(nl)}{ct}"
    s1 = list(salida)
    for i in range(len(s1)):
        if i % 4 ==0 and i !=0:
            s1[i] = "_"
    salida = ''.join(s1)
    return salida
    
print(StringChallenge("MrtyNNgMM"))
