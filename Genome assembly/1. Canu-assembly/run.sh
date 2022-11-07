canu -p ${acc} -d ${fd} genomeSize=420m -pacbio-raw ${acc}.pacbio.fastq.gz
awk '{if($1~/>/){print $1}else{print}}' ${acc}_canu.contigs.fasta > tmp && mv tmp ${acc}_canu.contigs.fasta
