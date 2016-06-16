#!/usr/bin/python
import os
import sys

# get tissue from file name
# add tissue annotation to gene list
# WNK1
# Brain
# GENE:WNK1 TISSUE:Brain
# stephen.j.newhouse@gmail.com
# python 3 tested


## get cmd line args
#GENEFILE="Cerebellum_Gene_Symbol.txt"
GENEFILE=sys.argv[1]
SUFFIX="_Gene_Symbol.txt"
TISSUE = GENEFILE.replace("_Gene_Symbol.txt","")

# file to process
print("File:", GENEFILE)

# set up blank list
genes_anno = [  ]

# read file and add format it
print("Reading and formatting data: eg. [GENE:MY_GENE	TISSUE:" + TISSUE + "] added to file")

f = open(GENEFILE)
genes_line = f.readlines()
for line in genes_line:
    x = "GENE:" + line.replace("\n","\t") + "TISSUE:" + TISSUE + '\n'
    genes_anno.append(x)

#print(genes_anno)

# write to file
filename = TISSUE + '.gene_list' + '.tsv'

print("Start Writing data to:", filename)

# Open a file
fo = open(filename,  'w')

for line in genes_anno:
    fo.write(line)

# Close opend file
fo.close()

print("Done Writing data to:", filename)
