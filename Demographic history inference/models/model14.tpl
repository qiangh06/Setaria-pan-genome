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
2
//Migration matrix 0
0.000 MIGA01 0.000 0.000
0.000 0.000 0.000 0.000
0.000 MIGA21 0.000 0.000
0.000 0.000 0.000 0.000
//Migration matrix 1
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
0.000 0.000 0.000 0.000
//historical event: time, source, sink, migrants, new deme size, new growth rate, migration matrix index
3 historical event
TDIV13 1 3 1 RESIZE13 0 1
TDIV23 2 3 1 RESIZE23 0 1
TDIV30 3 0 1 1 0 1
//Number of independent loci [chromosome] 
1 0
//Per chromosome: Number of contiguous linkage Block: a block is a set of contiguous loci
1
//per Block:data type, number of loci, per generation recombination and mutation rates and optional parameters
FREQ 1 0 OUTEXP