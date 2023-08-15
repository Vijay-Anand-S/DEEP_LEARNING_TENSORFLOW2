import itertools

gn_lis
gn_lis_typ_indx
ris_lis
ris_beh_lis
ris_brw_lis 
ris_crimebeh_lis
ris_lowdt_lis
ris_network_lis
ris_risky_lis
ris_rkyevt_lis
ris_rsylin_lis
ris_rskloc_lis
ris_rkyntw_lis

riskfactors=[ris_beh_lis,ris_brw_lis,ris_crimebeh_lis,ris_expusr_lis,ris_imm_lis,ris_lowdt_lis,ris_network_lis,ris_risky_lis,ris_rkyevt_lis,ris_rsylin_lis,ris_rskloc_lis,ris_rkyntw_lis]
lis2=[[]]
str1="stubResponse.set"
str2=""
str3="private "
Bool="Boolean "
Int = "Integer "
Str="String "
def replace(s, position):
    s = list(s)
    s[position] = s[position].upper()

    s = ''.join(s)
    return s

def initial_param():
    for gn in gn_lis:
        gn = replace(gn, 0)
        print(str1 + gn + "();")
    print("\n")

def typ_rtr(flag):
    if(flag==0):
        return Str
    elif(flag==1):
        return Int
    elif(flag == 2):
        return Bool

def RskFactors():
    for i in ris_lis:
        print(str3+replace(i,0   )+" "+i+";")

def BiocatchResponse():
    idx=0
    for i in gn_lis:
        print(str3+typ_rtr(gn_lis_typ_indx[idx])+i+";")
        idx=idx+1
    #print()
# for s in gn_lis:
#     s = s
#     t = list(map(''.join, itertools.product(*zip(s.upper(), s.lower()))))
#     lis2.append(t)
def final_params():
    for i in range(len(riskfactors)):
        print(ris_lis[i]+"---------")
        temp_str=str3+typ_rtr(2)
        for j in riskfactors[i]:
            print(temp_str+j+";")
        print("\n")
initial_param();
print("RiskFactors riskFactors = new RiskFactors();")
for i in range(len(riskfactors)):
    str2=""
    str_temp=replace(ris_lis[i],0)
    print(str_temp+" "+ris_lis[i]+" = new "+str_temp+"();")
    str2=ris_lis[i]+".set"
    j=riskfactors[i]
    for k in j:
        k=replace(k,0)
        temp_str=str2+k+"(true);"
        print(temp_str)
    print("\n")


print("-----------------")

BiocatchResponse()

print("-----------------")

RskFactors()

print("-----------------")
final_params()
