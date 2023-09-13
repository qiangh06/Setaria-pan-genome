#!/usr/bin/python
# -*-coding : utf-8 -*-
# @Time  : 2020/8/3 7:47
# @File  : 6.combine_VCF.py
# __author__ = 'qiangh'
import glob,os

def longest(ar):
    tmp = []
    for i in ar:
        tmp.append(len(i))
    idx = tmp.index(max(tmp))
    nc = ar[idx]
    return nc

def replaces(al,seq):
    if len(al[0]) == len(al[1]) and len(al[0])==1:
        outsq = [seq,al[1]+seq[1:]]
    if len(al[0])>len(al[1]):
        size = len(al[0]) - len(al[1])+1
        outsq = [seq,al[1]+seq[size:]]
    if len(al[0]) < len(al[1]):
        outsq = [seq,al[1]+seq[1:]]
    return outsq

files = glob.glob('/datalus/heqiang/millet/analysis/PAV/syri_svmu_sv/vcfs/INDEL/*.vcf')

dic = {}
dic_pos = {}
samples = []
out = open('combined.vcf','w')
out2 = open('combined_GT.vcf','w')
for fs in files:
    name = os.path.basename(fs).split('.')[0]
    samples.append(name)
    dic[name] = {}
    f = open(fs,'r')
    f.readline()
    f.readline()
    f.readline()
    print(name)
    for line in f:
        _line = line.rstrip().split('\t')
        key = '-'.join(_line[0:2])
        dic[name][key] = _line[3:5]
        dic_pos[key]=1
    f.close()
out.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t'+'\t'.join(samples)+'\n')
out2.write('#CHROM\tPOS\tID\tREF\tALT\tQUAL\tFILTER\tINFO\tFORMAT\t'+'\t'.join(samples)+'\n')
for pos in dic_pos:
    tmp = []
    tmp2 = []
    al1 = []
    al2 = []
    for sample in samples:
        if pos in dic[sample]:
            #print(dic[sample][pos])
            al1.append(dic[sample][pos][0])
    ref = longest(al1)
    #alt = ','.join(alt)
    for sample in samples:
        if pos in dic[sample]:
            gt = replaces(dic[sample][pos],ref)[1]
            al2.append(gt)
            tmp.append(gt)
        else:
            tmp.append(ref)
    alt = list(set(al2))
    alt.sort()
    for nc in tmp:
        if nc == ref:
            tmp2.append('0/0')
        else:
            tmp2.append(str(alt.index(nc)+1)+'/'+str(alt.index(nc)+1))
    outline = pos.split('-')+['.',ref,','.join(alt),'30','PASS','.','GT']+tmp
    outline2 = pos.split('-')+['.',ref,','.join(alt),'30','PASS','.','GT']+tmp2
    out.write('\t'.join(outline)+'\n')
    out2.write('\t'.join(outline2)+'\n')
out.close()
