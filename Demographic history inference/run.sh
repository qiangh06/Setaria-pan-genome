#Step 1. make SFS files
easySFS.py -i /datalus/heqiang/millet/analysis/evolution/dadi/all_0.05_0.1.impute.vcf.gz -p pop_7.lst -a -f --proj 79,79,79,79,79,79,79 --prefix all_7_group

#Step 2. Run fsc
for i in {1..16}; do for j in {1..30}; do \
cd /public200T/home/heqiang/project/dadi/RUN/model${i}_${j}; \
echo fsc26 -t millet.tpl -e millet.est -m -0 -n 100000 -L 30 -s 0 -M -q -c 12 > model${i}_${j}.sh; \
chmod 775 model${i}_${j}.sh; \
qsub -N model${i}_${j} -l nodes=1:ppn=12,h_vmem=15G -S /bin/bash -cwd -j y -V -b y -o model${i}_${j}.out -e model${i}_${j}.err sh model${i}_${j}.sh; done ;done

#Step 3. Calculate AIC 
python calcu_AIC.py 
