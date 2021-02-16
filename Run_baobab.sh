#!/bin/bash                                                                                                              

#SBATCH -J name                                                                                                          
#SBATCH --get-user-env                                                                                                   
#SBATCH --ntasks=1                                                                                                     
#SBATCH --cpus-per-task=1                                                                                                
#SBATCH -p dpt-bigmem-EL7                                                                                                      
#SBATCH --output=slurm-test-%J.out                                                                                       
#SBATCH -t 7-00:00:00                                                                                                     
#SBATCH --mail-type=FAIL
#SBATCH --mem-per-cpu=64000                                                                                                

##cd ##ROOTDIR##                                                                                           

#source /etc/profile.modules                                                                                             
#module load foss/2018b HDF5 GSL
ml GCC/8.2.0-2.31.1 OpenMPI/3.1.3 Python/3.7.2 SciPy-bundle/2019.03

echo Running on host `hostname`
echo Time is `date`
echo Directory is `pwd`
echo Slurm job ID is $SLURM_JOBID

python nnd_final.py

