#15 models for demographic inference

<img width="555" alt="image" src="https://user-images.githubusercontent.com/18697713/197721265-0428c2c4-d171-4fab-81b2-b643768682b4.png">


#Model 1
modle1.est:
[PARAMETERS]
//#isInt? #name   #dist.#min  #max
//all N are in number of haploid individuals
1  Ce         unif     10  100000     output
1  C1         unif     10  20000     output
1  C2         unif     10  20000     output
1  C3         unif     10  20000     output
1  AN_SIZE21  unif     10  1000000    output
1  AN_SIZE31  unif     10  1000000    output
1  TDIV10     unif     10  13000   output
1  TDIV21     unif     10    13000    output
1  TDIV31     unif     10    13000    output
0  OUTEXP     unif     0   0.5    hide

[RULES]

TDIV10 > TDIV21
TDIV21 > TDIV31

[COMPLEX PARAMETERS]
1  RESIZE31 = AN_SIZE31/C1       hide
1  RESIZE21 = AN_SIZE21/AN_SIZE31       hide


model1.tpl
//Parameters for the coalescence simulation program : simcoal.exe
4 samples to simulate :
//Population effective sizes (number of genes)
Ce
C1
C2
C3
//Samples sizes and samples age 
158
158
158
158
//Growth rates: negative growth implies population expansion
0
0
0
0
//Number of migration matrices : 0 implies no migration between demes
0
//historical event: time, source, sink, migrants, new deme size, new growth rate, migration matrix index
3 historical event
TDIV31 3 1 1 RESIZE31 0 0
TDIV21 2 1 1 RESIZE21 0 0
TDIV10 1 0 1 1 0 0
//Number of independent loci [chromosome] 
1 0
//Per chromosome: Number of contiguous linkage Block: a block is a set of contiguous loci
1
//per Block:data type, number of loci, per generation recombination and mutation rates and optional parameters
FREQ 1 0 OUTEXP

