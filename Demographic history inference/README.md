# Fifteen schematic diagram of demographic scenarios


<img width="555" alt="image" src="https://user-images.githubusercontent.com/18697713/197721265-0428c2c4-d171-4fab-81b2-b643768682b4.png">
----
The W1 represent Ce, C1 represent C3, and C3 represnt C1 in the .tpl and .est files in [model folder](https://github.com/qiangh06/Setaria-pan-genome/tree/main/Demographic%20history%20inference/models)

# RUN
[model folder](https://github.com/qiangh06/Setaria-pan-genome/tree/main/Demographic%20history%20inference/models)
### Step 1. Make sfs files for fsc input
```
easySFS.py -i /public200T/home/heqiang/project/dadi/all_0.05_0.1.impute.vcf.gz -p pop_4.lst -a -f --proj 78,78,78,78 --prefix millet
```

### Step 2. Run fsc for each model with 30 repeats
```
for i in {1..15}; do for j in {1..30}; do cd /public200T/home/heqiang/project/dadi/RUN/model${i}_${j}/; \
echo fsc26 -t millet.tpl -e millet.est -m -0 -n 100000 -L 30 -s 0 -M -q -c 12 > model${i}_${j}.sh; \
chmod 775 model${i}_${j}.sh; qsub -N model${i}_${j} -l nodes=1:ppn=12,h_vmem=20G -S /bin/bash -cwd -j y -V -b y -o model${i}_${j}.out  sh model${i}_${j}.sh; done; done
```

### Step 3. Calculate AIC values
```
python 1.Calcu_AIC.py
```
