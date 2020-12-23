#!/bin/sh

data1=("z0m5e11.csv" "z0m5e12.csv" "z0m5e13.csv" "z0m5e11.csv" "z1m5e11.csv" "z0m5e12.csv")
m_min1=("10" "11" "11.5" "12" "12.5" "13" "14")
n_num1=("1" "2" "4" "5" "8" "10")

ll=0;
for ((l = 0 ; l < 6 ; l++)); do
data=${data1[$l]}

for ((j = 0 ; j < 7 ; j++)); do
m_min=${m_min1[$j]}

for ((i = 0 ; i < 6 ; i++)); do
n_num=${n_num1[$i]}

ll=$((ll+1));
output_dir='sim['$data']_m_min['$m_min']_n_num['$n_num']'
echo $output_dir;
echo $i$j$k$l;
echo $ll;
#########
[ ! -d "$output_dir" ] && mkdir -p "$output_dir"

sed -e 's/m_min=10/m_min='$m_min'/g' -e 's/n = 2/n = '$n_num'/g' -e 's/data_name = 'z0m5e11.csv'/data_name = '$data'/g' nnd.py> ./"$output_dir"/Code_$output_dir.py

sed -e 's/python nnd.py/python .\/'$output_dir'\/Code_'$output_dir.py'/g' -e 's/#SBATCH -J job1/#SBATCH -J job1'$i$j$k$l'/g' Run_baobab.sh > Run_number$i$j$k$l.sh
#
#sbatch Run_number$i$j$k$l.sh
done
done
done