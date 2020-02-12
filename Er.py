# -*- coding: utf-8 -*-
"""
Created on Wed Feb 12 13:06:22 2020

author: Luis Carlos A. Rojas Torres
email: luiscarlos.bsf@oceanica.ufrj.br
"""

from LinearViscoelastic import LinearViscoelastic
import numpy as np
import matplotlib.pyplot as plt

elastic_modulus = [38,20.14,14.3,9.97,7.25,5.15,3.4,2.1,1.8] #in MPa
relaxation_times =[0.58,3.13,18.72,125.41,1042,10942,159569,5215397]    #in seconds

PU=LinearViscoelastic(elastic_modulus,relaxation_times,23)

time=np.linspace(0,100,10001)
Temp=[23,40,60,80]

plt.subplot(1,2,1)
for i in Temp:
    EM=PU.get_Er(i,time)
    plot_label='T = '+str(i)
    plt.plot(time,EM,label=plot_label)
    plt.title('Elastic modulus [MPa]')    
    plt.xlabel('Time')
    plt.legend(loc = 'best')
    print()
plt.grid()      

plt.subplot(1,2,2)    
for i in Temp:
    EM=PU.get_Er(i,time)
    plot_label='T = '+str(i)
    plt.semilogx(time,EM,label=plot_label)
	    
    plt.title('Elastic modulus [MPa]')    
    plt.xlabel('Time')
    plt.legend(loc = 'best')
    print()
plt.grid()   