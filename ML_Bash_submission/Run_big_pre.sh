#!/bin/bash

#SBATCH --account=s1051                                                                                                                                                                                      
#SBATCH --job-name="LCDM"                                                                                                                                                                             
#SBATCH --time=10:00:00                                                                                                                                                                                     
#SBATCH --partition=normal                                                                                                                                                                                  
#SBATCH --ntasks=400                                                                                                                                                                                       
#SBATCH --ntasks-per-node=12                                                                                                                                                                                
#SBATCH --cpus-per-task=1                                                                                                                                                                                   
#SBATCH --constraint=gpu                                                                                                                                                                                    
#SBATCH --output=gevolution.%j.o                                                                                                                                                                            
#SBATCH --error=gevolution.%j.e   

##cd ##ROOTDIR##

#source /etc/profile.modules
module load daint-gpu
module load cray-hdf5-parallel
module load cray-fftw/3.3.8.7
module load GSL
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/users/farbodh/Documents/LightCone-kessence/Healpix_3.31/lib
export LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/users/farbodh/Documents/LightCone-kessence/cfitsio


echo "The current job ID is $SLURM_JOB_ID"
echo "Running on $SLURM_NNODES nodes"
echo "Using $SLURM_NTASKS_PER_NODE tasks per node"
echo "A total of $SLURM_NTASKS tasks is used"
srun -n 400 --ntasks-per-node=12 -c 1 ./gevolution -n 20 -m 20 -s setting_lcdm.ini
