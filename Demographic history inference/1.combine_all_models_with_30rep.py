#!/usr/bin/env python
# -*- encoding: utf-8 -*-
#@File    :   1.combine_all_models_with_30rep.py
#@Time    :   2022/02/25 19:19:10
#@Contact :   qiangh@163.com

import os
out = open('Combined_models_30Rep.txt','w')
for i in range(1,12):
    for j in range(1,31):
        f = open('/public200T/home/heqiang/project/dadi/RUN2/model%s_%s/millet/millet.bestlhoods'%(i,j),'r')
        f.readline()
        _line = f.readline().rstrip().split()
        LH = abs(float(_line[-1])-float(_line[-2]))
        out.write('model%s\t%s\t%s\n'%(i,j,LH))
        print('model%s_%s: %s'%(i,j,LH))
        f.close()
out.close()
