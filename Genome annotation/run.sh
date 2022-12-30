#Repeat Annotation:
ltr_finder  -a ps_scan -s eukaryotic-tRNAs.fa $genome_fasta >ltr.result
RepeatModeler -engine ncbi -pa 4 -database "db" > modeler.out
tblastx  PGSB.databse $ltr_fasta -o tblastx.all.ltr  -nogaps mformat=2
awk '$3<=1e-10 && $11 >= 30 && $12 >= 30 {print}' tblastx.all.ltr >tblastx.rep.out
RepeatMasker -gff -xsmall -no_is -pa 4 $genome_fasta -lib $repbase_database -nolow -e rmblast

#Gene Annotation using augustus(Training)
perl randomSplit.pl $gb_file 20   # *.gb.train   *.gb.test
perl optimize_augustus.pl --species=$specie_name --rounds=5 --cpus=12 --kfold=10 $gb_file\.test --onlytrain=$gb_file\.train --metapars=$augustus/config/species/$specie_name/$specie_name\_metapars.cfg > optimize.out
etraining --species=$specie_name  $gb_file.train   #training
augustus --species=$specie_name $gb_file.test > test.2.withoutCRF.out     #evaluate accuracy
#generated model used for gene annotation by maker


#Gene prediction using SNAP:
maker2zff -c 0.8 -e 0.8 -o 0.8 -x 0.2 genome.all.gff
fathom -categorize 1000 genome.ann genome.dna
fathom -export 1000 -plus uni.ann uni.dna
forge export.ann export.dna
hmm-assembler.pl snap . > snap.hmm
#generated snap.hmm use for gene annotation by maker



#assembly RNAseq using trinity:
Trinity --seqType fq --max_memory 50G  \
--left condA_1.fq.gz,condB_1.fq.gz,condC_1.fq.gz \
--right condA_2.fq.gz,condB_2.fq.gz,condC_2.fq.gz \
--CPU 6  



#Gene annotation using maker
mpiexec -n 40  maker -base $basename
gff3_merge -d *index.log -n -g
fasta_merge -d *index.log

#gene function annotation using interproscan:
sh interproscan.sh  -mode cluster -clusterrunid uniqueName  -iprlookup -pa -goterms -i $file  -f tsv

