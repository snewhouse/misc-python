#!/usr/bin/env python
import json
import requests
import time
import sys

# usage : getGeneInfoEnrichr.py <gene_list.txt>

# gene list from command line
genelist=sys.argv[1]

# Enrichr API set up. See http://amp.pharm.mssm.edu/Enrichr/help#api&q=4
ENRICHR_URL = 'http://amp.pharm.mssm.edu/Enrichr/genemap'
query_string = '?json=true&setup=true&gene=%s'

# Time stamping
print("--------------------------------------------------")
print("Enrichr API: Find terms that contain a given gene")
print("--------------------------------------------------")
print("Enrichr API: Start : %s"  % time.ctime())

# get gene list
f = open(genelist)
print("Enrichr API: Gene List: ", genelist)
# read line by line
genes = f.readlines()

# loop through genes and send to enrichr
for my_gene in genes:
    # get gene name
    gene_to_annotate = my_gene.replace("\n","").strip()
    print("Enrichr API: getting infomration on gene:", gene_to_annotate)
    # outputfile
    outputfile = gene_to_annotate + '.json'
    # open outputfile for writing
    fout = open(outputfile,'wb')
    # send request
    print("Enrichr API: running query:", ENRICHR_URL + query_string % gene_to_annotate)
    response = requests.get(ENRICHR_URL + query_string % gene_to_annotate)
    # check it ok
    if not response.ok:
        raise Exception('Error searching for terms')
    # write results     
    print("Enrichr API: sending results to :", outputfile)
    for chunk in response.iter_content(chunk_size=1024):
        if chunk:
            fout.write(chunk)
    # close output file
    fout.close()
    
# The End
print("--------------------------------------------------")
print("Enrichr API: End : %s"  % time.ctime())
print("--------------------------------------------------")
