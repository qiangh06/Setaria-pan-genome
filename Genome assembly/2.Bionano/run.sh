#!/bin/bash

ref=${acc}_pilon.contigs.fasta

RefAligner -i ${acc}_RawMolecules.bnx -minlen 100 -merge -o ${acc}_RawMolecules.filter100kb -bnx

perl fa2cmap_multi_color.pl -i $ref -e CTTAAG 1

python align_bnx_to_cmap.py --prefix AM --mol ${acc}_RawMolecules.filter100kb.bnx --ra RefAligner/1.0/ --ref assembly_CTTAAG_0kb_0labels.cmap --nthreads 20 --output ${acc}_bnx2cmap --snrFilter 2 --color 1

python pipelineCL.py -U -d -T 20 -j 4 -N 10 -i 5 -b ${acc}_RawMolecules.filter100kb.bnx -l ${acc}_BN_asm.output -t RefAligner/1.0/ -a optArguments_nonhaplotype_noES_noCut_BG_saphyr.xml

perl hybridScaffold.pl -n assembly.fasta -b kbs-mac-74_bng_contigs2017.cmap -c hybridScaffold_config.xml -r RefAligner -o ${acc}_hybrid -B 1 -N 2
