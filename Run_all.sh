#!/bin/sh

data1=("SMDPL_Rockstar_z[05]_L[400]" "SMDPL_Rockstar_z[1]_L[400]" "SMDPL_Rockstar_z[0]_L[400]" "SMDPL_FOF_z[05]_L[400]" "SMDPL_FOF_z[1]_L[400]" "SMDPL_FOF_z[0]_L[400]" "MDPL2_Rockstar_z[05]_L[1000]" "MDPL2_Rockstar_z[1]_L[1000]" "MDPL2_Rockstar_z[0]_L[1000]" "MDPL2_FOF_z[05]_L[1000]" "MDPL2_FOF_z[1]_L[1000]" "MDPL2_FOF_z[0]_L[1000]" "MDPL_FOF_z[05]_L[1000]" "MDPL_FOF_z[1]_L[1000]" "MDPL_FOF_z[0]_L[1000]" "BigMDPL_Rockstar_z[05]_L[2500]" "BigMDPL_Rockstar_z[1]_L[2500]" "BigMDPL_Rockstar_z[0]_L[2500]")


m_min1=("10" "10.5" "11" "11.5" "12" "12.5" "13" "14" "15")

ll=0;
for ((l = 0 ; l < 18 ; l++)); do
data=${data1[$l]}

for ((j = 0 ; j < 9 ; j++)); do
m_min=${m_min1[$j]}

ll=$((ll+1));
output_dir='sim['$data']_m_min['$m_min']'
echo $output_dir;
echo $j$k$l;
echo $ll;
#########
[ ! -d "$output_dir" ] && mkdir -p "$output_dir"

sed -e 's/m_min=10/m_min='$m_min'/g' -e 's/data_name1 = "z0m5e11.csv"/data_name1 = "'$data'"/g' nnd_final.py> ./"$output_dir"/Code_$output_dir.py

sed -e 's/python nnd_final.py/python .\/'$output_dir'\/Code_'$output_dir.py'/g' -e 's/#SBATCH -J job1/#SBATCH -J job1'$j$k$l'/g' Run_baobab.sh > Run_$output_dir.sh
#
sbatch Run_$output_dir.sh
done
done