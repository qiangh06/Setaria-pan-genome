### Step1. combine all PAV vcfs
```shell
#需要修改py文件中的输入文件路径
python 1.combine_PAV_vcf.py
```

### Step2. make inversion vcf for each accession
```shell
#需要修改py文件中的基因组信息和输入文件路径
python 2.1.mkvcf_inv.py
```

### Step3. make vcf for Vgtoolkit
```shell
#修改py文件中输入文件路径
python 3.1.mkvcf_Vg.py
```
### Step4. make vg index

注意：通过脚本合并的vcf没有vcf表头，进行vg index构建之前，需要额外添加vcf表头
