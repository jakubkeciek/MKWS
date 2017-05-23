
# coding: utf-8

# In[1]:

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt

gas1=ct.Solution("gri30.xml")
#gas2=ct.Solution("gri30.xml")
#gas3=ct.Solution("gri30.xml")

list_v1=[]
list_p1=[]
width=0.01

t=273
p=ct.one_atm
while p<500000:
    gas1.TPX=t, p, 'CH4:1, O2:2, N2:7.52'
    f1 = ct.FreeFlame(gas1, width=width)
    v1=f1.get_flame_speed_reaction_sensitivities()
    list_v1.append(v1)
    list_p1.append(p/1000)
        
    """
    beta=2*np.arcsin(sl*p*np.pi*(dp/2)*(dp/2)/(ct.gas_constant*t))*180/np.pi
    list1.append(beta)
    list2.append(p/1000)
    #print ("t=%s" % t)
    #print ("p=%s" % p)
    #print ("beta=%s" % beta)
    """
    p=p+1800

plt.plot(list_p1,list_v1,'r--')
plt.xlabel('Pressure (kPa)')
plt.ylabel('V (cm/s)')
plt.title('Flame speed for T=273K')
plt.grid(True)
plt.savefig('1.png', bbox_inches='tight')
plt.show()


# In[ ]:



