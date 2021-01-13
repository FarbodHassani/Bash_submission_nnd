#!/bin/bash                                                                                                              

#SBATCH -J name                                                                                                          
#SBATCH --get-user-env                                                                                                   
#SBATCH --ntasks=1                                                                                                     
#SBATCH --cpus-per-task=1                                                                                                
#SBATCH -p dpt-EL7                                                                                                       
#SBATCH --output=slurm-test-%J.out                                                                                       
#SBATCH -t 7-00:00:00                                                                                                     
#SBATCH --mail-type=FAIL                                                                                                 

##cd ##ROOTDIR##                                                                                                         

#source /etc/profile.modules                                                                                             
#module load foss/2018b HDF5 GSL
echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo Slurm job ID is $SLURM_JOBID

python ./sim[MDPL_FOF_z[05]_L[1000]]_m_min[12]/Code_sim[MDPL_FOF_z[05]_L[1000]]_m_min[12].py

