#!/usr/bin/python
# -*-coding : utf-8 -*-
# @Time  : 2020/8/3 10:07
# @File  : 1.prepare_data_for_vgindex.py
# __author__ = 'qiangh'
import glob,os
import pandas as pd

indel = open('/datalus/heqiang/millet/analysis/PAV/syri_svmu_sv/vcfs/combine/combined_GT_INDEL.vcf')
out1 = open('millet_inv.vcf','w')
out2 = open('millet_indel.vcf','w')

hd = indel.readline().rstrip().split('\t')

dic = {}
for sample in hd[hd.index('FORMAT')+1:]:
    f = open('/datalus/heqiang/millet/analysis/PAV/syri_svmu_sv/vcfs/inv/invs/%s.vcf'%sample,'r')
    for line in f:
        _line = line.rstrip().split('\t')
        _line[3] = _line[3].upper()
        _line[4] = _line[4].upper()
        #_line = line.rstrip().split('\t')
        key = '-'.join(_line[:5])
        if key not in dic:
            dic[key] = 1
    f.close()
tag = 0
for key in dic:
    tag += 1
    _line = key.split('-')
    out1.write('\t'.join(_line)+'\t'+'100\tPASS\tDP=1000,VT=INDEL\n')
out1.close()
for line in indel:
    _line = line.rstrip().split('\t')
    out2.write(('\t'.join(_line[:5])+'\t'+'100\tPASS\tDP=1000,VT=INDEL\n'))
out2.close()

df1 = pd.read_csv('millet_inv.vcf',header=None,sep='\t')
df1 = df1.sort_values(by=[0,1])
tmp = []
for i in range(0,df1.shape[0]):
    tmp.append('INV%s'%i)
df1[2] = tmp

df2 = pd.read_csv('millet_indel.vcf',header=None,sep='\t')
df2 = df2.sort_values(by=[0,1])
tmp = []
for i in range(0,df2.shape[0]):
    tmp.append('INDEL%s'%i)
df2[2] = tmp

df = df1.append(df2)
df = df.sort_values(by=[0,1])
df.to_csv('millet_indel_sv_sorted.vcf',header=None,index=None,sep='\t')
