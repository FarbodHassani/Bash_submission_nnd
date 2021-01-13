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

python ./sim[BigMDPL_Rockstar_z[0]_L[2500]]_m_min[12.5]/Code_sim[BigMDPL_Rockstar_z[0]_L[2500]]_m_min[12.5].py

