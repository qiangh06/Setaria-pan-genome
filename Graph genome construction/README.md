### Step1. combine all PAV vcfs
```shell
#需要修改py文件中的输入文件路径
python 1.combine_PAV_vcf.py
```

### Step2. make inverstion vcf for each accession
```shell
#需要修改py文件中的基因组信息和输入文件路径
python 2.1.mkvcf_inv.py
```

### Step3. make vcf for Vgtoolkit
```shell
#修改py文件中输入文件路径
python 3.1.mkvcf_Vg.py
```
