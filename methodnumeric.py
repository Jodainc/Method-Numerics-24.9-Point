import numpy as npp
from matplotlib import pyplot as plt
from numpy  import array


x_data = npp.array([87.8, 96.6, 176, 263, 351, 571,834,1129,1624,2107,2678,3380,4258])
y_data = npp.array([153,204,255,306,357,408,459,510,561,612,663,714,765])

s=[87.8, 96.6, 176, 263, 351, 571,834,1129,1624,2107,2678,3380,4258]
#s1= s*1e+3;
e=[153,204,255,306,357,408,459,510,561,612,663,714,765]

se = []
ee=[]
sr=[0,0,0,0,0,0,0,0,0]
desder=[0,0,0,0,0,0,0,0,0]
for i in s:
        se.append(i * 1e+3)
     

    
for i in e:
        ee.append(i * 1e-3)
        
     
    
idx=5

np=len(s)-idx
for i in range(0,np):
    sr[i]=s[idx+i]
de=51e-3;
dde=2*de;
for i in range(0,np-1):
    if i>0 :
        desder[i]= (sr[i+1]-sr[i-1])/dde
    else:
        desder[0]= ((-sr[2])+4*sr[1]-3*sr[0])/dde
      
desder[np]= (3*sr[np-1]-(4*sr[np-2])+sr[np-3])/dde
desder[np-1]= (3*sr[np-1]-(4*sr[np-2])+sr[np-3])/dde
print(3*sr[np-1] )
print(-4*sr[np-2] )
print(sr[np-3] )
print(dde )
print(desder )
x_data = array( sr)
y_data =array( desder )

c1 = npp.polyfit(x_data,y_data,1)
a= c1[0]
eo=c1[1]
sp=[0,0,0,0,0,0]       
dsde1=npp.polyval(c1,sp)
#plt.plot(sp,dsde1,sr,desder,'-')
ep = [0 for x in range(163)]
for i in range(1,161): 
    if i==0:
         ep[0]= 0.00000 
    else:
          ep[i]= ep[i-1] + 0.00500

sp=(eo/a)*(npp.exp(a*ep)-1)
#punto b
#plt.plot(ep,sp,e,s,'*')
sStart=s[10];
eStart=e[10];
sBar=sStart/(npp.exp(a*eStart)-1)
sp2=sBar*(npp.exp(a*ep)-1)
#punto C
plt.plot(ep,sp2,e,s,'*')
