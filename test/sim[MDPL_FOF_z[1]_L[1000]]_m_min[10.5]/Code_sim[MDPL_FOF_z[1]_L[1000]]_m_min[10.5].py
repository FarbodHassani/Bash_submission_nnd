
"""

Created on Sat Dec  5 10:11:58 2020

@author: zahra
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#parameters
m_min=10.5
data_name1 = "MDPL_FOF_z[1]_L[1000]"

data_name_split =data_name1.split('_')
name = data_name_split[0]
halo_finder = data_name_split[1]
redshift = data_name_split[2]
L_box =int(data_name_split[3][2:-1])
if (halo_finder=='FOF'):
    m='mass'
if (halo_finder=='Rockstar'):
    m='Mvir'

#load data
#data_name = './../'+data_name+'.csv';
data_name = './Simulations_data/'+data_name1+'.csv';
data = pd.read_csv(data_name)
data['log_mass'] = np.log10(data[m])
data = data[data['log_mass']>m_min]
xyz = data[[m,'x','y','z']].values


#divide to subboxes

# NND Calculation

#nnd=np.zeros((len(data),6))
#nnd_r=np.zeros((len(data),5))
nnd= []
nnd_r=[]
    #Nearest Neighbor Distance
for i in range(len(xyz)):
    nnd.append([])
    nnd_r.append([])
for index,pos in enumerate(xyz):
    dist = np.sqrt(np.sum((pos[1:4]-xyz[:,1:4])**2,axis=1))
    nnd[index].append([pos[0],pos[1],pos[2],pos[3],np.amin(dist[dist!=0]),xyz[np.where(dist==np.amin(dist[dist!=0]))][0][0]])
    #nnd[index,0:7]=np.array([pos[0],pos[1],pos[2],pos[3],np.amin(dist[dist!=0]),xyz[np.where(dist==np.amin(dist[dist!=0]))][0][0]])

nnd=np.array(nnd)[:,0]
 #for calculating J-function
xr = np.random.uniform(0,L_box,len(data))
yr = np.random.uniform(0,L_box,len(data))
zr = np.random.uniform(0,L_box,len(data))
xyz_r = np.vstack((xr,yr,zr)).T
for index,pos in enumerate(xyz_r):
    dist = np.sqrt(np.sum((pos[0:3]-xyz[:,1:4])**2,axis=1))
    nnd_r[index].append([pos[0],pos[1],pos[2],np.amin(dist[dist!=0]),xyz[np.where(dist==np.amin(dist[dist!=0]))][0][0]])
nnd_r=np.array(nnd_r)[:,0]
    #saving data
address = './'+'sim['+data_name1+']_m_min['+str(m_min)+']/';

name_nnd = address + 'NND'+'_'+name+'_'+halo_finder+'_'+redshift+'_sample'+str([m_min])+'.txt'
name_nnd_r = address + 'NND_R'+'_'+name+'_'+halo_finder+'_'+redshift+'_sample'+str([m_min])+'.txt'
column_names_nnd = ['mass','x','y','z','nnd','mass[nn]']
column_names_nnd_r= ['x[random]','y[random]','z[random]','nnd','mass[nn]']
np.savetxt(name_nnd,nnd,header=','.join(column_names_nnd),comments='')
np.savetxt(name_nnd_r,nnd_r,header=','.join(column_names_nnd_r),comments='')



'''end'''
