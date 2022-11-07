#!/bin/bash

ref=Q01_canu.contigs.fasta
spe=Q01_canu

bwa index $ref
bwa mem -t 20 $ref ${spe}/110129_I248_FC81CK7ABXX_L2_CUCjsxRDUDIAAPEI-12_1.fq.gz ${spe}/110129_I248_FC81CK7ABXX_L2_CUCjsxRDUDIAAPEI-12_2.fq.gz  | samtools view -bS - > ${spe}.bam
samtools sort -@ 20 -m 3G ${spe}.bam -o ${spe}.sort.bam
samtools index ${spe}.sort.bam
java -Xmx100G -jar pilon-1.22.jar --genome $ref --bam  ${spe}.sort.bam --fix bases --mindepth 10 --vcf --output ${acc}_canu_pilon --outdir ./correct_1 --threads 20 --changes --tracks 1>correct_01.log 2>&1
