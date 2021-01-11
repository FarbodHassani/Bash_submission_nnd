
"""

Created on Sat Dec  5 10:11:58 2020

@author: zahra
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#parameters
n = 2
m_min=10
data_name1 = "BigMDPL_Rockstar_z[0]_L[2500]"
num_sub_boxes = n**3

data_name_split =data_name1.split('_')
name = data_name_split[0]
halo_finder = data_name_split[1]
redshift = data_name_split[2]
L_box =int(data_name_split[3][2:-1])
#load data
data_name = './Simulations_data/'+data_name1+'.csv';
#data_name = data_name+'.csv'
data = pd.read_csv(data_name)
data['log_mass'] = np.log10(data['mass'])
data = data[data['log_mass']>m_min]
xyz = data[['x','y','z']].values



num_den = len(data)/(L_box**3)
r_star=(3/(4*np.pi*num_den))**(1/3)
#divide to subboxes
def sample_space (n):
    arr =[]
    for i in range (n):
        for j in range (n):
            for k in range (n):
                arr.append((i,j,k))
    return(arr)
SubBox = []
condition_x=[]
condition_y=[]
condition_z=[]
# conditions
for i in range(n):
    condition_x.append((L_box*i/n< xyz[:,0]) & ( xyz[:,0] <L_box*(i+1.)/n))

for i in range(n):
    condition_y.append((L_box*i/n < xyz[:,1]) & ( xyz[:,1] <L_box*(i+1.)/n))

for i in range(n):
    condition_z.append((L_box*i/n < xyz[:,2]) & ( xyz[:,2] <L_box*(i+1.)/n))
# Making sub-boxisez
SubBox = []

for i in range (num_sub_boxes):
    SubBox.append(xyz[ (condition_x[sample_space(n)[i][0]]) & (condition_y[sample_space(n)[i][1]]) & (condition_z[sample_space(n)[i][2]])])

# NND Calculation

nnd=[]
nnd_r=[]
for k in range(num_sub_boxes):
    nnd.append([])

for k in range(num_sub_boxes):
    nnd_r.append([])

for i in range(num_sub_boxes):
    xyz=SubBox[i][:,0:3]
    for index,pos in enumerate(xyz):
        dist = np.sqrt(np.sum((pos-xyz)**2,axis=1))
        nnd[i].append(np.amin(dist[dist!=0]))   #Nearest Neighbor Distance
        #for calculating J-function
    xr = np.random.uniform(np.amin(xyz[:,0]),np.amax(xyz[:,0]),len(xyz))
    yr = np.random.uniform(np.amin(xyz[:,1]),np.amax(xyz[:,1]),len(xyz))
    zr = np.random.uniform(np.amin(xyz[:,2]),np.amax(xyz[:,2]),len(xyz))
    xyz_r = np.vstack((xr,yr,zr)).T
    for index,pos in enumerate(xyz_r):
        dist = np.sqrt(np.sum((pos-xyz)**2,axis=1))
        nnd_r[i].append(np.amin(dist))
nnd = np.array(pd.DataFrame(nnd))
nnd_r = np.array(pd.DataFrame(nnd_r))
bins = np.logspace(-1,1.7,101)
pdf = []
for l in range(num_sub_boxes):
    pdf.append([])

for l in range(num_sub_boxes):
    pdf[l],bins,_ = plt.hist(nnd[l,:][~np.isnan(nnd[l,:])],bins,density=True);


pdf_normal = np.array(pdf)*r_star
bincenters = 0.5*(bins[1:]+bins[:-1])
new_bins = bincenters/r_star
pdf_normal_mean = pdf_normal.mean(axis=0)
pdf_normal_std = pdf_normal.std(axis=0)
pdf = np.array(pdf)
pdf_mean = pdf.mean(axis=0)
G= []
F= []
for k in range(num_sub_boxes):
    G.append([])
for k in range(num_sub_boxes):
    G[k],bins,_ = plt.hist(nnd[k,:][~np.isnan(nnd[k,:])],bins,density=True,cumulative=True);

for l in range(num_sub_boxes):
    F.append([])
for l in range(num_sub_boxes):
    F[l],bins,_ = plt.hist(nnd_r[l,:][~np.isnan(nnd_r[l,:])],bins,density=True,cumulative=True);
J = (1-np.array(G))/(1-np.array(F))
J_mean = J.mean(axis=0)
J_std = J.std(axis=0)
poisson_error = 1/np.sqrt((len(data))*np.diff(bins)*pdf_mean)

pdf_nnd_data = np.vstack((new_bins,pdf_normal,pdf_normal_mean,pdf_normal_std,poisson_error)).T
J_data = np.vstack((new_bins,J,J_mean,J_std)).T
  #?????????????????????????????????


    #saving data
address = './'+'sim['+data_name1+']_m_min['+str(m_min)+']_n_num['+str(n)+']/';
name_nnd = address + 'NND'+'_'+name+'_'+halo_finder+'_'+redshift+'_sample'+str([m_min])+'_numsubbox'+str([n])+'.txt'
name_nnd_r = address + 'NND_R'+'_'+name+'_'+halo_finder+'_'+redshift+'_sample'+str([m_min])+'_numsubbox'+str([n])+'.txt'
name_J = address + 'J-function'+'_'+name+'_'+halo_finder+'_'+redshift+'_sample'+str([m_min])+'_numsubbox'+str([n])+'.txt'
name_pdf_nnd = address + 'PDF'+'_'+'NND'+'_'+name+'_'+halo_finder+'_'+redshift+'_sample'+str([m_min])+'_numsubbox'+str([n])+'.txt'

np.savetxt(name_nnd,nnd,header=str(len(data)),comments='')
np.savetxt(name_nnd_r,nnd_r,header=str(len(data)),comments='')
np.savetxt(name_pdf_nnd,pdf_nnd_data,header=str(len(data)),comments='')
np.savetxt(name_J,J_data,header=str(len(data)),comments='')


'''end'''
