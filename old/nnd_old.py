
"""

Created on Sat Dec  5 10:11:58 2020

@author: zahra
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#parameters
L_box = 400
n = 2
m_min=10
n_mass_sample=3
num_sub_boxes = n**3
name = 'smdpl'
redshift= 0
#load data
data_name1 = "z0m5e11.csv"
data_name ='./Simulations_data/'+data_name1;
data = pd.read_csv(data_name);

data['log_mass'] = np.log10(data['mass'])
mass_sample = []
m = m_min
for i in range(n_mass_sample):
    mass_sample.append(data[data['log_mass']>m][['x','y','z']].values)
    m += 0.5

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
for j in range(n_mass_sample):
    condition_x.append([])
for j in range(n_mass_sample):
    condition_y.append([])
for j in range(n_mass_sample):
    condition_z.append([])

for j in range (n_mass_sample):
    for i in range(n):
        condition_x[j].append((L_box*i/n< np.array(mass_sample[j])[:,0]) & ( np.array(mass_sample[j])[:,0] <L_box*(i+1.)/n))
for j in range (n_mass_sample):
    for i in range(n):
        condition_y[j].append((L_box*i/n < np.array(mass_sample[j])[:,1]) & ( np.array(mass_sample[j])[:,1] <L_box*(i+1.)/n))
for j in range (n_mass_sample):
    for i in range(n):
        condition_z[j].append((L_box*i/n < np.array(mass_sample[j])[:,2]) & ( np.array(mass_sample[j])[:,2] <L_box*(i+1.)/n))
# Making sub-boxisez
SubBox = []
for j in range(n_mass_sample):
    SubBox.append([])
for j in range(n_mass_sample):
    for i in range (num_sub_boxes):
        SubBox[j].append(np.array(mass_sample[j])[ (condition_x[j][sample_space(n)[i][0]]) & (condition_y[j][sample_space(n)[i][1]]) & (condition_z[j][sample_space(n)[i][2]])])

# NND Calculation
for j in range(n_mass_sample):
    nnd = []
    for k in range(num_sub_boxes):
        nnd.append([])
    nnd_r = []
    for k in range(num_sub_boxes):
        nnd_r.append([])

    for i in range(num_sub_boxes):
        xyz=SubBox[j][i][:,0:3]
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
    bins = np.logspace(-1,1.8,200)
    pdf = []
    for l in range(num_sub_boxes):
        pdf.append([])

    for l in range(num_sub_boxes):
        pdf[l],bins,_ = plt.hist(nnd[l,:][~np.isnan(nnd[l,:])],bins,density=True);
    pdf = np.array(pdf)
    bincenters = 0.5*(bins[1:]+bins[:-1])
    pdf_mean = pdf.mean(axis=0)
    pdf_std = pdf.std(axis=0)
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
    nnd_data = np.vstack((bincenters,pdf_mean,pdf_std)).T
    J_data = np.vstack((bincenters,J_mean,J_std)).T
    m = m_min + (j*0.5)


    #saving data
    address = './'+'sim['+data_name1+']_m_min['+str(m_min)+']_n_num['+str(n)+']/';
    name_nnd =address + 'NND'+'-'+name+'-'+'z'+str(redshift)+'-sample'+str(m)+'-num_subbox'+str(num_sub_boxes)+'.txt'
    name_J = address+ 'J-function'+'-'+name+'-'+'z'+str(redshift)+'-sample'+str(m)+'-num_subbox'+str(num_sub_boxes)+'.txt'
    np.savetxt(name_nnd,nnd_data,header=str(len(mass_sample[j])),comments='')
    np.savetxt(name_J,J_data,header=str(len(mass_sample[j])),comments='')

'''end'''
