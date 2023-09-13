#!/usr/bin/python
# -*-coding : utf-8 -*-
# @Time  : 2020/8/2 15:55
# @File  : 4.mkvcf_for_inv.py
# __author__ = 'qiangh'
import glob,os

files = glob.glob('/datalus/heqiang/millet/analysis/PAV/syri/ref_yugu1/snd/*')

fa = open('/datalus/heqiang/millet/genomes/softlinks/Yugu1.fa','r')
dic = {}
for line in fa:
    if line.startswith('>'):
        name = line.rstrip()[1:]
        dic[name] = []
    else:
        dic[name].append(line.rstrip())
for key in dic:
    dic[key] = ''.join(dic[key])
fa.close()

for fs in files:
    if os.path.isdir(fs):
        name = os.path.basename(fs)
        print(name)
        dic2 = {}
        fsa = open('/datalus/heqiang/millet/genomes/chrs/%s.fa'%name,'r')
        out = open(name+'.vcf','w')
        for line in fsa:
            if line.startswith('>'):
                ids = line.rstrip()[1:]
                dic2[ids] = []
            else:
                dic2[ids].append(line.rstrip())
        for key in dic2:
            dic2[key] = ''.join(dic2[key])
        f = open(fs+'/'+'invOut.txt','r')
        for line in f:
            if line.startswith('#'):
                _line = line[1:].strip().split('\t')
                ref = dic[_line[0]][int(_line[1])-1:int(_line[2])]
                alt = dic2[_line[4]][int(_line[5])-1:int(_line[6])]
                if ref.count('N')==0 and alt.count('N')==0:
                    out.write(_line[0]+'\t'+_line[1]+'\t.\t'+ref+'\t'+alt+'\t30\tPASS\t.\tGT\t1/1\n')
        out.close()
        f.close()
        fsa.close()
