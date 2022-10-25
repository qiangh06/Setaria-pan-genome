#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#@File    :   3.Calcu_AIC.py
#@Time    :   2022/03/08 11:01:18
#@Contact :   qiangh@163.com
import math
import re
import statistics

def getk(x):
    idx = x.index('[COMPLEX PARAMETERS]\n')
    count = 0
    for i in range(0,idx):
        if re.search(r'^/',x[i]) or re.search(r'^\[',x[i]) or re.search(r'^\n',x[i]):
            continue
        else:
            count += 1
    return count

out = open('sum_AIC.txt','w')
out.write('Models\tMaxEstLhood\tMaxObsLhood\tDeltaLhood\tAIC\n')
for i in range(1,16):
    model = 'model%s'%i
    k = 0
    maxest = []
    maxobs = []
    delta = []
    for j in range(1,31):
        if j == 1:
            count = 0
            est = open('model%s_%s/millet.est'%(i,j),'r')
            cont = est.readlines()
            k = getk(cont)
            est.close()
        f = open('/public200T/home/heqiang/project/dadi/RUN/model%s_%s/millet/millet.bestlhoods'%(i,j),'r')
        f.readline()
        _line = f.readline().rstrip().split()
        maxest.append(float(_line[-2]))
        maxobs.append(float(_line[-1]))
        delta.append(abs(float(_line[-2])-float(_line[-1])))
        f.close()
    maxest_m = round(sum(maxest)/len(maxest),2)
    maxobs_m = round(sum(maxobs)/len(maxobs),2)
    delta_m = round(sum(delta)/len(delta),2)
    maxest_sd = round(statistics.stdev(maxest),2)
    maxobs_sd = round(statistics.stdev(maxobs),2)
    delta_sd = round(statistics.stdev(delta),2)
    print('%s\t%s±%s\t%s±%s\t%s±%s'%(model,maxest_m,maxest_sd,maxobs_m,maxobs_sd,delta_m,delta_sd))
    print(k,maxest_m)
    AIC = round(2*int(k)-2*(maxest_m/math.log10(math.exp(1))),2)
    out.write('%s\t%s±%s\t%s±%s\t%s±%s\t%s\n'%(model,maxest_m,maxest_sd,maxobs_m,maxobs_sd,delta_m,delta_sd,AIC))
out.close()
