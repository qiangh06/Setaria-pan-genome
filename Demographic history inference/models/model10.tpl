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
4 historical event
TDIV23 2 3 1 RESIZE23 0 0
TADMIX12 1 2 PROPAD12 0 0 0
TADMIX13 1 3 1 0 0 0
TDIV30 3 0 1 1 0 0
//Number of independent loci [chromosome] 
1 0
//Per chromosome: Number of contiguous linkage Block: a block is a set of contiguous loci
1
//per Block:data type, number of loci, per generation recombination and mutation rates and optional parameters
FREQ 1 0 OUTEXP