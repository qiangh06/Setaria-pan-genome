# 1. Phylogenetic tree

#1.1 MEGA for 1844 samples
megacc -a ./megacc_nj.mao -d all.fa -f Fasta
#1.2 iqtree for 112 samples
echo '/home/data1/SNPhylo/snphylo.sh -v 112_snp.recode.vcf  -A -b -B 1000 -P Si112' |qsub -V -cwd -j y -q bio05.q -o tree.out.txt
zip -r SNPhylo_tree.zip ./*
python vcf2phylip.py -i 112_snp.recode.vcf
echo 'iqtree -s 112_snp.recode.min4.phy -m MFP+ASC  -alrt 1000 -bb 1000 -nt AUTO' |qsub -V -cwd -j y -q bio05.q -o iqtree.out.txt


# 2. Population structure
for i in {2..20}; do admixture -s time --cv /datalus/heqiang/millet/analysis/evolution/data/NGS/1844/all_0.05_0.1.bed ${i} | tee log${i}.out; done
for i in {1..10}; do admixture -s ${i} --cv /datalus/heqiang/millet/analysis/evolution/data/NGS/1844/all_0.05_0.1.bed 7 -j20 | tee log7_${i}.out; done



