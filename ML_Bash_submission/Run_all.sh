#!/bin/sh


seed1=0;
for ((l = 0 ; l < 10 ; l++)); do

seed1=$((seed1+1));
output_dir='sim_seed_['$seed1']'
echo $output_dir;
echo $seed1;
#########
[ ! -d "$output_dir" ] && mkdir -p "$output_dir"

sed -e 's/seed = 40/seed ='$seed1'/g' -e 's/output path = output/output path ='$output_dir' setting_lcdm.ini> settings_$output_dir.ini

#sed -e 's/srun -n 400 --ntasks-per-node=12 -c 1 .\/gevolution -n 20 -m 20 -s #setting_lcdm.ini/srun -n 400 --ntasks-per-node=12 -c 1 .\/gevolution -n 20 -m 20 -s settings_$output_dir.ini/g' Run_big_pre > Run_$output_dir.sh

sbatch Run_$output_dir.sh
done
