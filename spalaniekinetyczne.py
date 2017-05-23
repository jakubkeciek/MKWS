
# coding: utf-8

# In[1]:

import cantera as ct
import numpy as np
import matplotlib.pyplot as plt
# we have 1 mole per second molar expense

sl=4.1 # normal stechiometry burning speed cm/s
dp=1 # burner diametral cm

list1=[]
list2=[]
p=ct.one_atm
t=273
while p<500000:
    beta=2*np.arcsin(sl*p*np.pi*(dp/2)*(dp/2)/(ct.gas_constant*t))*180/np.pi
    list1.append(beta)
    list2.append(p/1000)
    #print ("t=%s" % t)
    #print ("p=%s" % p)
    #print ("beta=%s" % beta)
    p=p+1800
plt.plot(list2,list1,'r--')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Beta (deg)')
plt.title('Angle of kinetic flame for T=273K')
plt.grid(True)
plt.savefig('1.png', bbox_inches='tight')
plt.show()

list3=[]
list4=[]
p=ct.one_atm
t=373
while p<500000:
    beta=2*np.arcsin(sl*p*np.pi*(dp/2)*(dp/2)/(ct.gas_constant*t))*180/np.pi
    list3.append(beta)
    list4.append(p/1000)
    #print ("t=%s" % t)
    #print ("p=%s" % p)
    #print ("beta=%s" % beta)
    p=p+1800
plt.plot(list4,list3,'g--')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Beta (deg)')
plt.title('Angle of kinetic flame for T=373K')
plt.grid(True)
plt.savefig('2.png', bbox_inches='tight')
plt.show()

list5=[]
list6=[]
p=ct.one_atm
t=473
while p<500000:
    beta=2*np.arcsin(sl*p*np.pi*(dp/2)*(dp/2)/(ct.gas_constant*t))*180/np.pi
    list5.append(beta)
    list6.append(p/1000)
    #print ("t=%s" % t)
    #print ("p=%s" % p)
    #print ("beta=%s" % beta)
    p=p+1800
plt.plot(list6,list5,'b--')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Beta (deg)')
plt.title('Angle of kinetic flame for T=473K')
plt.grid(True)
plt.savefig('3.png', bbox_inches='tight')
plt.show()

list7=[]
list8=[]
p=ct.one_atm
t=573
while p<500000:
    beta=2*np.arcsin(sl*p*np.pi*(dp/2)*(dp/2)/(ct.gas_constant*t))*180/np.pi
    list7.append(beta)
    list8.append(p/1000)
    #print ("t=%s" % t)
    #print ("p=%s" % p)
    #print ("beta=%s" % beta)
    p=p+1800
plt.plot(list8,list7,'y--')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Beta (deg)')
plt.title('Angle of kinetic flame for T=573K')
plt.grid(True)
plt.savefig('4.png', bbox_inches='tight')
plt.show()

list9=[]
list10=[]
p=ct.one_atm
t=673
while p<500000:
    beta=2*np.arcsin(sl*p*np.pi*(dp/2)*(dp/2)/(ct.gas_constant*t))*180/np.pi
    list9.append(beta)
    list10.append(p/1000)
    #print ("t=%s" % t)
    #print ("p=%s" % p)
    #print ("beta=%s" % beta)
    p=p+1800
plt.plot(list10,list9,'m--')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Beta (deg)')
plt.title('Angle of kinetic flame for T=673K')
plt.grid(True)
plt.savefig('5.png', bbox_inches='tight')
plt.show()

list11=[]
list12=[]
p=ct.one_atm
t=773
while p<500000:
    beta=2*np.arcsin(sl*p*np.pi*(dp/2)*(dp/2)/(ct.gas_constant*t))*180/np.pi
    list11.append(beta)
    list12.append(p/1000)
    #print ("t=%s" % t)
    #print ("p=%s" % p)
    #print ("beta=%s" % beta)
    p=p+1800
plt.plot(list12,list11,'c--')
plt.xlabel('Pressure (kPa)')
plt.ylabel('Beta (deg)')
plt.title('Angle of kinetic flame for T=773K')
plt.grid(True)
plt.savefig('6.png', bbox_inches='tight')
plt.show()


# In[ ]:



